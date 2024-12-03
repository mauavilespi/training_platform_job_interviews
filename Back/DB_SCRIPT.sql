-- Create the database 
CREATE DATABASE interview_system;

-- Use the newly created database

-- Create the "records" table
CREATE TABLE records (
    id SERIAL PRIMARY KEY,
    record JSON NOT NULL
);

-- Create the "questions" table
CREATE TABLE questions (
    id SERIAL PRIMARY KEY,
    question TEXT NOT NULL,
    active BOOLEAN DEFAULT TRUE
);

-- Create the "categories" table
CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    category TEXT NOT NULL,
    active BOOLEAN DEFAULT TRUE
);

-- Create the "belong_to" table to represent the relationship between "questions" and "categories"
CREATE TABLE belong_to (
    id SERIAL PRIMARY KEY,
    question_id INT NOT NULL,
    category_id INT NOT NULL,
    FOREIGN KEY (question_id) REFERENCES questions (id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES categories (id) ON DELETE CASCADE
);