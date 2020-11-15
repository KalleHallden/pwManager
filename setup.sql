CREATE DATABASE IF NOT EXISTS pwmanager;
use pwmanager;

CREATE TABLE IF NOT EXISTS accounts (
    password VARCHAR(255),
    email VARCHAR(255),
    username VARCHAR(255),
    url VARCHAR(255),
    app_name VARCHAR(255)
);
