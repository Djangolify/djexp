all: clean test install

install:
	python setup.py install

test:
	python -m unittest

clean:
	rm -rf build/ djexp.egg-info/ dist/

deploy:
	python3 -m pip install --user --upgrade setuptools wheel
	python3 setup.py sdist bdist_wheel
	python3 -m pip install --user --upgrade twine
	twine upload dist/*
