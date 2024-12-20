/*
 * X2.c
 *
 *  Created on: Dec 2, 2024
 *      Author: Terrence Jackson
 *      Purpose: Source file containing function definitions
 */

#include "X2.h"

int imul(int x, int y){

	int ans = x, i = 0;

	if (y==0) return 0;

	for (i=1; i< y; i++){
		ans += x;
	}

	return ans;
}

int idiv(int n, int d){

	int q = 0, r;
	r = n;

	while(r > d){
		r = r - d;
		q += 1;
	}

	return q;
}
