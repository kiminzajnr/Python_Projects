# MySQL Replication

## MySQL Installation
[How To](https://intranet.alxswe.com/concepts/100002)

```
mysql --version
```

## Create a database on the primary server
```
CREATE DATABASE tyrell_corp;
```

## Create a table
```
USE tyrell_corp;
CREATE TABLE nexus6 (id int auto_increment primary key, name varchar(50));

```

## Add atleast one entry to the table
```
INSERT INTO nexus6(name) VALUES ("Erick");
```

## Create a new user for the replica 
```
CREATE USER 'replica_user'@'%' IDENTIFIED BY 'password';
```

## Grant replication permission
```
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
```
