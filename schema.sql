CREATE TABLE users (
    id SERIAL PRIMARY KEY, 
    username TEXT, 
    password TEXT
);
CREATE TABLE enemylist (
    id SERIAL PRIMARY KEY, 
    name TEXT, 
    health INT,
    attack INT
);
CREATE TABLE characterlist (
    id SERIAL PRIMARY KEY, 
    name TEXT, 
    health INT,
    attack INT
);