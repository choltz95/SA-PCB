CC := g++
CFLAGS := -g -std=c++17 -O2 -pthread -Wall -Wextra
LIBS := -lboost_regex

sa : main.o readFiles.o readScl.o
	$(CC) $(CFLAGS) $(LIBS) -o sa main.o readFiles.o  readScl.o

main.o : main.h readFiles.h readScl.h main.cpp
	$(CC) $(CFLAGS) $(LIBS) -c main.cpp

readFiles.o : readFiles.h readScl.h readFiles.cpp
	$(CC) $(CFLAGS) $(LIBS) -c readFiles.cpp

#readNets.o : readFiles.h readNets.h readNets.cpp
#	$(CC) $(CFLAGS) $(LIBS) -c readNets.cpp

readScl.o : readFiles.h readScl.h readScl.cpp
	$(CC) $(CFLAGS) $(LIBS) -c readScl.cpp

clean :
	-rm *.o
