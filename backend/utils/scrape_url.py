from urllib.parse import urlparse
from bs4 import BeautifulSoup
from tld import get_tld
from selenium import webdriver

class Data:
    def __init__(self, values):
        self.url = values[0]
        self.domain = values[1]
        self.special = values[2]
        self.https = values[3]
        self.lines = values[4]
        self.domain_title = values[5]
        self.description = values[6]
        self.socials = values[7]
        self.copyright = values[8]
        self.images = values[9]
        self.js = values[10]
        self.self_ref = values[11]
        self.has_submit = values[12]
        self.is_responsive = values[13]

    def __str__(self):
        return (f"URL: {self.url}\nDomain: {self.domain}\nSpecial: {self.special}\n"
                f"HTTPS: {self.https}\nLines: {self.lines}\nDomain Title: {self.domain_title}\n"
                f"Description: {self.description}\nSocials: {self.socials}\nCopyright: {self.copyright}\n"
                f"Images: {self.images}\nJS: {self.js}\nSelf Ref: {self.self_ref}")

    def to_dict(self):
        return {
            "url": self.url,
            "domain": self.domain,
            "special": self.special,
            "https": self.https,
            "lines": self.lines,
            "domain_title": self.domain_title,
            "description": self.description,
            "socials": self.socials,
            "copyright": self.copyright,
            "images": self.images,
            "js": self.js,
            "self_ref": self.self_ref,
            "has_submit": self.has_submit,
            "is_responsive": self.is_responsive
        }


class ScrapeService:
    def __init__(self, url):
        self.url = url

    async def fetch_url(self, url):
        try:
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")
            driver = webdriver.Chrome(options=options)
            driver.get(url)
            html_content = driver.page_source
        finally:
            driver.quit()
        return BeautifulSoup(html_content, "html.parser")

    async def get_data(self):
        try:
            print("Scraping URL")
            values = [None] * 14
            self.soup = await self.fetch_url(self.url)
            values[0] = self.url

            parsed_url = urlparse(self.url)

            special_url = self.url
            special_url = special_url.replace(get_tld(self.url), "")
            special_url = special_url.replace("www.", "")
            special_url = special_url.replace(parsed_url.scheme + "://", "")

            values[1] = self.get_domain(parsed_url)
            values[2] = self.ratio_special(self.url, special_url)
            values[3] = self.check_https(parsed_url)
            values[4] = self.num_lines_of_code(self.soup)
            values[5] = self.domain_title_match_score(self.soup, special_url, parsed_url)
            values[6] = self.check_description(self.soup)
            values[7] = self.check_socials(self.soup)
            values[8] = self.check_copyright(self.soup)
            values[9] = self.count_images(self.soup)
            values[10] = self.count_js(self.soup)
            values[11] = self.count_self_ref(parsed_url, self.soup)
            values[12] = self.has_submit_button(self.soup)
            values[13] = self.is_responsive(self.soup)

            print(values)
            return Data(values)
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def get_domain(parsed_url):
        return parsed_url.hostname

    @staticmethod
    def ratio_special(url, special_url):
        count_special = sum(not x.isalnum() for x in special_url)
        return count_special / len(url)

    @staticmethod
    def check_https(parsed_url):
        return 1 if parsed_url.scheme == "https" else 0

    @staticmethod
    def num_lines_of_code(soup: BeautifulSoup):
        # count newlines in the html content
        return str(soup).count('\n')
    

    @staticmethod
    def domain_title_match_score(soup, special_url, parsed_url):
        title_tag = soup.find('title')
        title = title_tag.string if title_tag else ''
        print(title, special_url)
        return 100

    @staticmethod
    def check_description(soup):
        meta_description = soup.find('meta', attrs={'name': 'description'})
        return 1 if meta_description else 0

    @staticmethod
    def check_socials(soup):
        social_media_domains = [
            'twitter', 'facebook', 'instagram', 'linkedin', 'youtube', 'pinterest', 'tiktok'
        ]
        anchor_tags = soup.find_all(href=True)
        return 1 if any(domain in tag['href'] for tag in anchor_tags for domain in social_media_domains) else 0

    @staticmethod
    def check_copyright(soup):
        copyright_phrases = ['©', 'All rights reserved', 'Copyright']
        page_text = str(soup)
        return 1 if any(phrase in page_text for phrase in copyright_phrases) else 0

    @staticmethod
    def count_images(soup):
        return len(soup.select("img"))

    @staticmethod
    def count_js(soup):
        return len(soup.select("script"))

    @staticmethod
    def count_self_ref(parsed_url, soup):
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
        anchor_tags = soup.find_all(href=True)
        return sum(1 for tag in anchor_tags if urlparse(tag['href']).netloc == parsed_url.netloc or (not urlparse(tag['href']).netloc and tag['href'].startswith('/')))

    @staticmethod
    def has_submit_button(soup):
        return 1 if soup.find('button', attrs={'type': 'submit'}) or soup.find('input', attrs={'type': 'submit'}) else 0

    @staticmethod
    def is_responsive(soup):
        return 1 if '@media' in str(soup) else 0
