"use client"
import { useRouter } from "next/navigation";
import { useRef } from "react";

export default function SearchField({ currentQuery }: { currentQuery: string | undefined }) {
    const searchRef = useRef<HTMLInputElement>(null);
    const router = useRouter();


    function handleClick(e: React.MouseEvent<HTMLButtonElement>) {
        if (!searchRef.current) return;
        pushRouter(searchRef.current!.value);
    }
    function handleEnter(e: React.KeyboardEvent<HTMLInputElement>) {
        if (!searchRef.current) return;
        if (e.key === "Enter") {
            pushRouter(searchRef.current!.value);
        }
    }

    function pushRouter(query: string) {
        if (query.length === 0) return;
        router.push(`/search?q=${encodeURIComponent(query)}`);
    }


    return (
        <div className="flex duration-200 shadow-lg hover:shadow-2xl">
            <input
                type="text"
                className="h-12 p-2 text-lg duration-100 rounded-l-lg outline-none w-96 bg-zinc-700"
                onKeyDown={handleEnter}
                placeholder="Search..."
                ref={searchRef}
                defaultValue={currentQuery || ""}
            />
            <button className="rounded-r-lg outline-none w-fit bg-zinc-700" onClick={handleClick}>
                {/* Tablericons */}
                <svg xmlns="http://www.w3.org/2000/svg"
                    width="32" height="32"
                    viewBox="0 0 24 24"
                    strokeWidth="1.5"
                    stroke="#e4e4e7"
                    fill="none"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                >
                    <path stroke="none" d="M0 0h24v24H0z" fill="none" />
                    <circle cx="10" cy="10" r="7" />
                    <line x1="21" y1="21" x2="15" y2="15" />
                </svg>
            </button>

        </div>
    )
}