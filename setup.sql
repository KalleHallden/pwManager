CREATE DATABASE IF NOT EXISTS pwmanager;
use pwmanager;

CREATE TABLE IF NOT EXISTS accounts (
    password VARCHAR,
    email VARCHAR,
    username VARCHAR,
    url VARCHAR,
    app_name VARCHAR
);
