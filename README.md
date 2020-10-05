# Notify

[![Build Status](https://travis-ci.org/rozumalex/notify.svg?branch=master)](https://travis-ci.org/github/rozumalex/notify)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/rozumalex/notify/blob/master/LICENSE)

---

Notify is asynchronous app for creating notes based on aiohttp.


## Installation Guide


If you want to get a copy of this app for your personal usage,
please follow the instructions below.


### Clone the project to your local machine

```
git clone https://github.com/rozumalex/notify
```

### Install poetry

```
pip install poetry
```

### Install dependencies

***Note:*** you need to get to the directory with the project,
then you can run the command: 

```
poetry install
```

### Install postgresql and create user and database

```
sudo apt install postgres psycopg2 -y
sudo -u postgres psql
CREATE DATABASE <DATABASE_NAME>;
CREATE ROLE <USER_NAME> WITH ENCRYPTED PASSWORD '<PASSWORD>';
GRANT ALL PERMISSIONS ON DATABASE <DATABASE_NAME> TO <USER_NAME>;
ALTER USER <USER_NAME> CREATEDB;
```

### Create config.yaml file in the main folder

***Note:*** insert your personal data.

```
postgres:
  database: DATABASE_NAME
  user: USER_NAME
  password: PASSWORD
  host: localhost
  port: 5432

site:
  secret_key: SECRET_KEY
  lang: en
  charset: utf-8
  site_name: SITE_NAME
```

### Run app

```
poetry shell
python app.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/rozumalex/notify/blob/master/LICENSE) file for details.

