CREATE DATABASE sales;
CREATE USER admin WITH PASSWORD '1234';
GRANT SELECT, INSERT, UPDATE, DELETE, TRIGGER, CONNECT ON sales TO admin;
