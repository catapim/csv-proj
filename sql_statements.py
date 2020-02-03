TEST_COPY = "COPY master_country (id, region, country) FROM '/csv/filtered_region_country.csv' " \
            "(FORMAT csv, HEADER, DELIMITER ',');"

WRITE_ALL_CSV_TO_DB = "COPY all_data (region, country, itemType, SalesChannel, OderPriority, OrderDate, OrderId, ShipDate, UnitsSold, UnitPrice, UnitCost, TotalRevenue, TotalCost, TotalProfit) FROM '/csv/records.csv' (FORMAT csv, HEADER, DELIMITER ',');"
