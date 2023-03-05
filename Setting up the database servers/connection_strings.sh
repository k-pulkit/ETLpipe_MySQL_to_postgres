-- MYSQL
mysql --protocol=tcp -h localhost -P 3306 -D s_retail_db -u s_retail_user -p

-- POSTGRESSQL
psql -h localhost -p 5432 -d t_retail_db -U t_retail_user -W 

-- Port forwarding
ssh -i ~/.ssh/google_compute_engine -fNL 3306:localhost:3306 -fNL 5432:localhost:5432 8080:localhost:8080  user@IP
ps aux | grep ssh

# in case of errors when connecting to DB from python with mysql connector, use
# alter user s_retail_user@'%' identified by 's_retail_pass';