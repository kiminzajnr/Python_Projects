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

# Setting up the replication

# Configre master

- Add:
```
server-id              = 1
log_bin                 = /var/log/mysql/mysql-bin.log
binlog_do_db     = tyrell_corp
```
To:
```
sudo vi /etc/mysql/mysql.conf.d/mysqld.cnf
```

- Restart MySQL
```
sudo systemctl restart mysql
```

- Get Binary log coordinates from master

```
FLUSH TABLES WITH READ LOCK;
SHOW MASTER STATUS;
```