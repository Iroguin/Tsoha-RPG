CREATE TABLE users (
    id SERIAL PRIMARY KEY NOT NULL, 
    username TEXT UNIQUE NOT NULL, CHECK (LENGTH(username) >= 3 AND LENGTH(username) <= 25),
    password TEXT NOT NULL
); --list of users
CREATE TABLE enemylist (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE,
    health INTEGER,
    attack INTEGER
); --list of all enemies
CREATE TABLE characterlist (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE,
    health INTEGER,
    attack INTEGER,
    exp INTEGER DEFAULT 0
); --list of characters in active party
CREATE TABLE fights (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE,
    difficulty INT
); --list of fights
CREATE TABLE fightsenemies (
    id SERIAL PRIMARY KEY,
    fight_id INTEGER REFERENCES fights(id),
    enemylist_id INTEGER REFERENCES enemylist(id)
); --relationships of what fights have what enemies