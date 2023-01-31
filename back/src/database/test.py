import sqlite3
from pathlib import Path
import time

with sqlite3.connect("test.db") as conn:
    print("creating table")
    conn.execute(
        """create virtual table if not exists fts5test using fts5(data, tokenize="trigram");""")
    p = Path(__file__).parent.absolute()/Path("sample-text-data/")

    print("Inserting data")
    for file in p.iterdir():
        with file.open() as f:
            current = f.read()
            for i in range(100):
                conn.execute(
                    """insert into fts5test (data) values (?);""", (current,))

    print("Data inserted")
    print("Searching for 'Lorem ipsum dolor sit amet'")
    cursor = conn.cursor()
    start = time.time()
    test = cursor.execute(
        """SELECT HIGHLIGHT(fts5test, 0, '<b style="color:red;">', '</b>') FROM fts5test WHERE data MATCH 'Lorem ipsum dolor sit amet';""").fetchall()
    end = time.time()
    print("Writing to file")
    with open("test.html", "w") as f:
        f.flush()
        for t in test:
            f.write(str(end-start) + "seconds: " + t[0])

# conn.execute(
#     """create virtual table fts5test using fts5(data, tokenize="trigram");""")
# conn.execute("""insert into fts5test (data)
#                 values ('this is a test of full-text search');""")
# cursor = conn.cursor()
# test = cursor.execute(
#     """SELECT * FROM fts5test WHERE data MATCH 'ull';""").fetchall()
# print(test)
# test = cursor.execute(
#     """SELECT HIGHLIGHT(fts5test, 0, '<b>', '</b>') FROM fts5test WHERE data LIKE '%te%';""").fetchall()
# print(test)
