TARGET=greeter

all: test
test:
	tox
install:
	python setup.py install
uninstall:
	echo y | pip uninstall $(TARGET) 
clean:
	rm -rf build
	rm -rf dist
	rm -rf tests/__pycache__
	rm -rf $(TARGET)/__pycache__
	rm -rf $(TARGET).egg-info
	find . -type f -name '*.pyc' -delete
run: install
	python -c 'import sys,greeter; sys.stdout.write(greeter.greet())'

