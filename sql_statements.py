TEST_COPY = "COPY records_copy FROM 'records2.csv' insert into master_country select country, region from records_copy;"
