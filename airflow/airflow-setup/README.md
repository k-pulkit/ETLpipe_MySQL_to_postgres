## How to setup the airflow service

To install the airflow service for out test application, we will be deploying airflow containers using docker-compose on the VM instance on the cloud. I am using the same machine where the postgres and the mysql instances are running.

Since, everything is running on docker containers, so the environments are isolated for the services.

In order to make the development easier, I am using a linux utility called `sshfs` which allows me to sync my local and remote directories.

```shell
user=$(echo $HOME | awk -F '/' '{print $3}') 
sshfs -o sync,sshfs_sync,sync_readdir,nonempty $user@instancex:/home/$user/airflow/ ./airflow/

# To kills the same, or related sshfs processes
ps aux | grep sshfs | awk '{print $2}' | xargs kill 9   
```

While seeting up the airflow env with docker-compose, I faces many challenges, mainly that helped me to get a more clear understanding of docker and docker-compose. On of the key steps, is to make sure that the database initializatons are done before starting the webserver. The same is ensured with below snipped in docker-compose file.
```yaml
command: ["bash", "-c", 
           "airflow db init && 
            airflow users create --role Admin --username admin --email admin --firstname admin --lastname admin --password admin && 
            airflow webserver -D && 
            airflow scheduler -D"]
```
This file, like mentioned do the admin stuff so you can access the web-server without any issues.

The airflow env can be spun with the `sudo docker build -t my_airflow:latest . && docker-compose up -d ` command.

