# Example code from Python docs.
# https://docs.python.org/3/library/concurrent.futures.html#threadpoolexecutor-example

import concurrent.futures
import urllib.request

import _parser as parser
from fake_useragent import UserAgent

from TestUrls import URLS

# Retrieve a single page and report the URL and contents
def load_url(url, timeout):
    ua = UserAgent() # From here we generate a random user agent
    request = urllib.request.Request(
        url,
        data=None,
        headers={
            'User-Agent': ua.random,
        }
    )

    with urllib.request.urlopen(request, timeout=timeout) as conn:
        return conn.read()

def scrapeURLS(listOfUrls: list, timeout=60, maxWorkers=10) :
    URLerrors = 0

    # We can use a with statement to ensure threads are cleaned up promptly
    with concurrent.futures.ThreadPoolExecutor(max_workers=maxWorkers) as executor:
        # Start the load operations and mark each future with its URL
        future_to_url = {
            executor.submit(load_url, url, timeout): url for url in listOfUrls
        }
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
                parser.testParseWebpageContent(url, data) ## saves data to file
                yield url, future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (url, exc))
                URLerrors += 1
            else:
                print('%r page is %d bytes' % (url, len(data)))

        print(f"URLs tested: {len(URLS)} URL errors: {str(URLerrors)}/{len(URLS)}")



def main():
    pages = []
    for url, data in scrapeURLS(URLS, 60, 20):
        page = parser.Page(url, data)
        print("adding ", page.pageTitle)
        pages.append(page)
    
    print(f"Pages scraped successfully: {len(pages)}")
        

if __name__ == "__main__":
    main()