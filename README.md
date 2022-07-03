# URL-shortener
A simple URL shortener using python and django.

With this simple tool you can shorten your long URL to a simple and short one.

Tools
---
  - python
  - django
  - docker
  - nginx
  - html/css
  
Run Project
---
After cloning project, you can simply run this project by following instructions bellow.

### 1- environment variables.
create a `.env` file and set value for `SECRET_KEY`, `POSTGRES_NAME`, `POSTGRES_USER` and `POSTGRES_PASSWORD` keys.
### 2- install docker and docker-compose.
you can install docker from [here](https://docs.docker.com/engine/install/).

### 3- docker commands.
open a terminal and run command bellow.
```
docker-compose up
```
this command will run project on `localhost:80` and you will be able to visit that by your favorite browser.
