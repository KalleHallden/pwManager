CREATE DATABASE IF NOT EXISTS password_manager;
use password_manager;

CREATE TABLE IF NOT EXISTS accounts (
    password VARCHAR(255),
    email VARCHAR(255),
    username VARCHAR(255),
    url VARCHAR(255),
    app_name VARCHAR(255)
);
