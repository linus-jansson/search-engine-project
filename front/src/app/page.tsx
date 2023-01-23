import SearchField from "./components/search/SearchField";

export default function Home() {
    return (
        <>
            <div className="grid place-content-center h-screen text-center">
                <h1 className="text-3xl font-bold mb-3">Search stuff</h1>
                <SearchField currentQuery={undefined} />
            </div >
        </>
    )
}
