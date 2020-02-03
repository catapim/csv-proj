CREATE TABLE all_data (
    id serial,
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
    TotalProfit FLOAT,
    PRIMARY KEY (id)
);

CREATE TABLE master_country (
    id integer not null,
    Region CHAR(100),
    Country CHAR(100),
    PRIMARY KEY (id)
);


