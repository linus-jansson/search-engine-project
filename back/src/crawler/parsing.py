from pathlib import Path
from bs4 import BeautifulSoup as bs4
import time
import re


class OpenGraph:
    def __init__(self, html):
        self.document = bs4(html, 'html.parser')

    def usesOpenGraph(self):
        """Check if page uses Open Graph
        TODO: check if correct regex before using method
        """
        print("WARNING: usesOpenGraph() is not tested yet")
        if self.document.findAll("meta", property=re.compile("^og:.*$")):
            return True
        return False

    @property
    def url(self):
        """Return the Open Graph site name
        """

        if self.document.findAll("meta", property="og:url"):
            return self.document.find("meta", property="og:url")["content"]

        return None

    @property
    def image(self):
        """Return the Open Graph site name """

        if self.document.findAll("meta", property="og:image"):
            return self.document.find("meta", property="og:image")["content"]

        return None

    @property
    def site_name(self):
        """Return the Open Graph site name"""

        if self.document.findAll("meta", property="og:site_name"):
            return self.document.find("meta", property="og:site_name")["content"]
        return None

    @property
    def description(self):
        """Return the Open Graph description"""

        if self.document.findAll("meta", property="og:description"):
            return self.document.find("meta", property="og:description")["content"]

        return None

    @property
    def locale(self):
        """Return the Open Graph locale
        """

        if self.document.findAll("meta", property="og:locale"):
            return self.document.find("meta", property="og:locale")["content"]

        return None

    @property
    def title(self):
        """Return the Open Graph title
        """

        if self.document.findAll("meta", property="og:title"):
            return self.document.find("meta", property="og:title")["content"]

        return None


class Page:
    url = None
    title = None
    words = []
    currentDateEpoch = int(time.time())

    # Open Graph: https://ogp.me/
    ogTitle = None
    ogType = None
    ogImage = None
    ogUrl = None
    ogDescription = None
    ogLocale = None

    def __init__(self, url, data):
        self.document = bs4(data, 'html.parser')
        self.url = url
        self.__data = data

        try:
            # Check if page has meta tags or opengraph tags
            og = OpenGraph(html=self.__data)
            self.ogTitle = og.title
            # self.ogType = og.type
            self.ogImage = og.image
            self.ogUrl = og.url
            self.ogDescription = og.description
            self.ogLocale = og.locale

            # Get page title
            if self.ogTitle:
                self.title = self.ogTitle
            else:
                if self.document.find("title"):
                    self.title = self.document.find("title").string

            # Get all words using __data spliting it into a list of words
            _pagetext = self.document.get_text()
            self.words = re.sub(r"[^\w]", ' ', _pagetext).split()

            # self.debugSavePageToFile()

        except Exception as exc:
            print('%r in parser.py generated an exception: %s' %
                  (self.url, exc))
            raise exc

    @property
    def pageObject(self):
        return {
            "url": self.url,
            "title": self.title,
            "content": self.words,
            "ogTitle": self.ogTitle,
            "ogType": self.ogType,
            "ogImage": self.ogImage,
            "ogUrl": self.ogUrl,
            "ogDescription": self.ogDescription,
            "ogLocale": self.ogLocale,
            "praseDate": self.currentDateEpoch
        }

    def debugSavePageToFile(self):
        # Check if website folder exists
        if not Path(".websites").exists():
            Path(".websites").mkdir()

        # Saves data to file
        try:
            with open(f".websites/pages.txt", "a+", encoding="utf-8") as f:
                f.write(str(self.pageObject) + "\n")
        except Exception as exc:
            print("Error saving file")
            print('%r generated an exception: %s' % (self.url, exc))
