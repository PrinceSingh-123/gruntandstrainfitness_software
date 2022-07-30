DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Attendances;
DROP TABLE IF EXISTS Expenses;
DROP TABLE IF EXISTS Revenues;
DROP TABLE IF EXISTS Staffs;

CREATE TABLE Users (
    username TEXT PRIMARY KEY CHECK (length(username) > 4 and length(username) < 10),
    email TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    age INTEGER,
    address TEXT,
    profile_pic BLOB,
    bio TEXT,
    membership_type TEXT NOT NULL
);

CREATE TABLE Attendances (
	user TEXT NOT NULL,
	day DATE NOT NULL DEFAULT (DATE('now')),
	present SMALLINT NOT NULL DEFAULT 0 CHECK (present IN (0,1)),
	FOREIGN KEY (user) REFERENCES Users (username),
    PRIMARY key (user, day)
);

CREATE TABLE Expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    purpose TEXT NOT NULL,
    amount REAL NOT NULL,
    description TEXT,
    added_at DATETIME NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE Revenues (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    source TEXT NOT NULL,
    amount REAL NOT NULL,
    description TEXT,
    added_at DATETIME NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE Staffs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    position TEXT NOT NULL,
    salary REAL,
    date_joined DATE NOT NULL DEFAULT (DATE('now')),
    due_amount REAL,
    paid SMALLINT NOT NULL DEFAULT 0 CHECK (paid IN (0,1,2)),
    generate_date DATE
);