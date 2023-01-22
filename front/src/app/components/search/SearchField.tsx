"use client"
import { useRouter } from "next/navigation";

export default function SearchField({ currentQuery }: { currentQuery: string | undefined }) {
    const router = useRouter();

    function handleSearch(e: React.KeyboardEvent<HTMLInputElement>) {
        if (e.key !== "Enter") return;
        let inputFieldValue = (e.target as HTMLInputElement).value;

        if (inputFieldValue.length === 0) return;

        router.push(`/search?q=${encodeURIComponent(inputFieldValue)}`);
        // console.log(inputFieldValue)
    }


    return (
        <input
            type="text"
            className="border-2 shadow-lg w-96 h-12 focus:outline-none p-2 text-lg bg-zinc-700 rounded-xl"
            onKeyDown={handleSearch}
            placeholder="Search..."
            defaultValue={currentQuery || ""}
        />
    )
}