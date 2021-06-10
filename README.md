# Setup

## Create and start db container
sudo docker-compose -f docker-compose.yml up

## Stop and remove containers, networks, images, and volumes
sudo docker-compose down

## Change init scripts
sudo docker-compose -f docker-compose.yml down
sudo docker-compose -f docker-compose.yml build --no-cache
sudo docker-compose -f docker-compose.yml up