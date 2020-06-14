# Trivial Purfuit
### Project for Foundations of Software Engineering at Johns Hopkins University

## Getting Started

### Tools needed:
* `Python` version 3.8
* `Pyenv` enables use of multiple versions of Python and also managing virtual environments
* IDE such as `PyCharm`
* `Docker`
* `pip3` to help install libraries in `requirements.txt`

### Python and Virtual Environments
Since we are working on different operating systems, it is essential that we use a `requirements.txt` file 
and a virtual environment. By doing so we ensure that we have the same environment set up across our different machines
and avoid the problem of "it works on my machine".

With `Pyenv`:
* create a virtual env with `pyenv virtualenv 3.8.0 trivial-purfuit`, which creates an virtual env locally called `trivial-purfuit` using Python 3.8.0
* activate the virtual env `pyenv activate trivial-purfuit`
* deactivate the virtual env `pyenv deactivate trivial-purfuit`

Once you have your virtual env set up, you are ready to install libraries. We don't have any libraries yet, but I added 
a `python-dateutil==2.8.1` library for you to test. 
* To see what libraries you have installed in your virtual env, you run
the command `pip3 freeze`
* You create a `requirements.txt` file by running `pip3 freeze > requirements.txt` 
* You install what is in the requirements file by running `pip3 install -r requirements.txt`. This ensures we all have the same libraries

### Virtual Environments and IDE
When using an IDE, you must add your virtual env to PyCharm as well. This [Stackoverflow post](https://stackoverflow.com/a/51545578/4882806) covers how to add the virtual env
you created above to PyCharm 

### Docker
The advantage of using Docker is that we are running the code on the exact same machine while developing locally.

If we end up adding databases, then this will be very helpful. If you are not familiar with Docker, it is containerized development
and allows us to run code in containers so that we have the *exact* same env. 

when you bring up docker, it creates a container, which allows us to install libraries and run our code in the container.
The Docker container mounts your local computer's Trivial Purfuit directory to the container's directory in `/opt/trivial-purfuit`

### Steps to bring up docker containers
Note: This project utilizes a `Makefile` to ease use of terminal commands. I encourage you to take a look at the `Makefile`

* Clone this project to a directory. For me the project exists in `/Users/samra/FdnsSoftwareEng/Development/TrivialPurfuit` directory on my local machine
* Use command `make add-path d="path/to/directory/TrivialPursuit"` to add the path to where Trivial Pursuit directory is on your computer.
For me, this command looks like `make add-path d="/Users/samra/FdnsSoftwareEng/Development/TrivialPurfuit"`. You will see that in 
`docker-compose.yml` this command updates the path to where docker mounts for each of our local environments

```
services:
  python:
    build: ./docker
    container_name: trivial
    command: bash -c "pip install -r requirements.txt && tail -f /dev/null"
    ports:
      - 8000:8000
    volumes:
      - /path/to/local/here:/opt/trivial-purfuit
```
* Use `make build` to build a Docker image that is based on the contents of the `Dockerfile`
* Once the image builds successfully, run `make up` to bring up the docker container called `trivial`
* Run `make logs` to see that docker container is up and `ctrl+c` to exit that log
* Run `make status` to view the status of your docker container
* Run `make exec-trivial` to enter the `trivial` docker container
* You will enter in the `/opt/trivial-purfuit` directory and the files that are in your local computer are mounted in this directory.
If you delete anything in the container's `/opt/trivial-purfuit` directory, it will also delete it locally and vice-versa.
* While in the container, run `pip3 install -r requirements.txt`, which will install the `python-dateutil==2.8.1` library
* Also, in the container run `python3 helloword.py`, which should output `Hello Software Titans!`. If you go into your IDE and open up the 
`hellworld.py` file and change the output to `Hello World!` and run the file in the container, you will see that the change is immediately available in the container
because it is mounted to your local directory
* Type `exit` in the container's command line to exit the container
* Run `make down` to stop the container. This will save your container's state. So, for example, the library you installed will be available next
time you run `make up`. If you run `make kill`, it destroys the container, so when you run `make up` again you will have to reinstall the `requirements.txt` file.
