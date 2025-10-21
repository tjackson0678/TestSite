#include <stdio.h>

void interpolate( double x1, double x2, double y1, double y2){
	double x_mid;
	double y_mid;

	x_mid = (x2+x1)/2;
	y_mid = (y2+y1)/2;

	printf("(%f, %f)\n", y_mid, x_mid);
}

int main(){
	interpolate(0.0,10.0, 0.0, 10.0);
	return 0;
}
