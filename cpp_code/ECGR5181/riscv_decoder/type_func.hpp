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
static inline uint32_t parse_bin_u32(const std::string &bits) {
    return static_cast<uint32_t>(std::bitset<32>(bits).to_ulong());
}

// Build the R-type map (maps key -> list of possible instructions)
static inline std::unordered_map<uint32_t, std::vector<std::string> > build_rtype_map_with_opcode() {
    std::unordered_map<uint32_t, std::vector<std::string> > m;

    auto add = [&](const std::string &name, const std::string &opcode_str,
                   const std::string &f3, const std::string &f7) {
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
    add("sub",   "0110011", "000", "0110000");
    add("subw",  "0111011", "000", "0100000");
    add("xor",   "0110011", "100", "0000000");

    return m;
}

static const std::unordered_map<uint32_t, std::vector<std::string> > rtype_map_with_opcode = build_rtype_map_with_opcode();

// Lookup by numeric opcode/funct3/funct7
std::vector<std::string> rtype_ops_from_ints(uint8_t opcode7, uint8_t funct3, uint8_t funct7) {
    uint32_t key = make_rtype_key_uint(opcode7, funct7, funct3);
    auto it = rtype_map_with_opcode.find(key);
    if (it == rtype_map_with_opcode.end()) return {};
    return it->second;
}

// Lookup by bit-strings like "0110011", "001", "0000000"
std::vector<std::string> rtype_ops_from_bits(const std::string &opcode_bits,
                                             const std::string &funct3_bits,
                                             const std::string &funct7_bits) {
    uint8_t opc = static_cast<uint8_t>(parse_bin_u32(opcode_bits));
    uint8_t f3 = static_cast<uint8_t>(parse_bin_u32(funct3_bits));
    uint8_t f7 = static_cast<uint8_t>(parse_bin_u32(funct7_bits));
    return rtype_ops_from_ints(opc, f3, f7);
}


// Build the I-type map (maps key -> list of possible instructions)
static inline std::unordered_map<uint16_t, std::vector<std::string>> build_itype_map_with_opcode() {
    std::unordered_map<uint16_t, std::vector<std::string>> m;

    auto add = [&](const std::string &name, const std::string &opcode_str,
                   const std::string &f3) {
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

    // system / CSR immediate variants are sometimes encoded with opcode 1110011 and specific funct3,
    add("csrrw",  "1110011", "001");
    add("csrrs",  "1110011", "010");
    add("csrrc",  "1110011", "011");
    add("csrrwi", "1110011", "101");
    add("csrrsi", "1110011", "110");
    add("csrrci", "1110011", "111");

    return m;
}

static const std::unordered_map<uint16_t, std::vector<std::string>> itype_map_with_opcode = build_itype_map_with_opcode();

// Lookup by numeric opcode/funct3
std::vector<std::string> itype_ops_from_ints(uint8_t opcode7, uint8_t funct3) {
    uint16_t key = make_itype_key_uint(opcode7, funct3);
    auto it = itype_map_with_opcode.find(key);
    if (it == itype_map_with_opcode.end()) return {};
    return it->second;
}

// Lookup by bit-strings like "0010011", "000"
std::vector<std::string> itype_ops_from_bits(const std::string &opcode_bits,
                                             const std::string &funct3_bits) {
    uint8_t opc = static_cast<uint8_t>(parse_bin_u32(opcode_bits));
    uint8_t f3  = static_cast<uint8_t>(parse_bin_u32(funct3_bits));
    return itype_ops_from_ints(opc, f3);
}


// Convert a binary string to a signed decimal integer
int bin2SignedDec(const std::string& binary, int significantBits) {
    int power = static_cast<int>(std::pow(2, significantBits - 1));
    int sum = 0;

    // Check the sign bit (most significant bit)
    if (binary[0] == '1') {
        sum = -power; // If negative, subtract the value of the MSB
    }

    // Add the values of the remaining bits
    for (int i = 1; i < significantBits; ++i) {
        if (binary[i] == '1') {
            sum += static_cast<int>(std::pow(2, significantBits - 1 - i));
        }
    }
    return sum;
}