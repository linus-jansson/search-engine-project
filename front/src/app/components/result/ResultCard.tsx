import Link from 'next/link';

export default function SearchResultCard(props: any) {
    function formatDate(date: string) {
        let dateObj = new Date(date);
        return dateObj.toLocaleDateString();
    }

    return (
        <>
            <div className="w-96 mb-6">
                <div id="title">
                    <Link href={props.url} className="text-2xl">{props.title}</Link>
                </div>
                <div id="desc">
                    <span className='mr-2 text-neutral-400'>{formatDate(props.date)}</span>
                    <span className='text-neutral-300'>{props.summary}</span>
                </div>
            </div>
        </>
    )
};