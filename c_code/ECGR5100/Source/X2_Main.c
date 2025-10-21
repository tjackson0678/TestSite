

/*
 * X2_Main.c
 *
 *  Created on: Dec 13, 2024
 *      Author: Terrence Jackson
 *      Purpose: Main Function to exercise multiplication and division functions
 */

#include "X2.c"
#include <time.h>

int main()
{

	// Declare variable for functions
	int n = 1600, d = 246;
	int x = 554, y = 293;

	for (int i = 0; i < 3; i++)
	{
		n *= 109;
		x *= 18;

		clock_t begin = clock();

		// Print division and multiplication results
		printf("This is the result of dividing %d into %d: %d\n", n, d, idiv(n, d));
		printf("The product of multiplying %d and %d: %d\n", x, y, imul(x, y));

		clock_t end = clock();
		double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;

		printf("This part took %f seconds\n", time_spent);
		printf("\n");

		begin = clock();

		// Try this using regular multiplication and division
		printf("This is the result of dividing %d into %d: %d\n", n, d, n / d);
		printf("The product of multiplying %d and %d: %d\n", x, y, x * y);

		end = clock();
		time_spent = (double)(end - begin) / CLOCKS_PER_SEC;

		printf("This second part took %f seconds\n", time_spent);
		printf("\n");
	}

	return 0;
}
