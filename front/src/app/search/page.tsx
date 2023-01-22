
import NoResults from '../components/result/NoResults';
import ResultCard from '../components/result/ResultCard';
import SearchField from '../components/search/SearchField';

export const revalidate = 300; // revalidate this page every 5 minutes

async function GetSearchResults(query: string) { // leave it as any for now
    const apiResponse = await fetch(`http://localhost:3000/api/search?q=${query}`, { cache: 'default' })
    return apiResponse.json();
}

export default async function SearchPage({ searchParams }: { [key: string]: string | string[] | undefined }) {
    let searchQuery = searchParams.q;
    const searchResults = await GetSearchResults(searchQuery);
    return (
        <div>
            <div id="top-bar" className='w-screen shadow-3xl bg-neutral-900 flex flex-col p-4 items-center md:flex-row'>
                <h1 className="text-3xl font-bold mr-6">Search stuff</h1>
                <SearchField currentQuery={searchQuery} />
            </div>
            <div id="search-results" className='ml-4 mt-4'>
                {/* TODO: In future if no results show no results found */}
                {/* {searchResults.length === 0 && <NoResults query={searchQuery} />} */}
                <NoResults query={searchQuery} />
                {searchResults && searchResults.map((data: unknown, idx: number) => <ResultCard key={idx} {...data} />)}
            </div>
        </div>
    )
}
