#!/bin/bash

echo "[mysqld]\nbind-address = 0.0.0.0" > custom_my.cnf
docker run -d --name mysql-docker -p 13306:3306 -v $(pwd)/custom_my.cnf:/etc/mysql/mysql.conf.d/mysqld.cnf --env MYSQL_ALLOW_EMPTY_PASSWORD=yes mysql/mysql-server:5.7
sleep 30
docker exec mysql-docker sh -c 'echo "CREATE USER '\''root'\''@'\''%'\''; GRANT ALL PRIVILEGES ON *.* TO '\''root'\''@'\''%'\'' WITH GRANT OPTION; FLUSH PRIVILEGES;" | mysql -u root'
mysql -u root -h 127.0.0.1 -P 13306

