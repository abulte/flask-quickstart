This is a quickstart Flask project with all the extensions I usually require from start for a SPA project. All the extensions are pre-configured. It's designed to get up and running quickly on Docker, with no requirements on the host machine except Docker Toolbox. Just clone, run and customize!

## Requirements

Docker Toolbox https://www.docker.com/toolbox

## What's inside

TODO

## Quickstart

```
# will build and run the web and db containers
docker-compose up -d
# will create the initial tables (roles and users)
docker-compose run web python manage.py db upgrade
# create a superuser
docker-compose run web python manage.py create_superuser user@domain.com us3rPassword
# enjoy -> http://<your-docker-ip>:5001
```

## Customize

TODO
