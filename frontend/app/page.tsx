import Form from "@/components/Form"

export default function Home() {

    return (
        <main className="flex flex-col min-h-[100dvh] px-[1rem] sm:px-[5rem] lg:px-[15rem]">
            <header className="flex flex-row justify-between items-center py-8">
                <h1
                    className="text-2xl font-bold text-gray-800"
                >Phishing Website Detection</h1>
                <nav>
                    <ul className="flex flex-row gap-4 list-none">
                        <li><a href="#abstract">Abstract</a></li>
                        <li><a href="#dataset-features">Dataset & Features</a></li>
                        <li><a href="#demo">Demo</a></li>
                    </ul>
                </nav>
            </header>

            <div className="flex flex-col gap-5 my-auto">
                <section
                id="abstract"
                className="flex flex-col gap-1"
                >
                    <h2
                        className="text-xl font-bold"
                    >Abstract</h2>
                    <p>
                    Phishing is described as a form of online attack/scam where scammers target consumers as a well-known source - an internet service provider, 
                    a bank, or a mortgage company, for example in an email asking the consumer for personal identifying information. With this new-found information, 
                    scammers attempt to access or open new accounts posing as the consumer. An analysis done by a Forbes Advisor on the Federal Bureau of Investigation's 
                    (FBI) Internet Crimes Report found that over 300,000 online users fell victim to phishing attacks with a total loss of $52,089,159 in the U.S. in 2022. 
                    Over 500 million phishing attacks were reported in 2022, with phishing attacks becoming more clever, intricate, and convincing over the years.
                    <br />
                    <br />
                    To prevent consumers from falling victim to these forms of cyber-attacks, we propose to build an application to detect phishing websites using 
                    supervised learning techniques. The application will either take the form of an online web extension (for seamless use) or web application utilizing 
                    web-scraping techniques to collect input for validating the website.
                    </p>
                </section>

                <section
                id="dataset-features"
                className="flex flex-col gap-1"
                >
                    <h2
                        className="text-xl font-bold"
                    >Dataset & Features</h2>
                    <p>
                        The dataset used for this project is available on Kaggle:{" "}
                        <a
                        className="text-blue-500 hover:text-blue-700 transition-colors duration-200 ease-in-out"
                        href="https://www.kaggle.com/datasets/prishasawhney/phishing-url-website-dataset-cleaned" 
                        target="_blank" 
                        rel="noopener noreferrer">Phishing URL Website Dataset (Cleaned)</a>
                        <br /><br />
                        The dataset contains numerous relevant features (15+) for detecting phishing websites such as URL and HTML markers, HTTP protocols, and images/scripts. The original UCI dataset has been cleaned using outlier removal and feature selection techniques.
                        <br /><br />
                        Some of the relevant features in the dataset include:
                    </p>
                    <ul
                        className="list-disc list-inside pl-4"
                    >
                        <li>URL and HTML markers</li>
                        <li>HTTP protocols</li>
                        <li>Images and scripts</li>
                        {/* Add more features here */}
                    </ul>
                </section>

                <section
                id="demo"
                className="flex flex-col gap-1"
                >
                    <h2
                        className="text-xl font-bold"
                    >Demo</h2>
                    <p>
                        When entering a URL please ensure the URL is in the following format: <code>http://www.example.com</code> or <code>https://www.example.com</code>.
                    </p>

                    <Form />
                </section>
            </div>

            <footer
                className="py-8 border-t-2 border-gray-200 mt-auto"
            >
                <p
                    className="text-center"
                >&copy; 2024 Phishing Website Detection</p>
            </footer>
        </main>
    )
}
