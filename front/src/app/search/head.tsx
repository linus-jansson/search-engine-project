export default function Head({ searchParams }: { [key: string]: string | string[] | undefined }) {
    // TODO: Add search query to title
    // https://github.com/vercel/next.js/pull/43305
    return (
        <>
            {/* SVG as favicon */}
            <link rel="shortcut icon" href="/favicon.svg" type="image/x-icon" />
            <title>This is being worked on by nextjs team</title>
        </>
    );
}
