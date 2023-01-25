from pathlib import Path
from bs4 import BeautifulSoup as bs4
import time
import re

class OpenGraph(dict):
    """
    """

    required_attrs = ['title', 'type', 'image', 'url', 'description']

    def __init__(self, html=None, scrape=False, **kwargs):
        # If scrape == True, then will try to fetch missing attribtues
        # from the page's body

        self.scrape = scrape

        for k in kwargs.keys():
            self[k] = kwargs[k]

        dict.__init__(self)

        if html is not None:
            self.parser(html)

    def __setattr__(self, name, val):
        self[name] = val

    def __getattr__(self, name):
        return self[name]

    def parser(self, html):
        """
        """
        if not isinstance(html,bs4):
            doc = bs4(html)
        else:
            doc = html
        ogs = doc.html.head.findAll(property=re.compile(r'^og'))
        for og in ogs:
            if og.has_attr(u'content'):
                self[og[u'property'][3:]]=og[u'content']
        # Couldn't fetch all attrs from og tags, try scraping body
        if not self.is_valid() and self.scrape:
            for attr in self.required_attrs:
                if not self.valid_attr(attr):
                    try:
                        self[attr] = getattr(self, 'scrape_%s' % attr)(doc)
                    except AttributeError:
                        pass

    def valid_attr(self, attr):
        return self.get(attr) and len(self[attr]) > 0

    def is_valid(self):
        return all([self.valid_attr(attr) for attr in self.required_attrs])

    def to_html(self):
        if not self.is_valid():
            return u"<meta property=\"og:error\" content=\"og metadata is not valid\" />"

        meta = u""
        for key,value in self.iteritems():
            meta += u"\n<meta property=\"og:%s\" content=\"%s\" />" %(key, value)
        meta += u"\n"

        return meta

    def scrape_image(self, doc):
        images = [dict(img.attrs)['src']
            for img in doc.html.body.findAll('img')]

        if images:
            return images[0]

        return u''

    def scrape_title(self, doc):
        return doc.html.head.title.text

    def scrape_type(self, doc):
        return 'other'

    def scrape_description(self, doc):
        tag = doc.html.head.findAll('meta', attrs={"name":"description"})
        result = "".join([t['content'] for t in tag])
        return result

class Page:
    url = None
    pageTitle = None
    pageText = None
    pageType = None
    currentDateEpoch = None

    def __init__(self, url, data):
        soupData = bs4(data, 'html.parser')
        self.url = url
        self.__data = data

        og = OpenGraph(html=self.__data)
        if og.is_valid():
            self.pageTitle = og.title
            self.pageText = og.description
            self.pageType = og.type
        else:
            self.pageTitle = soupData.title.string
            self.pageText = soupData.get_text().replace("\n","").strip()

        self.currentDateEpoch = int(time.time())

    def usesOpenGraph(self) -> bool:
        pass

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
    
    def debugSavePageToFile(self):
        pass
        # Check if website folder exists
        if not Path(".websites").exists():
            Path(".websites").mkdir()

        # Saves data to file
        try:
            with open(f".websites/pages.html", "a+", encoding="utf-8") as f:
                f.write(self.__str__())
        except Exception as exc:
            print("Error saving file")
            print('%r generated an exception: %s' % (self.url, exc))

