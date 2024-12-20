#include <stdio.h>

void stars (int n) {
    
    for (int i=1; i<=n; i++) {
	for (int j=0; j<i; j++) {
	    printf("*");
	}
	printf("\n");
    }
}

int main () {

   stars(5);

   return 0;
}
