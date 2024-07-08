# ex: set ts=8 noet:

all: qt5

testpy3:
	python3 -m unittest discover tests

qt5: qt5py3

qt5py3:
	pyrcc5 -o resources.py resources.qrc

.PHONY: test
