PWD=$(shell pwd)

.PHONY=mysql
mysql:
	docker run -d --name mysql-tms --env-file .env -p 3406:3306 -v $(PWD)/init.sql:/data/init.sql mysql/mysql-server:latest

.PHONY=mysql-down
mysql-down:
	docker stop mysql-tms
	docker rm mysql-tms
