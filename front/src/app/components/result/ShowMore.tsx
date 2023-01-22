"use client"

import { useState } from "react"

export default function ShowMore(props: any) {
    const [pageNumber, setPageNumber] = useState(1)
    function handleShowMoreInteraction() {
        setPageNumber(prev => prev + 1);
        console.log("Showing more for" + props.query + " on page " + pageNumber)
    }
    /* Every "page" shows a number of items every time button is pressed fetch more data from api and pass it to searchResult in parent component */
    return (
        <div>
            <button onClick={handleShowMoreInteraction}>Show more</button>
        </div>
    )
}