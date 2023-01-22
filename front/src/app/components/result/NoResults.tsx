import Link from 'next/link';

export default function NoResults({ query }: { query: string }) {

    return (
        <div className='flex flex-col'>
            <h1 className="text-3xl font-bold mb-3">No results found</h1>
            <p>Would you like to search using <span className='font-bold'>DuckDuckGo</span> instead?</p>
            <div className='m-2'>
                <Link href={`https://duckduckgo.com/?q=${query}`} className="font-bold border p-1 rounded-lg border-white text-lg duration-100 hover:bg-neutral-500">Search</Link>
            </div>
        </div>
    )

}