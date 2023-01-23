// Next.js API route support: https://nextjs.org/docs/api-routes/introduction
import type { NextApiRequest, NextApiResponse } from 'next'

type ReturnData = {
    title: string,
    summary: string,
    url: string,
    date?: Date,
}

export default function handler(
    req: NextApiRequest,
    res: NextApiResponse<Array<ReturnData>>
) {
    /*
        Todo: 
            This will in the future call the external API that gets the data from the database

            Should only return some amount of links at the time, and send more when client asks for it
        output:
            First Batch of links
            amount of pages
    */

    let query = req.query.q // query from the search bar
    let min = req.query.min // min link index
    let max = req.query.max // max link index


    /* predefined data to test api */
    let data = {
        title: 'Hello World',
        summary: 'This is a summary Lorem ipsum dolor sit amet, consectetur adipisicing elit. Culpa porro expedita qui dolorem pariatur maxime iste atque dolore nam ad',
        url: 'https://www.google.com',
        date: new Date() // Date page was added to database / last updated
    }

    let output = []

    for (let i = 0; i < 50; i++) output.push(data);
    /**/

    res.status(200).json(output)
}
