all: src doc bindings

src:
	$(MAKE) -C src

doc:
	doxygen ./Doxyfile

test:
	$(MAKE) -C src test

bindings:
	$(MAKE) -C install

.PHONY: clean src doc

clean:
	$(MAKE) -C src clean
	$(MAKE) -C doc clean

style:
	astyle --options=astyle.conf ./src/*.cpp ./src/*.h