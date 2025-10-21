// Quadratic Equation
// ax + by + c = 0
// \frac{-b \pm \sqrt{b^2 - 4ac}{2a}
//

#include <math.h>
#include "stdio.h"
#include <string.h>

double quad (double a, double b, double c, char * sign) {
	double denom, result, desc, num;

	desc = (b * b) - (4 * a * c);
	
	if (strcmp(sign, "pos")) { 
		num = -b + sqrt(desc);
	} else num = -b - sqrt(desc); 
  
	denom = 2 * a; 

	result = num / denom;
	
	return result;
 
}
int main () {
	double x0, x1;
	x0 = quad(1, -1, -6, "pos"); 
	x1 = quad(1, -1, -6, "neg"); 
	printf("x_0 = %f\n", x0);
	printf("x_1 = %f\n", x1);
	return 0;

}
