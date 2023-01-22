
import NoResults from '../components/result/NoResults';
import ResultCard from '../components/result/ResultCard';
import SearchField from '../components/search/SearchField';

async function GetSearchResults(params: any) { // leave it as any for now

    let searchQuery = params.query;

    const apiResponse = await fetch('http://localhost:3000/api/search', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            query: searchQuery,
        }),
    })
    return apiResponse.json();
}

export default async function SearchPage({ searchParams }: { [key: string]: string | string[] | undefined }) {
    const searchResults = await GetSearchResults(searchParams);
    console.log(searchResults);
    return (
        <>
            <div>
                <div id="top-bar" className='w-screen shadow-3xl bg-neutral-800 flex flex-row p-4 items-center'>
                    <h1 className="text-3xl font-bold mr-6">Search stuff</h1>
                    <SearchField />

                </div>
                <div id="search-results" className='ml-4 mt-4'>
                    <NoResults query={searchParams.query} />
                    {searchResults.map((data: unknown, idx: number) => <ResultCard key={idx} {...data} />)}
                </div>
            </div>
        </>
    )
}
