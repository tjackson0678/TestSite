// Warriors Group
// ECGR 5181 - Computer Architecture
// Project 3 - Function Definitions
// Fall 2025

#include <cstdint>
#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>
#include <bitset>
#include <string>
#include <stdio.h>
#include <functional>

using namespace std;

// Function to read a 32-bit binary string from user
bool readBinaryString(string &binary) {
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

// Build a key from opcode (7 bits), funct7 (7 bits) and funct3 (3 bits):
// key = (opcode << 10) | (funct7 << 3) | funct3
static inline uint32_t make_rtype_key_uint(uint8_t opcode7, uint8_t funct7, uint8_t funct3) {
    return (uint32_t(opcode7) << 10) | (uint32_t(funct7) << 3) | (funct3 & 0x7);
}

// Build a key from opcode (7 bits) and funct3 (3 bits):
// key = (opcode << 3) | funct3
static inline uint16_t make_itype_key_uint(uint8_t opcode7, uint8_t funct3) {
    return (uint16_t(opcode7) << 3) | (funct3 & 0x7);
}

// Helper to parse binary strings like "0110011" or "0100000"
static inline uint32_t parse_bin_u32(const string &bits) {
    return static_cast<uint32_t>(bitset<32>(bits).to_ulong());
}

// Build the R-type map (maps key -> list of possible instructions)
static inline unordered_map<uint32_t, vector<string> > build_rtype_map_with_opcode() {
    unordered_map<uint32_t, vector<string> > m;

    auto add = [&](const string &name, const string &opcode_str,
                   const string &f3, const string &f7) {
        uint8_t opcode = static_cast<uint8_t>(parse_bin_u32(opcode_str));
        uint8_t funct3 = static_cast<uint8_t>(parse_bin_u32(f3));
        uint8_t funct7 = static_cast<uint8_t>(parse_bin_u32(f7));
        uint32_t key = make_rtype_key_uint(opcode, funct7, funct3);
        m[key].push_back(name);
    };

    // Entries taken from your CSV (R-TYPE lines). Opcode values used as in the CSV.
    add("add",   "0110011", "000", "0000000");
    add("addw",  "0111011", "000", "0000000");
    add("and",   "0110011", "111", "0000000");
    add("div",   "0110011", "100", "0000001");
    add("divu",  "0110011", "101", "0000001");
    add("divuw", "0111011", "101", "0000001");
    add("divw",  "0111011", "100", "0000001");
    add("mul",   "0110011", "000", "0000001");
    add("mulh",  "0110011", "001", "0000001");
    add("mulhsu","1100111", "010", "0000001");
    add("mulhu", "1100111", "011", "0000001");
    add("mulw",  "0111011", "000", "0000001");
    add("or",    "0110011", "110", "0000000");
    add("rem",   "0110011", "110", "0000001");
    add("remu",  "0110011", "111", "0000001");
    add("remuw", "0111011", "111", "0000001");
    add("remw",  "0111011", "110", "0000001");
    add("sll",   "0110011", "001", "0000000");
    add("sllw",  "0111011", "001", "0000000");
    add("slt",   "0110011", "010", "0000000");
    add("sltu",  "0110011", "011", "0000000");
    add("sra",   "0110011", "101", "0100000");
    add("sraw",  "0110011", "101", "0100000");
    add("srl",   "0110011", "101", "0000000");
    add("srlw",  "0111011", "001", "0100000");
    add("sub",   "0110011", "000", "0100000");
    add("subw",  "0111011", "000", "0100000");
    add("xor",   "0110011", "100", "0000000");
    add("fsub.s", "1010011", "000", "0000001");

    return m;
}

static const unordered_map<uint32_t, vector<string> > rtype_map_with_opcode = build_rtype_map_with_opcode();

// Lookup by numeric opcode/funct3/funct7
vector<string> rtype_ops_from_ints(uint8_t opcode7, uint8_t funct3, uint8_t funct7) {
    uint32_t key = make_rtype_key_uint(opcode7, funct7, funct3);
    auto it = rtype_map_with_opcode.find(key);
    if (it == rtype_map_with_opcode.end()) return {};
    return it->second;
}

// Lookup by bit-strings like "0110011", "001", "0000000"
vector<string> rtype_ops_from_bits(const string &opcode_bits,
                                             const string &funct3_bits,
                                             const string &funct7_bits) {
    uint8_t opc = static_cast<uint8_t>(parse_bin_u32(opcode_bits));
    uint8_t f3 = static_cast<uint8_t>(parse_bin_u32(funct3_bits));
    uint8_t f7 = static_cast<uint8_t>(parse_bin_u32(funct7_bits));
    return rtype_ops_from_ints(opc, f3, f7);
}


// Build the I-type map (maps key -> list of possible instructions)
static inline unordered_map<uint16_t, vector<string>> build_itype_map_with_opcode() {
    unordered_map<uint16_t, vector<string>> m;

    auto add = [&](const string &name, const string &opcode_str,
                   const string &f3) {
        uint8_t opcode = static_cast<uint8_t>(parse_bin_u32(opcode_str));
        uint8_t funct3 = static_cast<uint8_t>(parse_bin_u32(f3));
        uint16_t key = make_itype_key_uint(opcode, funct3);
        m[key].push_back(name);
    };

    // Common I-type loads / immediates and system-like I-type entries
    add("addi",   "0010011", "000");
    add("addiw",  "0011011", "000");
    add("andi",   "0010011", "111");
    add("ori",    "0010011", "110");
    add("slti",   "0010011", "010");
    add("sltiu",  "0010011", "011");
    add("slli",   "0010011", "001");
    add("slliw",  "0011011", "001");
    add("lb",     "0000011", "000");
    add("lbu",    "0000011", "100");
    add("lh",     "0000011", "001");
    add("lhu",    "0000011", "101");
    add("lw",     "0000011", "010");
    add("lwu",    "0000011", "110");
    add("ld",     "0000011", "011");
    add("flw",    "0000111", "010");
    add("fld",    "0000111", "011");
    add("jalr",   "1100111", "000");

    //S-TYPE Store instructions
    add("sb",     "0100011", "000");
    add("sh",     "0100011", "001");
    add("sw",     "0100011", "010");
    add("sd",     "0100011", "011");    

    //B-TYPE Branch instructions
    add("beq",    "1100011", "000");
    add("bne",    "1100011", "001");
    add("blt",    "1100011", "100");
    add("bge",    "1100011", "101");
    add("bltu",   "1100011", "110");
    add("bgeu",   "1100011", "111");    

    // U-TYPE instruction
    add("lui",    "0110111", "000");
    add("auipc",  "0010111", "000");

    // UJ-TYPE instruction
    add("jal",    "1101111", "000");


    return m;
}

static const unordered_map<uint16_t, vector<string>> itype_map_with_opcode = build_itype_map_with_opcode();

// Lookup by numeric opcode/funct3
vector<string> itype_ops_from_ints(uint8_t opcode7, uint8_t funct3) {
    uint16_t key = make_itype_key_uint(opcode7, funct3);
    auto it = itype_map_with_opcode.find(key);
    if (it == itype_map_with_opcode.end()) return {};
    return it->second;
}

// Lookup by bit-strings like "0010011", "000"
vector<string> itype_ops_from_bits(const string &opcode_bits,
                                             const string &funct3_bits) {
    uint8_t opc = static_cast<uint8_t>(parse_bin_u32(opcode_bits));
    uint8_t f3  = static_cast<uint8_t>(parse_bin_u32(funct3_bits));
    return itype_ops_from_ints(opc, f3);
}


// Convert a binary string to a signed decimal integer
int bin2SignedDec(const string& binary, int significantBits) {
    int power = static_cast<int>(pow(2, significantBits - 1));
    int sum = 0;

    // Check the sign bit (most significant bit)
    if (binary[0] == '1') {
        sum = -power; // If negative, subtract the value of the MSB
    }

    // Add the values of the remaining bits
    for (int i = 1; i < significantBits; ++i) {
        if (binary[i] == '1') {
            sum += static_cast<int>(pow(2, significantBits - 1 - i));
        }
    }
    return sum;
}

// Function to set control signals based on instruction type and opcode
void setControlSignals(const string& ins, string& aluop, string& regread, string& regwrite, 
                      string& memread, string& memwrite, string& writemode, string& immmode,
                      string& itypemode, string& shiftimmode, string& unsignedmode,
                      string& auipcenable, string& branchenable, string& jumpenable) {
    
    // Default values - everything disabled
    aluop = "00000";
    regread = "0";
    regwrite = "0";
    memread = "0";
    memwrite = "0";
    writemode = "00";
    immmode = "00";
    itypemode = "0";
    shiftimmode = "0";
    unsignedmode = "0";
    auipcenable = "0";
    branchenable = "0";
    jumpenable = "0";
    
    // Load instructions
    if (ins == "lb" || ins == "lbu" || ins == "lh" || ins == "lhu" || ins == "lw" || ins == "flw") {
        aluop = "00001";
        regread = ins == "flw" ? "0" : "0"; // According to signals.txt
        regwrite = "1";
        memread = "1";
        memwrite = "0";
        writemode = "10";
        immmode = "01";
        
        if (ins == "flw") {
            // Special case for floating point load
            jumpenable = "0";
        }
    }
    
    // Store instructions
    else if (ins == "sb" || ins == "sh" || ins == "sw" || ins == "fsw") {
        aluop = "00001";
        regread = "1";
        regwrite = "0";
        memread = "0";
        memwrite = "1";
        writemode = "00";
        immmode = "01";
        itypemode = "1";
        
        if (ins == "fsw") {
            // Special case for floating point store
        }
    }
    
    // Floating point move instructions
    else if (ins == "fmv.s.x") {
        aluop = "00110";
        regread = "0";
        regwrite = "1";
        memread = "0";
        memwrite = "0";
        writemode = "00";
        immmode = "10";
    }
    else if (ins == "fmv.x.s") {
        aluop = "00111";
        regread = "1";
        regwrite = "0";
        memread = "0";
        memwrite = "0";
        writemode = "00";
        immmode = "10";
    }
    
    // Integer arithmetic instructions
    else if (ins == "add") {
        aluop = "00001";
        regread = "1";
        regwrite = "1";
        memread = "0";
        memwrite = "0";
        writemode = "00";
        immmode = "10";
    }
    else if (ins == "addi") {
        aluop = "00001";
        regread = "1";
        regwrite = "1";
        memread = "0";
        memwrite = "0";
        writemode = "00";
        immmode = "01";
    }
    else if (ins == "sub") {
        aluop = "00010";
        regread = "1";
        regwrite = "1";
        memread = "0";
        memwrite = "0";
        writemode = "00";
        immmode = "10";
    }
    
    // Multiplication and division instructions
    else if (ins == "mul") {
        aluop = "10000";
        regread = "1";
        regwrite = "1";
        memread = "0";
        memwrite = "0";
        writemode = "00";
        immmode = "10";
    }
    else if (ins == "mulh") {
        aluop = "10001";
        regread = "1";
        regwrite = "1";
        memread = "0";
        memwrite = "0";
        writemode = "00";
        immmode = "10";
    }
    else if (ins == "mulhsu") {
        aluop = "10010";
        regread = "1";
        regwrite = "1";
        memread = "0";
        memwrite = "0";
        writemode = "00";
        immmode = "10";
    }
    else if (ins == "mulhu") {
        aluop = "10011";
        regread = "1";
        regwrite = "1";
        memread = "0";
        memwrite = "0";
        writemode = "00";
        immmode = "10";
    }
    else if (ins == "div") {
        aluop = "10100";
        regread = "1";
        regwrite = "1";
        memread = "0";
        memwrite = "0";
        writemode = "00";
        immmode = "10";
    }
    else if (ins == "divu") {
        aluop = "10101";
        regread = "1";
        regwrite = "1";
        memread = "0";
        memwrite = "0";
        writemode = "00";
        immmode = "10";
    }
    else if (ins == "rem") {
        aluop = "10110";
        regread = "1";
        regwrite = "1";
        memread = "0";
        memwrite = "0";
        writemode = "00";
        immmode = "10";
    }
    else if (ins == "remu") {
        aluop = "10111";
        regread = "1";
        regwrite = "1";
        memread = "0";
        memwrite = "0";
        writemode = "00";
        immmode = "10";
    }
    
    // Logical operations
    else if (ins == "and") {
        aluop = "00011";
        regread = "1";
        regwrite = "1";
        memread = "0";
        memwrite = "0";
        writemode = "00";
        immmode = "10";
    }
    else if (ins == "andi") {
        aluop = "00011";
        regread = "1";
        regwrite = "1";
        memread = "0";
        memwrite = "0";
        writemode = "00";
        immmode = "10";
    }
    else if (ins == "or") {
        aluop = "00100";
        regread = "1";
        regwrite = "1";
        memread = "0";
        memwrite = "0";
        writemode = "00";
        immmode = "10";
    }
    else if (ins == "ori") {
        aluop = "00100";
        regread = "1";
        regwrite = "1";
        memread = "0";
        memwrite = "0";
        writemode = "00";
        immmode = "10";
    }
    else if (ins == "xor") {
        aluop = "00101";
        regread = "1";
        regwrite = "1";
        memread = "0";
        memwrite = "0";
        writemode = "00";
        immmode = "10";
    }
    else if (ins == "xori") {
        aluop = "00101";
        regread = "1";
        regwrite = "1";
        memread = "0";
        memwrite = "0";
        writemode = "00";
        immmode = "10";
    }
    
    // U-Type instructions
    else if (ins == "lui") {
        aluop = "00000";
        regread = "0";
        regwrite = "1";
        memread = "0";
        memwrite = "0";
        writemode = "11";
        immmode = "00";
    }
    else if (ins == "auipc") {
        aluop = "00000";
        regread = "0";
        regwrite = "1";
        memread = "0";
        memwrite = "0";
        writemode = "11";
        immmode = "00";
        auipcenable = "1";
    }
    
    // Shift operations
    else if (ins == "sll") {
        aluop = "11000";
        regread = "1";
        regwrite = "1";
        memread = "0";
        memwrite = "0";
        writemode = "00";
        immmode = "10";
    }
    else if (ins == "slli") {
        aluop = "11000";
        regread = "1";
        regwrite = "1";
        memread = "0";
        memwrite = "0";
        writemode = "00";
        immmode = "01";
    }
    else if (ins == "srl") {
        aluop = "11001";
        regread = "1";
        regwrite = "1";
        memread = "0";
        memwrite = "0";
        writemode = "00";
        immmode = "10";
    }
    else if (ins == "srli") {
        aluop = "11001";
        regread = "1";
        regwrite = "1";
        memread = "0";
        memwrite = "0";
        writemode = "00";
        immmode = "01";
    }
    else if (ins == "sra") {
        aluop = "11010";
        regread = "1";
        regwrite = "1";
        memread = "0";
        memwrite = "0";
        writemode = "00";
        immmode = "10";
    }
    else if (ins == "srai") {
        aluop = "11010";
        regread = "1";
        regwrite = "1";
        memread = "0";
        memwrite = "0";
        writemode = "00";
        immmode = "01";
    }
    
    // Set less than operations
    else if (ins == "slt") {
        aluop = "01110";
        regread = "1";
        regwrite = "1";
        memread = "0";
        memwrite = "0";
        writemode = "00";
        immmode = "10";
    }
    else if (ins == "slti") {
        aluop = "01110";
        regread = "1";
        regwrite = "1";
        memread = "0";
        memwrite = "0";
        writemode = "00";
        immmode = "01";
    }
    else if (ins == "sltu") {
        aluop = "01111";
        regread = "1";
        regwrite = "1";
        memread = "0";
        memwrite = "0";
        writemode = "00";
        immmode = "10";
    }
    else if (ins == "sltiu") {
        aluop = "01111";
        regread = "1";
        regwrite = "1";
        memread = "0";
        memwrite = "0";
        writemode = "00";
        immmode = "01";
        unsignedmode = "1";
    }
    
    // Branch instructions
    else if (ins == "beq") {
        aluop = "01010";
        regread = "1";
        regwrite = "0";
        memread = "0";
        memwrite = "0";
        writemode = "00";
        immmode = "00";
        branchenable = "1";
    }
    else if (ins == "bne") {
        aluop = "01011";
        regread = "1";
        regwrite = "0";
        memread = "0";
        memwrite = "0";
        writemode = "00";
        immmode = "00";
        branchenable = "1";
    }
    else if (ins == "blt") {
        aluop = "01000";
        regread = "1";
        regwrite = "0";
        memread = "0";
        memwrite = "0";
        writemode = "00";
        immmode = "00";
        branchenable = "1";
    }
    else if (ins == "bge") {
        aluop = "01001";
        regread = "1";
        regwrite = "0";
        memread = "0";
        memwrite = "0";
        writemode = "00";
        immmode = "00";
        branchenable = "1";
    }
    else if (ins == "bltu") {
        aluop = "01100";
        regread = "1";
        regwrite = "0";
        memread = "0";
        memwrite = "0";
        writemode = "00";
        immmode = "00";
        branchenable = "1";
    }
    else if (ins == "bgeu") {
        aluop = "01101";
        regread = "1";
        regwrite = "0";
        memread = "0";
        memwrite = "0";
        writemode = "00";
        immmode = "00";
        branchenable = "1";
    }
    
    // Jump instructions
    else if (ins == "jal") {
        aluop = "00001";
        regread = "0";
        regwrite = "1";
        memread = "0";
        memwrite = "0";
        writemode = "10";
        immmode = "00";
        shiftimmode = "1";
        jumpenable = "1";
    }
    else if (ins == "jalr") {
        aluop = "00001";
        regread = "1";
        regwrite = "1";
        memread = "0";
        memwrite = "0";
        writemode = "10";
        immmode = "01";
        jumpenable = "1";
    }
}


