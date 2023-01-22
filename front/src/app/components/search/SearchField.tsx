"use client"
import { useRouter } from "next/navigation";
export default function SearchField() {
    const router = useRouter();

    function handleSearch(e: React.KeyboardEvent<HTMLInputElement>) {
        if (e.key !== "Enter") return;
        let inputFieldValue = (e.target as HTMLInputElement).value;

        if (inputFieldValue.length === 0) return;

        router.push(`/search?query=${encodeURIComponent(inputFieldValue)}`);
        console.log(inputFieldValue)
    }


    return (
        <input type="text" onKeyDown={handleSearch} className="border-2 shadow-lg w-96 h-12 focus:outline-none p-2 text-lg bg-neutral-600 rounded-xl" />
    )
}