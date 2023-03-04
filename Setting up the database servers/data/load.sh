#!/bin/bash
echo "Loading data to mysql"
mysql --protocol=tcp -h localhost -P 3306 -D s_retail_db -u s_retail_user -p < ./create_db.sql
echo "Complete"