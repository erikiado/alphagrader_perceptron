# https://www.alphagrader.com/courses/6/assignments/17
import fileinput
import re
import math


def read_input():
    lines = []
    # Read file input and clean each line
    for line in fileinput.input():
        lines.append(line.strip())
        print(line,end='')

def main():
    read_input()


if _name_ == '_main_':
    main()
