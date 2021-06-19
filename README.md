# DBS Project 2021

## Prerequisites
* Docker
* Docker Compose
* PostgreSQL (Client libaries)
* python3
* pip3 
* python3-venv

## Database

### Start container
Also builds container if not existent.

    sudo docker-compose -f docker-compose.yml up

### Stop and reset state
Warning: This will reset the state of the database
to the initial state.

    sudo docker-compose down

To just stop container use the following:

    sudo docker-compose stop

### Change init scripts
    sudo docker-compose -f docker-compose.yml down
    sudo docker-compose -f docker-compose.yml build --no-cache
    sudo docker-compose -f docker-compose.yml up

### Webserver

### Setting up virtual env

    /web/setup-venv.sh


### Start server

    /web/src/start-server.sh



