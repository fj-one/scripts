"""Decomment Fortran source files."""

import argparse
import os.path
import sys

FIXED = ".f", ".for"

MAX_LINE_LENGTH = 2048

BANG = "!"
APOS = "'"
QUOT = '"'
QUOTE_CHARS = APOS, QUOT
BKSLSH = "\\"


def main():
    """Run program."""
    exitcode = 0
    parser = argparse.ArgumentParser()
    parser.add_argument("infile", type=argparse.FileType("rt"))
    parser.add_argument("outfile", nargs="?", default=sys.stdout, type=argparse.FileType("wt"))
    parser.add_argument("--qamode", action="store_true")
    parser.add_argument("--qafile")
    args = parser.parse_args()
    ext = os.path.splitext(args.infile.name)[1].lower()
    decomment = decomment_fixed if ext in FIXED else decomment_free
    if args.qamode:
        qafile = args.qafile or ("qa.f" if ext in FIXED else "qa.f90")
        with open(qafile, "a") as f:
            for n, line in enumerate(args.infile, start=1):
                decommented = decomment(line)
                if line != decommented:
                    print(">", f"file: {args.infile.name}, line {n}", file=f)
                    print("-", line.rstrip(), file=f)
                    print("+", decommented.rstrip(), file=f)
                    print("", file=f)
                args.outfile.write(decommented)
    else:
        for line in args.infile:
            args.outfile.write(decomment(line))
    return exitcode


def decomment_fixed(line):
    """Return decommented line for fixed-format FORTRAN."""
    if not line.strip() or line[0] in "cC*!":
        return ""
    return decomment_bang(line, fixed=True) if BANG in line else line


def decomment_free(line):
    """Return decommented line for free-format Fortran."""
    if not (stripped := line.strip()) or (stripped.startswith(BANG)):
        return ""
    return decomment_bang(line) if BANG in line else line


def decomment_bang(line, fixed=False):
    """Return decommented exclamation-mark-containing line."""
    ibang = line.index(BANG)
    if fixed and ibang == 5:
        head, tail = line[:6], line[6:]
        return head + decomment_bang(tail) if BANG in tail else head + tail

    iapos = line.index(APOS) if APOS in line else MAX_LINE_LENGTH
    iquot = line.index(QUOT) if QUOT in line else MAX_LINE_LENGTH
    if min(ibang, iapos, iquot) == ibang:
        return simple_strip(ibang, line)
    if BANG in (censored := censor(line)):
        return simple_strip(censored.index(BANG), line)
    return line


def simple_strip(index, line):
    """Slice up to index; right strip; append newline."""
    if s := line[:index].rstrip():
        return s + "\n"
    return ""


def censor(line, censor_char="X"):
    """Return line with string literals censored."""
    buff = []
    in_literal = False
    current_quote_char = None
    last_char = None
    for char in line:
        if char in QUOTE_CHARS:
            if current_quote_char is None:
                in_literal = True
                current_quote_char = char
            elif last_char == BKSLSH or char != current_quote_char:
                buff.append(censor_char)
                continue
            else:
                in_literal = False
                current_quote_char = None
                buff.append(censor_char)
                continue
        if in_literal:
            buff.append(censor_char)
        else:
            buff.append(char)
        last_char = char
    return "".join(buff)


sys.exit(main())
