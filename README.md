[![Code style:
black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# CSV TO MYSQL
This package help to import csv file and push data to MYSQL

# Requirement
Install python-mysql which can be installed from:
https://dev.mysql.com/doc/connector-python/en/
For debian and ubuntu user:
```
sudo apt install python-mysql
```
## Setup mysqldb configuration
inside /db/configure.py
```
configure = {
  'user': <username>
  'password': <password>
  'database': <database_name>
  }
```
