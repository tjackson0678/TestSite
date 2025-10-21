// Warriors Group
// ECGR 5181 - Computer Architecture
// Project 3 - Decoder 
// Fall 2025


// Example function to read a 32-bit binary string and store in an array
#include <iostream>
#include <string>
#include <stdio.h>
#include "type_func.hpp"

using namespace std;

#define R_TYPE  "0110011"
#define S_TYPE  "0100011"
#define I_TYPE  "0010011"
#define I_TYPE_LOAD  "0000011"
#define SB_TYPE "1100011"
#define U_TYPE  "0110111" 
#define UJ_TYPE "1101111"



bool readBinaryString(std::string &binary) {
    cout << "Enter a 32-bit binary number: ";
    cin >> binary;
    cout << endl; 

    if (binary.length() != 32) {
        cerr << "Error: Input must be 32 bits.\n";
        return false;
    }

    for (char c : binary) {
        if (c != '0' && c != '1') {
            cerr << "Error: Invalid character in input.\n";
            return false;
        }
    }

    return true;
}

// Example usage
int main() {
    
    int bits[32];
    string codeType; 
    string binary;

    while (true) {
    codeType = ""; 

    if (!readBinaryString(binary)) {
        return 1;
    }

    for (int i = 0; i < 32; ++i) {
        bits[i] = binary[i] - '0';
    }

    string opCode = binary.substr(25, 7);
    string rd = binary.substr(20, 5);
    string func3 = binary.substr(17, 3); 
    string rs1 = binary.substr(12, 5);
    string rs2;
    string func7;
    string imm;
    int imm_signed = 0;

    auto print = [&](const string &opc, const string &f3, const string &f7) {
        auto ops = rtype_ops_from_bits(opc, f3, f7);
        cout << "OpCode=" << opc << "\n" << "f3=" << f3 << "\n" << "f7=" << f7 << "\nInstruction -> ";
        if (ops.empty()) cout << "(none)\n";
        else {
            for (size_t i = 0; i < ops.size(); ++i) {
                if (i) cout << ", ";
                cout << ops[i];
            }
            cout << " x" << stoi(rd, nullptr, 2) << ", x" << stoi(rs1, nullptr, 2) << ", x" << stoi(rs2, nullptr, 2) << "\n";
        }
    };

    auto i_print = [&](const string &opc, const string &f3) {
        auto ops = itype_ops_from_bits(opc, f3);
        cout << "OpCode=" << opc << "\n" << "f3=" << f3 << "\nInstruction -> ";
        if (ops.empty()) cout << "(none)\n";
        else {
            for (size_t i = 0; i < ops.size(); ++i) {
                if (i) cout << ", ";
                cout << ops[i];
            }
            if (codeType == "I_TYPE_LOAD")
                cout << " x" << stoi(rd, nullptr, 2) << ", " << imm_signed << "(x" << stoi(rs1, nullptr, 2) << ")\n";
            else
            cout << " x" << stoi(rd, nullptr, 2) << ", x" << stoi(rs1, nullptr, 2) << ", " << imm_signed << "\n";
        }
    };

    if (opCode == R_TYPE) {
        codeType = "R_TYPE";
        rs2 = binary.substr(7, 5);
        func7 = binary.substr(0, 7);
        print(opCode,func3,func7);
    }
    else if (opCode == S_TYPE) {
        codeType = "S_TYPE";
    }
    else if (opCode == I_TYPE || opCode == I_TYPE_LOAD) {
        if (opCode == I_TYPE){
            codeType = "I_TYPE";
        }
        else {
            codeType = "I_TYPE_LOAD";
        }
        imm = binary.substr(0, 12);
        imm_signed = bin2SignedDec(imm, 12);
        i_print(opCode,func3);
    }   
    else if (opCode == SB_TYPE) {
        codeType = "SB_TYPE";
    }
    else if (opCode == U_TYPE) {
        codeType = "U_TYPE";
    }
    else {
        cout << "Does not match any type" << endl;
    }
   
    cout << "Code Type: " << codeType << "\n" << endl;

    }
    return 0;
}
