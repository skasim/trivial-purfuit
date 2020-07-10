SHELL := /bin/bash

docs: # generate pydoc
	python3 -m pydoc src/* > TrivialPurfuitDocs.txt

clean-docs:
	sed -i '' -e "s/$(d)//g" TrivialPurfuitDocs.txt
