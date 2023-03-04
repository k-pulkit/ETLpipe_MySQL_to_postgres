## How to setup the database servers (using docker on VM)?

We are hosting the PostGresSQL and MYSQL servers on a computing instance running in GCP virtual machine. The servers have been setup with the help of docker images.

For starting the compute instance, on next login:
```shell
gcloud compute instances start instance-z --zone=zone-name

#switch user
sudo su - root
sysmtemctl start docker

docker-compose up

# After this, just do a local port forward to access the databases on the localhost of dev machine
ssh -i ~/.ssh/google_compute_engine -L 3306:localhost:3306 -L 5432:localhost:5432  user@IP
```

In summary the steps are - 
1. Pull the docker image for both MySQL and PostGreSQL
2. Create a docker compose file to start the database servers
3. Use `docker-compose up` to start the containers
4. Use connection string to validate the connection

The servers are accessible over the local network of the VM. To access it over the network, we can do ssh port forward so external IPs can access the database servies.

To access the database on local machine, we can use the below command to securely access the services running locally on the VM.
```shell
ssh -i ~/.ssh/google_compute_engine -L 3306:localhost:3306 -L 5432:localhost:5432  user@IP
```

This will allow the local programs to access the database as if it were running locally.

Once, connected to the DB instances, we can create the required table schemas and load the tables in the source database MySQL.
