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
#define AUIPC   "0010111"
#define UJ_TYPE "1101111"


// Main function
int main() {
    
    string codeType; 
    string binary;
    string opCode ;
    string rd;
    string func3; 
    string rs1;
    string rs2;
    string func7;
    string imm;
    int imm_signed = 0;

    while (true) {
    codeType = ""; 

    // Read a 32-bit binary string from user
    if (!readBinaryString(binary)) {
        return 1;
    }

    // Extract fields from the binary string
    opCode = binary.substr(25, 7);
    rd = binary.substr(20, 5);
    func3 = binary.substr(17, 3); 
    rs1 = binary.substr(12, 5);

    
    // Print functions used in decoder.cpp for R-Type instructions
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
    // Print function for I-Type and S-Type instructions
    auto i_print = [&](const string &opc, const string &f3) {
        auto ops = itype_ops_from_bits(opc, f3);
        cout << "OpCode=" << opc << "\n" << "f3=" << f3 << "\nInstruction -> ";
        if (ops.empty()) cout << "(none)\n";
        else {
            for (size_t i = 0; i < ops.size(); ++i) {
                if (i) cout << ", ";
                cout << ops[i];
            }
            if (codeType == "I_TYPE_LOAD") // Load instructions
                cout << " x" << stoi(rd, nullptr, 2) << ", " << imm_signed << "(x" << stoi(rs1, nullptr, 2) << ")\n";
            else if (codeType == "S_TYPE") // Store instructions
                cout << " x" << stoi(rs2, nullptr, 2) << ", " << imm_signed << "(x" << stoi(binary.substr(18, 3), nullptr, 2) << ")\n";
            else if (codeType == "SB_TYPE") // Branch instructions
                cout << " x" << stoi(rs1, nullptr, 2) << ", x" << stoi(rs2, nullptr, 2) << ", " << imm_signed << "\n";
            else if (codeType == "U_TYPE") // U-Type instructions
                cout << " x" << stoi(rd, nullptr, 2) << ", " << imm_signed << "\n";
            else if (codeType == "UJ_TYPE") // UJ-Type instructions
                cout << " x" << stoi(rd, nullptr, 2) << ", " << imm_signed << "\n";
            else
            // I-Type arithmetic instructions
            cout << " x" << stoi(rd, nullptr, 2) << ", x" << stoi(rs1, nullptr, 2) << ", " << imm_signed << "\n";
        }
    };
    // Determine instruction type based on opcode
    if (opCode == R_TYPE) {
        codeType = "R_TYPE";
        rs2 = binary.substr(7, 5);
        func7 = binary.substr(0, 7);
        print(opCode,func3,func7);
    }
    // S-Type Store instructions
    else if (opCode == S_TYPE) {
        codeType = "S_TYPE";    
        rs2 = binary.substr(8, 5);
        imm = binary.substr(0, 8) + binary.substr(21, 4);
        imm_signed = bin2SignedDec(imm, 12);
        i_print(opCode,binary.substr(18, 3));

    }
    // I-Type instructions
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
    // UJ-Type instructions
    else if (opCode == UJ_TYPE) {
        codeType = "UJ_TYPE";
    }
    // SB-Type instructions
    else if (opCode == SB_TYPE) {
        codeType = "SB_TYPE";
        rs2 = binary.substr(7, 5);
        imm = binary[0] + binary.substr(24,1) + binary.substr(1,6) + binary.substr(20,4) + "0";
        imm_signed = bin2SignedDec(imm, 13);
        i_print(opCode,func3);
    }
    // U-Type instructions
    else if (opCode == U_TYPE || opCode == AUIPC) {
        codeType = "U_TYPE";
        imm = binary.substr(0, 20) + "000000000000";
        imm_signed = bin2SignedDec(imm, 32);
        i_print(opCode, "000");
    }
    // UJ-Type instructions
    else if (opCode == UJ_TYPE) {
        codeType = "UJ_TYPE";
        imm = binary[0] + binary.substr(12,8) + binary.substr(11,1) + binary.substr(1,10) + "0";
        imm_signed = bin2SignedDec(imm, 21);
        i_print(opCode, "000");
    }
    
    else {
        cout << "Does not match any type" << endl;
    }
   
    cout << "Code Type: " << codeType << "\n" << endl;

    }
    return 0;
}
