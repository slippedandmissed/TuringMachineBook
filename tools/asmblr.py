#!/usr/bin/python3.9

from riscv_assembler.convert import AssemblyConverter
cnv = AssemblyConverter()
cnv.convert("simple.s")
#outputs to binary file simple.bin
