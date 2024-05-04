CREATE TABLE users (
    id SERIAL PRIMARY KEY NOT NULL, 
    username TEXT UNIQUE NOT NULL, 
    password TEXT NOT NULL
);
CREATE TABLE enemylist (
    id SERIAL PRIMARY KEY, 
    name TEXT UNIQUE, 
    health INTEGER,
    attack INTEGER
);
CREATE TABLE characterlist (
    id SERIAL PRIMARY KEY, 
    name TEXT, 
    health INTEGER,
    attack INTEGER
);
CREATE TABLE fights (
    id SERIAL PRIMARY KEY,
    name TEXT,
)
CREATE TABLE fightsenemies (
    id SERIAL PRIMARY KEY,
    fight_id INTEGER REFERENCES fights(id),
    enemylist_id INTEGER REFERENCES enemylist(id),
)