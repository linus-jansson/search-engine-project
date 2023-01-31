import sqlite3

conn = sqlite3.connect(':memory:')
conn.execute(
    """create virtual table fts5test using fts5(data, tokenize="trigram");""")
conn.execute("""insert into fts5test (data) 
                values ('this is a test of full-text search');""")
cursor = conn.cursor()
test = cursor.execute(
    """select * from fts5test where data like '%te%';""").fetchall()
print(test)
test = cursor.execute(
    """select highlight(data, 2, '<b>', '</b>') from fts5test where data like '%te%';""").fetchall()
print(test)
