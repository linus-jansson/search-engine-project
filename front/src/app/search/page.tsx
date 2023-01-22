import Link from 'next/link';

import SearchField from '../components/search/SearchField';
import SearchResults from '../components/result/SearchResults';

export default function SearchPage({ searchParams }: { [key: string]: string | string[] | undefined }) {
    if (searchParams === undefined || !searchParams.hasOwnProperty("q")) return <div>Search params are undefined</div>;
    let searchQuery = searchParams["q" as any];

    return (
        <div>
            <div id="top-bar" className='w-screen shadow-3xl bg-neutral-900 flex flex-col p-4 items-center md:flex-row'>
                <Link href='/' className="text-3xl font-bold mr-6">Search stuff</Link>
                <SearchField currentQuery={searchQuery} />
            </div>

            {/* https://github.com/vercel/next.js/issues/42292 */}
            {/* @ts-expect-error Server Component */}
            <SearchResults query={searchQuery} />
        </div>
    )
}
