from pathlib import Path
from bs4 import BeautifulSoup as bs4
import time

class Page:
    def __init__(self, url, data):
        soupData = bs4(data, 'html.parser')
        self.url = url
        self.__data = data
        self.pageTitle = soupData.title.string
        self.pageText = soupData.get_text().replace("\n","").strip()
        self.currentDateEpoch = int(time.time())
    
    def __str__(self):
        return f"{'#'*50}\nURL: {self.url}\nTitle: {self.pageTitle}\nPageContent: {self.pageText}\nDate: {self.currentDateEpoch}\n{'#'*50}\n\n"
    
    @property
    def pageObject(self):
        return {
            "url": self.url,
            "title": self.pageTitle,
            "content": self.pageText,
            "praseDate": self.currentDateEpoch
        }
    

def testParseWebpageContent(url, data):
    # Check if website folder exists
    if not Path("websites").exists():
        Path("websites").mkdir()
    
    # get number of files in websites folder
    num_files = len([f for f in Path("websites").iterdir() if f.is_file()])

    newPage = Page(url, data)
    # Saves data to file
    try:
        with open(f"websites/pages.html", "a+", encoding="utf-8") as f:
            f.write(newPage.__str__())
    except Exception as exc:
        print("Error saving file")
        print('%r generated an exception: %s' % (url, exc))
        

    
