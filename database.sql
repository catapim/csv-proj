CREATE DATABASE sales;

CREATE USER 'admin' IDENTIFIED BY '1234';

GRANT USAGE ON *.* TO 'admin'@localhost IDENTIFIED BY '1234';

FLUSH PRIVILEGES;

SHOW GRANTS FOR 'admin';

CREATE TABLE all_data (
    Region CHAR(100),
    Country CHAR(100),
    ItemType CHAR(100),
    SalesChannel CHAR(100),
    OderPriority CHAR(1),
    OrderDate CHAR(100),
    OrderID INTEGER,
    ShipDate DATE,
    UnitsSold INTEGER,
    UnitPrice FLOAT,
    UnitCost FLOAT,
    TotalRevenue FLOAT,
    TotalCost FLOAT,
    TotalProfit FLOAT
);

CREATE TABLE master_country (
    Region CHAR(100),
    Country CHAR(100),
    ItemType CHAR(100)
);
