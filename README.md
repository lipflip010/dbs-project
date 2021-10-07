# DBS Project 2021

A simple web application to visualize and compare statistics of two countries. 

## Used tools
* postgres database
* python-flask for web application
* matplotlib to create plots

## Example

![Selection_028](https://user-images.githubusercontent.com/17150689/136340512-cc5a3a88-7e79-4872-8400-596476f2c558.png)

## Setup

### Prerequisites
* Docker
* Docker Compose
* PostgreSQL (Client libaries)
* python3
* pip3 
* python3-venv

### Database

#### Start container
Also builds container if not existent.

    sudo docker-compose -f docker-compose.yml up

### Stop and reset state
Warning: This will reset the state of the database
to the initial state.

    sudo docker-compose down

To just stop container use the following:

    sudo docker-compose stop

#### Change init scripts
    sudo docker-compose -f docker-compose.yml down
    sudo docker-compose -f docker-compose.yml build --no-cache
    sudo docker-compose -f docker-compose.yml up

### Webserver

#### Setting up virtual env

    /web/setup-venv.sh


#### Start server

    /web/start-server.sh

## Sources
https://matplotlib.org/stable/users/license.html

