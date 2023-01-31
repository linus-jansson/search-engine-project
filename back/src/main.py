
import sys
from fastapi import FastAPI, Request
from pydantic import BaseModel, create_model

# Running app: uvicorn main:app --reload
app = FastAPI()


@app.post('/api/search')
def search():
    # Match the search term to the database
    # Handle Results
    # If results older than 30 days; re-scrape url?
    pass


@app.get('/api/URL/')
def testGetPage(q: str = None):
    import crawler as scraper
    # get url from body from request
    url = q
    if url is None:
        return {'error': 'No URL provided'}

    url_list = url.split(',')
    output_data = []
    for url, data in scraper.scrapeURLS(url_list, 60, 20):
        new_page = scraper.Page(url, data)
        output_data.append(new_page.pageObject)

    return output_data


@app.post('/api/URL/save')
def savePage():
    # Get URL/s from body of request
    # Parse URL/s
    # Save to database
    pass


@app.delete('/api/URL/delete')
def removePage():
    # Get URL/s from body of request
    # Delete from database
    pass


if __name__ == '__main__':
    shouldRunDebug = "debug" in sys.argv
    app.run(debug=shouldRunDebug)
