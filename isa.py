"""Типы данных для представления и сериализации/десериализации машинного кода."""
# !/usr/bin/python3
# pylint: disable=missing-function-docstring  # чтобы не быть Капитаном Очевидностью

import json
from enum import Enum


class Opcode(str, Enum):
    """Opcode для ISA."""

    HLT = 'hlt'
    MOV = 'mov'
    CMP = 'cmp'
    CMP_REL_INC = 'cmp_rel_inc'
    RDIV = 'rdiv'
    ADD = 'add'
    INC = 'inc'

    IN = 'in'
    OUT = 'out'
    OUT_CHAR = 'out_char'
    OUT_REL = 'out_rel'
    JMP = 'jmp'
    JE = 'je'
    SV = 'sv'


def write_code(filename, code, data):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(json.dumps(code, indent=4))

    with open("data_file", "w", encoding="utf-8") as file:
        file.write(json.dumps(data, indent=4))


def read_code(filename):
    with open(filename, encoding="utf-8") as file:
        code = json.loads(file.read())

    with open("data_file", encoding="utf-8") as file:
        data_section = json.loads(file.read())

    return code, data_section
