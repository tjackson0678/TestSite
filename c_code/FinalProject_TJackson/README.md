### README  <br> Terrence Jackson <br> ECGR 5100 - Fall 2024 <br> 
#### X2 - Take Home Project 

<ins>**API**</ins> 

**int imul(int x, int y)** <br> 
This function takes in two integers and returns a the result of multiplying those integers using an iterative method. 

**int idiv(int n, int d)** <br> 
This function takes a numerator and denominator and returns the quotient of dividing the numerator n by the denominator d. The remainder is not returned. 

**Makefile** <br>
This file contains the ruleset for running and compiling the project. 
Simply run **'make'** and the code will compile.  After that run **'X2'** and the executeable file will run 
```
% make 
  cc -c X2_Main.c 
  cc -c X2.c
  cc -o X2 X2_Main.o X2.o
% X2
  This is the result of dividing 16 into 5: 3
  The product of multiplying 5 and 5: 25
```

