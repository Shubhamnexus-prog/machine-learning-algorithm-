CREATE DATABASE webgui;

USE webgui;

CREATE TABLE registration (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    course VARCHAR(100) NOT NULL,
    fee DECIMAL(10,2) NOT NULL
);

DESC registration;