from pathlib import Path
from bs4 import BeautifulSoup as bs4
import time


def testParseWebpageContent(url, data):
    # Check if website folder exists
    if not Path("websites").exists():
        Path("websites").mkdir()
    
    # get number of files in websites folder
    num_files = len([f for f in Path("websites").iterdir() if f.is_file()])

    soup = bs4(data, 'html.parser')
    pageTitle = soup.title.string
    pageText = soup.get_text().replace("\n","").strip()
    pageUrl = url
    currentDateEpoch = int(time.time())

    outString = f"""\n
    {"#"*50}\n
    URL: {pageUrl}\n
    Title: {pageTitle}\n
    PageContent: {pageText}\n
    Date: {currentDateEpoch}\n
    {"#"*50}\n\n
    """
    # Saves data to file
    try:
        with open(f"websites/pages.html", "a+", encoding="utf-8") as f:
            f.write(outString)
    except Exception as exc:
        print("Error saving file")
        print('%r generated an exception: %s' % (url, exc))
        

    
