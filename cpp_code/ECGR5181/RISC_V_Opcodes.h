#ifndef RISC_V_OPCODES_H
#define RISC_V_OPCODES_H

// B-TYPE Instructions
#define OPCODE_BEQ      0b1100011   BEQ   
#define OPCODE_BGE      0b1100011   BGE
#define OPCODE_BGEU     0b1100011   BGEU
#define OPCODE_BLT      0b1100011   BLT
#define OPCODE_BLTU     0b1100011   BLTU
#define OPCODE_BNE      0b1100011   BNE

// C-TYPE Instructions
#define OPCODE_CSRRC    0b1110011   CSRRC
#define OPCODE_CSRRCI   0b1110011   CSRRCI
#define OPCODE_CSRRS    0b1110011   CSRS
#define OPCODE_CSRRSI   0b1110011   CSRRSI 
#define OPCODE_CSRRW    0b1110011   CSRRW
#define OPCODE_CSRRWI   0b1110011   CSRRWI
#define OPCODE_EBREAK   0b1110011   EBREAK
#define FUNCT3_EBREAK   0b000       
#define FUNCT7_EBREAK   0b0000001
#define OPCODE_ECALL    0b1110011
#define FUNCT3_ECALL    0b000
#define FUNCT7_ECALL    0b0000000

// F-TYPE Instructions
#define OPCODE_FENCE    0b0001111
#define OPCODE_FENCE_I  0b0001111

// I-TYPE Instructions
#define OPCODE_ADDI     0b0010011
#define OPCODE_ADDIW    0b0011011
#define OPCODE_ANDI     0b0010011
#define OPCODE_FLD      0b0000111
#define FUNCT3_FLD      0b011
#define OPCODE_FLW      0b0000111
#define FUNCT3_FLW      0b010
#define OPCODE_JALR     0b1100111
#define FUNCT3_JALR     0b000
#define OPCODE_LB       0b0000011
#define FUNCT3_LB       0b000
#define OPCODE_LBU      0b0000011
#define FUNCT3_LBU      0b100
#define OPCODE_LD       0b0000011
#define FUNCT3_LD       0b011
#define OPCODE_LH       0b0000011
#define FUNCT3_LH       0b001
#define OPCODE_LHU      0b0000011
#define FUNCT3_LHU      0b101
#define OPCODE_LW       0b0000011
#define FUNCT3_LW       0b010
#define OPCODE_LWU      0b0000011
#define FUNCT3_LWU      0b110
#define OPCODE_ORI      0b0010011
#define FUNCT3_ORI      0b110
#define OPCODE_SLLI     0b0010011
#define FUNCT3_SLLI     0b001
#define OPCODE_SLLIW    0b0010011
#define FUNCT3_SLLIW    0b001
#define OPCODE_SLTI     0b0010011
#define FUNCT3_SLTI     0b010
#define OPCODE_SLTIU    0b0010011
#define FUNCT3_SLTIU    0b011

// R-TYPE Instructions
#define OPCODE_ADD      0b0110011
#define FUNCT3_ADD      0b000
#define FUNCT7_ADD      0b0000000
#define OPCODE_SUB      0b0110011
#define FUNCT3_SUB      0b000
#define FUNCT7_SUB      0b0100000
#define OPCODE_SLL      0b0110011
#define FUNCT3_SLL      0b001
#define FUNCT7_SLL      0b0000000
#define OPCODE_SLT      0b0110011
#define FUNCT3_SLT      0b010
#define FUNCT7_SLT      0b0000000
#define OPCODE_SLTU     0b0110011
#define FUNCT3_SLTU     0b011
#define FUNCT7_SLTU     0b0000000
#define OPCODE_XOR      0b0110011
#define FUNCT3_XOR      0b100
#define FUNCT7_XOR      0b0000000
#define OPCODE_SRL      0b0110011
#define FUNCT3_SRL      0b101
#define FUNCT7_SRL      0b0000000
#define OPCODE_SRA      0b0110011
#define FUNCT3_SRA      0b101
#define FUNCT7_SRA      0b0100000
#define OPCODE_OR       0b0110011
#define FUNCT3_OR       0b110
#define FUNCT7_OR       0b0000000
#define OPCODE_AND      0b0110011
#define FUNCT3_AND      0b111
#define FUNCT7_AND      0b0000000


#endif // RISC_V_OPCODES_H