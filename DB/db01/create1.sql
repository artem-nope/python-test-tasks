DROP TABLE IF EXISTS languages;

CREATE TABLE IF NOT EXISTS languages
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    year INTEGER,
    rating REAL,
    created TEXT
);

INSERT INTO languages (name, year, rating, created)
VALUES
('python', 1991, 8.1, DATETIME('now')),
('c++', 1984, 7.5, DATETIME('now')),
('js', 1994, 7.9, DATETIME('now')),
('java', 1994, 7.7, DATETIME('now'));