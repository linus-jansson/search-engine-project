
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
                <div id="top-bar">

                </div>
                <div id="search-results">
                    {searchResults.map((data: unknown, idx: number) => <p>result {idx}: {data.title}</p>)}
                </div>
            </div>
        </>
    )
}
