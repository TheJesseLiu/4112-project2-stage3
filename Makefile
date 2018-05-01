# File: Makefile
# Simple make file to build the executable

TARGETS = branch_mispred_q3_04_v2
CC=gcc
CFLAGS = -g -Wall -O3 -save-temps
INCLUDE = 
LIBS = 

all: $(TARGETS)

branch_mispred: branch_mispred_q3_04_v2.o
	$(CC) $(CFLAGS) $(LIB_INCLUDE) -o $@ branch_mispred_q3_04_v2.o $(LIBS)
.c.o:
	$(CC) $(CFLAGS) $(INCLUDE) -c -o  $*.o $<
clean:
	rm -f *.o *~ $(TARGETS)
