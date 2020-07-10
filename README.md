# Trivial Purfuit
### Project for Foundations of Software Engineering at Johns Hopkins University

## Getting Started

### Tools needed:
* `Python` version 3.8
* `Pyenv` enables use of multiple versions of Python and also managing virtual environments
* IDE such as `PyCharm`
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

### Generate Documentation
Use `make docs` to generate documentation. To clean up file names in the documentation to make them generic use:
```
sed -i '' -e "s/path\/to\/local\///g" TrivialPurfuitDocs.txt
```
