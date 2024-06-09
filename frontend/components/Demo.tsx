"use client"

import { useEffect, useState } from 'react'
import Form from './Form'

const Demo = () => {

    const [response, setResponse] = useState<any>(null)

    const handleSubmit = (url: string) => {
        setResponse(null)
        fetch("http://127.0.0.1:8000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ url }),
        })
        .then((res) => res.json())
        .then((data) => setResponse(data))
        .catch((err) => console.error(err))
    }

    return (
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

            <Form _onSubmit={handleSubmit} />

            {/* Display the response here */}
            {response && (
                <div
                    className="flex flex-col gap-1"
                >
                    <h3
                        className="text-lg font-bold"
                    >Result</h3>

                    { response.prediction !== undefined && response.prediction !== null && <p className={response.prediction ? "text-red-500 text-lg" : "text-green-700 text-lg"}>
                        { response.prediction ? "Oh no! Phishing Website Detected!" : "You are safe!" }
                    </p> }

                    { response.error && <p className="text-red-500 text-lg">
                        { response.error }
                    </p> }
                </div>
            )}
        </section>
    )
}

export default Demo