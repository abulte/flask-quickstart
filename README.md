This is a quickstart Flask project with all the extensions I usually require from start for a classic project (no SPA, no API). All the extensions are pre-configured. It's designed to get up and running quickly on Docker, with no requirements on the host machine except Docker Toolbox. Just clone, run and customize!

## Requirements

Docker Toolbox https://www.docker.com/toolbox

## What's inside

* PostgreSQL database w/ Flask-Sqlalchemy and migrations w/ Flask-Migrate
* Bootstrap (CSS framework) w/ Flask-Bootstrap
* Users, roles, authentication and authorization w/ Flask-Security
* Bootstrap integration for Flask-Login forms
* Command line tools w/ Flask-Script
* Secured backoffice w/ Flask-Admin

## Quickstart

```
# will build and run the web and db containers
docker-compose up -d
# will create the initial tables (roles and users)
docker-compose run web python manage.py db upgrade
# create a superuser
docker-compose run web python manage.py create_superuser user@domain.com us3rPassword
```

## Customize

TODO
