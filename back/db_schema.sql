CREATE TABLE IF NOT EXISTS words (
  id INTEGER NOT NULL PRIMARY KEY,
  word TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS parsedPages (
  id INTEGER NOT NULL PRIMARY KEY,
  url TEXT NOT NULL,
  title TEXT NOT NULL,
  summary TEXT NOT NULL,
  full_text TEXT NOT NULL, -- Store the full text of the page to easier get what the client is looking for
  fetch_time TIMESTAMP NOT NULL
);

CREATE TABLE IF NOT EXISTS notParsedPages (
  id INTEGER NOT NULL PRIMARY KEY,
  url TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS words_urls (
  word_id INTEGER NOT NULL CONSTRAINT words_urls_word_id_fk REFERENCES words(id),
  url_id INTEGER NOT NULL CONSTRAINT words_urls_url_id_fk REFERENCES parsedPages(id),
  CONSTRAINT words_urls_word_id_uq UNIQUE (word_id, url_id)
);
