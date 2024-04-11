CREATE TABLE users (
    id SERIAL PRIMARY KEY, 
    username TEXT, 
    password TEXT
);
CREATE TABLE commands (
    id SERIAL PRIMARY KEY,
    content TEXT,
    user_id INTEGER REFERENCES users,
);