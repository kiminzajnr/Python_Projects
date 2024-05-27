# MySQL Replication

![MySQL_Replication](/MySQL_Replication/img/Repl.png)

## MySQL 5.7.* Installation
## [How To Install Guide](https://intranet.alxswe.com/concepts/100002) - (credits: [nuuX](https://github.com/nuuxcode) - C13)
- Check version:
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
server-id        = 1
log_bin          = /var/log/mysql/mysql-bin.log
binlog_do_db     = tyrell_corp
```
- To:
```
/etc/mysql/mysql.conf.d/mysqld.cnf
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

## Migrate existing data to slave
- Create a mysqldump utility
```
scp -i ~/.ssh/priv.key tyrell_corp.sql ubuntu@slave_ip:/tmp/
```

- create `tyrell_corp` database in slave
```
CREATE DATABASE tyrell_corp;
```

- import the snapshot
```
sudo mysql tyrell_corp < /tmp/tyrell_corp.sql
```

- Unlock tables in master
```
UNLOCK TABLES;
```

# Configure slave
- Add:
```
server-id               = 2
log_bin                 = /var/log/mysql/mysql-bin.log
binlog_do_db            = tyrell_corp
relay-log               = /var/log/mysql/mysql-relay-bin.log
```

- To:
```
/etc/mysql/mysql.conf.d/mysqld.cnf
```

- restart MySQL
```
sudo systemctl restart mysql
```

# Testing Replication

- On slave, configure replication settings by running:

```
CHANGE MASTER TO
MASTER_HOST='master_ip',
MASTER_USER='replica_user',
MASTER_PASSWORD='password#70',
MASTER_LOG_FILE='mysql-bin.000001',
MASTER_LOG_POS=154;
```

- Activate slave
```
START SLAVE;
```

- Show slave state
```
SHOW SLAVE STATUS\G;
```

- Creating an entry in master should now reflect in slave