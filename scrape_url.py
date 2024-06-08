# Import necessary packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests
from tld import get_tld
import difflib

#Fetch a website URL and store it to webpage
def fetchURL(url):
  webpage = requests.get(url)
  #Take the webpage variable and fetch the content using BeautifulSoup
  return BeautifulSoup(webpage.content, "html.parser")

  # Get Domain
def getDomain(ParsedURL):
  return ParsedURL.hostname

  # Count Number of Special Characters in URL
def countSpecial(specialURL):
  count_special = sum(not x.isalnum() for x in specialURL)
  return count_special

  #Check if URL is HTTPS
def checkHTTPS(ParsedURL):
  if ParsedURL.scheme == "https":
      return 1
  return 0

  # Check Lines of Code
def numLinesOfCode(soup):
  number_of_lines = soup.find_all()
  return len(number_of_lines)

  #Check Domain vs Title

# Function to calculate the similarity percentage
def similarity(a, b):
    return difflib.SequenceMatcher(None, a, b).ratio() * 100

def domainTitleMatchScore(specialURL, ParsedURL):
  # Extract the domain from the URL
  domain = ParsedURL.netloc if ParsedURL.netloc else ''

  # Extract the metadata title
  title_tag = soup.find('title')
  title = title_tag.string if title_tag else ''

  # Calculate the similarity percentage
  return similarity(specialURL, title)

# Find description
def checkDescription(soup):
  meta_description = soup.find('meta', attrs={'name': 'description'})

  # Check description
  if meta_description:
      return 1
  return 0

#Check for social network
def checkSocials(soup):
  # List of social media domains to check for
  social_media_domains = [
      'twitter.com',
      'facebook.com',
      'instagram.com',
      'linkedin.com',
      'youtube.com',
      'pinterest.com',
      'tiktok.com'
  ]

  # Find all anchor tags
  anchor_tags = soup.find_all('a', href=True)

  # Check for social media links
  social_media_links = False

  for tag in anchor_tags:
      href = tag['href']
      if any(domain in href for domain in social_media_domains):
          return 1

  return 0

#Check for copyright info
def checkCopyright(soup):
  # Define common copyright-related phrases
  copyright_phrases = [
      '©', '©', 'All rights reserved', 'Copyright'
  ]

  # Search for copyright information
  page_text = soup.get_text()

  # Check if any copyright phrases are in the page text
  has_copyright_info = any(phrase in page_text for phrase in copyright_phrases)

  if has_copyright_info:
      return 1
  return 0

# Number of Images
def countImages(soup):
  imgTags = soup.select("img")

  # Print number of <img> tags retrieved
  return len(imgTags)

#Number of JS lines

def countJS(soup):
  # Find all <script> tags
  script_tags = soup.select("script")

  return len(script_tags)

# Number of self-references
def countSelfRef(ParsedURL, soup):
  base_url = f"{ParsedURL.scheme}://{ParsedURL.netloc}"

  # Initialize a counter for the number of self-referencing links
  self_referencing_links_count = 0

  # Find all tags with href attributes
  anchor_tags = soup.find_all(href=True)

  # Loop through all anchor tags and check for self-referencing links
  for tag in anchor_tags:
      href = tag['href']
      # Normalize the href to handle relative URLs
      full_url = urlparse(href, scheme=ParsedURL.scheme, allow_fragments=True)
      # Check if the href is a self-referencing link
      if full_url.netloc == ParsedURL.netloc or (not full_url.netloc and href.startswith('/')):
          self_referencing_links_count += 1

  return self_referencing_links_count

class Data:
  def __init__(dataList):
    Data.url = dataList[0]
    Data.domain = dataList[1]
    Data.specialCharacterCount = dataList[2]
    Data.isHTTPS = dataList[3]
    Data.numOfCodeLines = dataList[4]
    Data.domainTitleMatchScore = dataList[5]
    Data.hasDescription = dataList[6]
    Data.hasSocial = dataList[7]
    Data.hasCopyright = dataList[8]
    Data.countImage = dataList[9]
    Data.countJS = dataList[10]
    Data.countSelfRef = dataList[11]


def fetchURL(url="https://www.southbankmosaics.com"):
  try:
    values = [None] * 12

    values[0] = url

    ParsedURL = urlparse(url)

    specialURL = url
    specialURL = specialURL.replace(get_tld(url), "")
    specialURL = specialURL.replace("www.", "")
    specialURL = specialURL.replace(ParsedURL.scheme + "://", "")

    soup = fetchURL(url)

    #Replace Domain
    values[1] = getDomain(ParsedURL)

    #Replace Special Character Count
    values[2] = countSpecial(specialURL)

    #Check HTTPS
    values[3] = checkHTTPS(ParsedURL)

    #Find Number of Lines of Code
    values[4] = numLinesOfCode(soup)

    #DomainTitleMatchScore
    values[5] = domainTitleMatchScore(specialURL, ParsedURL)

    #Check Description
    values[6] = checkDescription(soup)

    #Check for Social Network
    values[7] = checkSocials(soup)

    #Check for Copyright Info
    values[8] = checkCopyright(soup)

    #Find Number of Images
    values[9] = countImages(soup)

    # Find Number of JS Lines
    values[10] = countJS(soup)

    # Find Number of Self References
    values[11] = countSelfRef(ParsedURL, soup)

    return Data(values)
  except Exception as e:
    return []