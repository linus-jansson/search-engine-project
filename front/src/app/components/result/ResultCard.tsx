import Link from 'next/link';
import DeleteLink from './DeleteLink';

export default function SearchResultCard(props: any) {
    function formatDate(date: string) {
        let dateObj = new Date(date);
        return dateObj.toLocaleDateString();
    }

    return (
        <>
            <div className="mb-6 w-96">
                <div id="title">
                    <Link href={props.url} className="text-2xl">{props.title}</Link>
                </div>
                <div id="desc" >
                    <span className='mr-2 text-zinc-400'>{formatDate(props.date)}</span>
                    <span className='text-zinc-300'>{props.summary}</span>
                </div>
                {/* <DeleteLink link={props.url} /> */}
            </div>
        </>
    )
};