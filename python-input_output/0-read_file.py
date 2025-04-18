#!/usr/bin/python3
"""
   code for reading utf8 files
"""   

def read_file(filename=""):
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
