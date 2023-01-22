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
    */

    let data = {
        title: 'Hello World',
        summary: 'This is a summary',
        url: 'https://www.google.com',
        date: new Date()
    }

    let output = []

    for (let i = 0; i < 10; i++) output.push(data);

    res.status(200).json(output)
}
