import sqlite3
from pathlib import Path


class Database():
    def __init__(self):
        # ...
        self.connection = sqlite3.connect('database.db')
        # Getting the SQLite version and printing it to console
        with self.connection.cursor() as cursor:
            cursor.execute('SELECT SQLITE_VERSION()')
            data = cursor.fetchone()
            print('SQLite version:', data)

        self.initTables()

    def initTables(self):
        # If database empty initialize tables
        schemaPath = Path(__file__).parent.absolute()/'db_schema.sql'
        with schemaPath.open() as f:
            with self.connection.cursor() as cursor:
                cursor.executescript( f.read() );

    def executeQueries(self, queries: list[list[str, str]] = None):
        """
        Executes a list of queries with optional parameters
        :param queries: List of queries to execute [[query, parameters], [query, parameters], ...]
        """
        self.connection.isolation_level = None
        with self.connection.cursor() as cursor:
            cursor.execute("BEGIN")
            try:
                # Todo: if a tuple of query, parameter is passed execute it and commit
                for querySet in queries:
                    query = querySet[0]
                    if len(querySet) > 1:
                        parameters = querySet[1]
                        cursor.execute(query, parameters)
                    else:
                        cursor.execute(query)

                cursor.execute("COMMIT")
            except Exception as exc:
                self.connection.execute("ROLLBACK")
                raise Exception(
                    "Error: Unable to execute queries (rolling back): %s" % exc.message)

    @property
    def last_insert_id(self):
        result = self.connection.execute(
            "SELECT last_insert_rowid()").fetchone()
        if result:
            return result[0]
        return None

    def addURL(self, url):
        pass

    def addPage(self, url, page):
        """Example code"""
        query = "INSERT INTO pages (url, title, ogTitle, ogType, ogImage, ogUrl, ogDescription, ogLocale, praseDate) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        parameters = (url, page.title, page.ogTitle, page.ogType, page.ogImage,
                      page.ogUrl, page.ogDescription, page.ogLocale, page.praseDate)

        self.executeQueries([[query, parameters]])
        page_id = self.last_insert_id

        self.addWords(page_id, page.words)

        """"""

    def addWords(self, page_id: int, words: list):
        cursor = self.connection.cursor()
        cursor.executemany("INSERT OR IGNORE INTO words_pages(word_id,page_id) VALUES((INSERT OR IGNORE INTO words(word) VALUES(?) RETURNING id),?)",
                           [(word,page_id) for word in words])


    def search(self, query: str):
        # https://www.sqlite.org/fts5.html#the_experimental_trigram_tokenizer
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM pages WHERE title LIKE ?", (query, ))
        return cursor.fetchall()

if __name__ == "__main__":
    db = Database()
