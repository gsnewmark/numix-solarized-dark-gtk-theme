#!/usr/bin/env python3

import sys

def get_replace_lines(theme):
    with open(theme, "r") as f:
        text = f.read()
        raw_lines = text.split('\n')
        lines = [line for line in raw_lines if len(line) != 0 and line[0] != '#']
        splits = [line.split(' ', 1) for line in lines]
        return splits

def content(file):
    with open(file, "r") as f:
        return f.read()

def replace(replace_lines, to_replace):
    text = to_replace
    for line in replace_lines[::-1]:
        text = text.replace(line[0], line[1])
    return text

def write(text, file):
    with open(file, "w") as f:
        f.write(text)

replace_lines = get_replace_lines(sys.argv[1])
before = content(sys.argv[2])
after = replace(replace_lines, before)
write(after, sys.argv[3])
