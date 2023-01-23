import Link from 'next/link';

import SearchField from '../components/search/SearchField';
import SearchResults from '../components/result/SearchResults';

export default function SearchPage({ searchParams }: { [key: string]: string | string[] | undefined }) {
    if (searchParams === undefined || !searchParams.hasOwnProperty("q")) return <div>Search params are undefined</div>;
    let searchQuery = searchParams["q" as any];

    return (
        <div>
            <div id="top-bar" className='flex flex-col items-center w-screen p-4 shadow-3xl bg-neutral-900 md:flex-row'>
                <Link href='/' className="mr-6 text-3xl font-bold">Search stuff</Link>
                <SearchField currentQuery={searchQuery} />
            </div>

            {/* https://github.com/vercel/next.js/issues/42292 */}
            {/* @ts-expect-error Server Component */}
            <SearchResults query={searchQuery} />
        </div>
    )
}
