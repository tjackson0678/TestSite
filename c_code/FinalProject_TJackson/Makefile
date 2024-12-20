X2 : X2_Main.o X2.o 
	cc -o X2 X2_Main.o X2.o
X2_Main.o: X2_Main.c X2.h
	cc -c X2_Main.c 
X2.o: X2.c X2.h
	cc -c X2.c

clean: 
	rm X2 X2.o X2_Main.o
