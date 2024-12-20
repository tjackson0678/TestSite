#include <stdio.h>

#define MAX 100

extern int printf(const char *, ...);

int main () {

	int x = MAX; 

	printf("Hello World!\n");
	return x;
}
