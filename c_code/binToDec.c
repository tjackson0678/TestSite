#include "stdio.h"
#include <math.h>

int main() {

int bits[8] = {1, 0, 1, 0, 0, 0, 1, 1};
int sum = 0; 
	for (int i=0; i<8; i++) {
		sum = sum + bits[7-i] * (int)pow(2,i); 
	}
	printf("Answer is %d\n", sum); 
return 0;
}
