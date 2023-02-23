-- MYSQL
mysql --protocol=tcp -h localhost -P 3306 -D s_retail_db -u s_retail_user -p

-- POSTGRESSQL
psql -h localhost -p 5432 -d t_retail_db -U t_retail_user -W 

-- Port forwarding
ssh -i ~/.ssh/google_compute_engine -L 3306:localhost:3306 -L 5432:localhost:5432  user@IP