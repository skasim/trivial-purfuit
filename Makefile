SHELL := /bin/bash

build: # build docker image
	docker-compose build

up: # bring up docker containers
	docker-compose up -d

down: # bring down docker containers but not lose docker state
	docker-compose down

kill: # kill docker containers and lose docker state
	docker-compose kill

exec-trivial: # enter docker trivial containers
	docker exec -it trivial bash

logs: # show logs for containers or <name> container
	docker-compose logs -f $(c)

prune: # clean up docker temporary files
	docker system prune --volumes

status: # status of containers
	docker-compose ps

add-path: # add your local path to Trivial Purfuit dir
	sed -i '' -e "s|- /.*|- $(d):/opt/trivial-purfuit|g" docker-compose.yml

clean-path: # clean up the path before commits
	sed -i '' -e "s|- /.*|- /path/to/local/here:/opt/trivial-purfuit|g" docker-compose.yml
