import NoResults from './NoResults';
import ResultCard from './ResultCard';
import ShowMore from './ShowMore';

export const revalidate = 300; // revalidate this page every 5 minutes

async function GetSearchResults(query: string) { // leave it as any for now
    const apiResponse = await fetch(`http://localhost:3000/api/search?q=${query}`, { cache: 'default' })
    return apiResponse.json();
}

export default async function SearchResults({ query }: { query: string }) {

    const searchResults = await GetSearchResults(query);

    function addToResults(dataList: Array<any>) { // any for now

    }

    return (
        <div id="search-results" className='ml-4 mt-4'>
            {/* TODO: In future if no results show no results found */}
            {/* {searchResults.length === 0 && <NoResults query={searchQuery} />} */}
            {searchResults && <span>Found {searchResults.length} results</span>}
            <NoResults query={query} />
            {searchResults && searchResults.map((data: unknown, idx: number) => <ResultCard key={idx} {...data} />)}
            {/* TODO: add pagnition for large amounts of results */}
            <ShowMore query={query} />
        </div>
    )
}