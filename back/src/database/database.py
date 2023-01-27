import sqlite3
from pathlib import Path


class Database():
    def __init__(self):
        # ...
        self.connection = sqlite3.connect('database.db')
        # Getting the SQLite version and printing it to console
        with self.connection as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT SQLITE_VERSION()')
            data = cursor.fetchone()
            print('SQLite version:', data)

        self.initTables()
        # ...

    def initTables(self):
        # ...
        schemaPath = Path(__file__).parent.absolute()/Path('db_schema.sql')

        # If database empty initialize tables
        self.connection.isolation_level = None
        cursor = self.connection.cursor()
        cursor.execute("BEGIN")
        try:
            # Parse db_schema.sql
            with open(schemaPath, 'r') as f:
                currentQuery = ""
                for lines in f.readlines():
                    currentQuery += lines
                    if lines.endswith(";\n"):
                        cursor.execute(currentQuery)
                        currentQuery = ""

            cursor.execute("COMMIT")
        except Exception as exc:
            self.connection.execute("ROLLBACK")
            raise Exception(
                "Error: Unable to parse db_schema.sql (rolling back): %s" % exc.message)

    def addURL(self, url):
        # ...
        self.connection.execute(
            "INSERT INTO urls (url, date) VALUES (?, ?)", (url, self.currentDateEpoch))
        self.connection.commit()
        # ...

    def addPage(self, url, page):


if __name__ == "__main__":
    db = Database()
