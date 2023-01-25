"use client"
import { useRef, useEffect } from "react";
export default function ScrollTopButton() {
    const buttonRef = useRef(null);

    let handleSCroll = () => {
        if (!buttonRef.current) return;
        if (typeof window === "undefined") return;

        if (window.scrollY > 100) {
            buttonRef.current.classList.remove("hidden")
        } else {
            buttonRef.current.classList.add("hidden")
        }
    }
    let handleScrollButtonClick = () => {

        if (typeof window === "undefined") return;

        window.scrollTo({
            top: 0,
            behavior: "smooth"
        })
    }

    useEffect(() => {
        if (typeof window === "undefined") return;

        window.addEventListener("scroll", handleSCroll)
        return () => {
            window.removeEventListener("scroll", handleSCroll)
        }

    }, [])

    return (
        <button ref={buttonRef} onClick={handleScrollButtonClick} className="fixed z-10 hidden p-3 bg-gray-300 rounded-full shadow-md bottom-10 right-10 animate-bounce" >
            <svg className="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"
                xmlns="http://www.w3.org/2000/svg">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2.5" d="M5 10l7-7m0 0l7 7m-7-7v18" />
            </svg>
        </button >
    )

}