#!/bin/bash

echo "Work in progress..."
docker pull mysql
docker run -e MYSQL_ROOT_PASSWORD=password1234! -p 3333:3306 -d mysql:latest