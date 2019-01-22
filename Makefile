all: clean test install

.PHONY: test test-verbose clean pre_build build install deploy

test:
	python -m unittest

test-verbose:
	python -m unittest -v

clean:
	rm -rf build/ djexp.egg-info/ dist/

pre_build:
	pip3 install --user --upgrade setuptools wheel twine

build: pre_build
	python setup.py sdist bdist_wheel

install: pre_build
	python setup.py install

deploy: build dist
	twine upload dist/*
