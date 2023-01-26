-- Add Open Graph data if exist
CREATE TABLE IF NOT EXISTS pages (
  url TEXT NOT NULL PRIMARY KEY,
  title TEXT NOT NULL, -- title of page
  fetch_time TIMESTAMP NOT NULL -- Date page was last indexed
);

CREATE TABLE IF NOT EXISTS wordsInTable {
    id INT NOT NULL PRIMARY KEY,
    url TEXT NOT NULL,
    word TEXT NOT NULL,
    FOREIGN KEY(url) REFERENCES pages(url),
    FOREIGN KEY(word) REFERENCES words(word)
};

CREATE TABLE IF NOT EXISTS words {
    word TEXT NOT NULL PRIMARY KEY,
};

-- Maybe not needed (Only if server get unexpected error causing programing to crash)
CREATE TABLE IF NOT EXISTS notParsedPages (
    url TEXT NOT NULL PRIMARY KEY,
);