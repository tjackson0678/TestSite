// Warriors Group
// ECGR 5181 - Computer Architecture
// Project 3 - Decoder 
// Fall 2025


// Example function to read a 32-bit binary string and store in an array
#include <iostream>
#include <string>
#include <stdio.h>

#define R_TYPE 0110011
#define S_TYPE 0100011
#define I_TYPE 0010011
#define SB_TYPE 1100011
#define U_TYPE 0110111 
#define UJ_TYPE 0110111


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
    readBinaryToArray(bits);

    int opCode = bits[];

    // Print array

    std::cout << "These are the last 6 bits: " << std::endl;
    for (int i = 26; i < 32; ++i) {
        std::cout << bits[i];
    }
    std::cout << std::endl;
    return 0;
}
