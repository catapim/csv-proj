TEST_COPY = "COPY records_copy FROM '/home/catalina/csv-proj/records2.csv' " \
            "insert into master_country select country, " \
            "region from records_copy;"

INSERT_INTO_MASTER = "insert into master_country (region, country) values ('america', 'chile');"
