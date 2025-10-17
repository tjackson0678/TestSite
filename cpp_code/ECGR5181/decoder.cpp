// Warriors Group
// ECGR 5181 - Computer Architecture
// Project 3 - Decoder 
// Fall 2025


// Example function to read a 32-bit binary string and store in an array
#include <iostream>
#include <string>
#include <stdio.h>
#include "RISC_V_Opcodes.h"

#define R_TYPE 110011
#define S_TYPE 100011
#define I_TYPE 10011
#define SB_TYPE 1100011
#define U_TYPE 110111 
#define UJ_TYPE 110111


void readBinaryToArray(int arr[32]) {
    std::string binary;
    std::cout << "Enter a 32-bit binary number: ";
    std::cin >> binary;

    if (binary.length() != 32) {
        std::cerr << "Error: Input must be 32 bits.\n";
        return;
    }

    for (int i = 0; i < 32; ++i) {
        if (binary[i] == '0' || binary[i] == '1') {
            arr[i] = binary[i] - '0';
        } else {
            std::cerr << "Error: Invalid character in input.\n";
            return;
        }
    }
}

// Example usage
int main() {
    int bits[32];
    std::string codeType = ""; 
    readBinaryToArray(bits);

    int opCode = bits[25] * 1000000 + bits[26] * 100000 + bits[27] * 10000 + bits[28] * 1000 + bits[29] * 100 + bits[30] * 10 + bits[31] * 1;

    int test = 0b110011;

    // Print array

    /*std::cout << "These are the last 6 bits: " << std::endl;
    for (int i = 25; i < 32; ++i) {
        std::cout << bits[i];
    }*/

    int rd = bits[20] * 16 + bits[21] * 8 + bits[22] * 4 + bits[23] * 2 + bits[24] * 1;
    int func3 = bits[17] * 4 + bits[18] * 2 + bits[19] * 1; 
    int rs1 = bits[12] * 16 + bits[13] * 8 + bits[14] * 4 + bits[15] * 2 + bits[16] * 1;
    int rs2 = bits[7] * 16 + bits[8] * 8 + bits[9] * 4 + bits[10] * 2 + bits[11] * 1;
    int func7 = bits[0] * 64 + bits[1] * 32 + bits[2] * 16 + bits[3] * 8 + bits[4] * 4 + bits[5] * 2 + bits[6] * 1;

    switch (opCode)
    {   
    case R_TYPE:
        //std::cout << "R_TYPE" << std::endl;
        codeType = "R_TYPE";
        
        break;
    case S_TYPE:
        //std::cout << "S_TYPE" << std::endl;
        codeType = "S_TYPE";
        break;
    case I_TYPE:                
        //std::cout << "I_TYPE" << std::endl;
        codeType = "I_TYPE";
        break;
    case SB_TYPE:          
        //std::cout << "SB_TYPE" << std::endl;
        codeType = "SB_TYPE";
        break;                  
    case U_TYPE:        
        //std::cout << "U_TYPE" << std::endl;
        codeType = "U_TYPE";
        break;
    default:
        std::cout << "Does not match any type" << std::endl;
        break;
    }
   
    std::cout << "Code Type: " << codeType << std::endl;

    return 0;
}
