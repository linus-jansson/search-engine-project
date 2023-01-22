import Link from 'next/link';

export default function NoResults({ query }: { query: string }) {

    return (
        <div className='flex flex-col w-96'>
            <h1 className="text-3xl font-bold mb-3">No results found for &quot;{query}&quot;</h1>
            <p>Would you like to search using <span className='font-bold'>DuckDuckGo</span> instead?</p>
            <div className='mt-2'>
                <Link href={`https://duckduckgo.com/?q=${query}`} className="font-bold border p-1 rounded-lg border-white text-lg duration-100 hover:bg-zinc-500 hover:text-zinc-900">Search</Link>
            </div>
        </div>
    )

}