"use client"

import { FC, FormEvent } from "react"

const Form: FC = () => {
    return (
    <form
    name="demo-form"
    className="flex flex-col gap-4 justify-center items-center"
    onSubmit={(e: FormEvent<HTMLFormElement>) => {
        e.preventDefault()
        const url = e.currentTarget["url-input"].value
        console.log(url)
    }}
    >
        <input 
            name="url-input"
            type="text" 
            placeholder="Enter URL" 
            className="w-full border-2 border-gray-200 p-2 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
        />
        <button
            className="bg-blue-500 text-white py-2 px-4 rounded-md hover:bg-blue-700 transition-colors duration-200 ease-in-out"
            type="submit"
        >Detect Phishing Website</button>
    </form>
    )
}

export default Form