### Docker


To use docker, create a docker container with the following commands.

```
docker create --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=<password> mariadb/server
```

Then start the container.

```
docker start mysql
```

You're all setup!