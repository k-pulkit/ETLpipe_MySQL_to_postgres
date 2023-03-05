#!/bin/bash
echo "Loading data to mysql"
mysql --protocol=tcp -h localhost -P 3306 -D s_retail_db -u s_retail_user -p < ./create_db.sql
echo "Complete"

echo "Create schemas in postgres"
psql -h localhost -p 5432 -d t_retail_db -U t_retail_user -W -i ./create_db_tables_pg.sql
echo "Complete"