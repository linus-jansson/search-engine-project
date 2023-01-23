CREATE TABLE page (
  url TEXT NOT NULL PRIMARY KEY,
  title TEXT NOT NULL,
  summary TEXT NOT NULL,
  full_text TEXT NOT NULL, -- Store the full text of the page to easier get what the client is looking for
  fetch_time TIMESTAMP NOT NULL
);
