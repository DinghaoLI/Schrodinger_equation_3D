CC = g++
CFLAGS = -std=c++11 -Wall -Wextra -g
TESTGEN = cxxtestgen
TESTFLAGS = --error-printer
TESTS = MyTest.h
TARGET = main
OBJS = main.o Solver.o

#Compiler le code
all: $(TARGET)

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) $^ -o $@ -larmadillo

main.o: main.cpp
	$(CC) $(CFLAGS) -c $< -o $@

%.o: %.cpp %.h
	$(CC) $(CFLAGS) -c $< -o $@

#Compiler les tests unitaires
test: tests
	./tests

tests.cpp: $(TESTS)
	$(TESTGEN) $(TESTFLAGS) -o $@ $(TESTS)

tests.o: tests.cpp
	$(CC) $(CFLAGS) -c $^ -o $@

tests: tests.o Solver.o
	$(CC) $(CFLAGS) $^ -o $@ -larmadillo

#Vérifier les fuites mémoires
memcheck: tests
	valgrind ./tests

.PHONY: clean

clean:
	rm -f *.o
	rm -f $(TARGET)
	rm -f *.pickle
	rm -f tests.cpp
	rm -f tests



