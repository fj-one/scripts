"""Print line, word, and byte counts for each file.

Print newline, word, and byte counts for each FILE, and a total line if
more than one FILE is specified.  A word is a non-zero-length sequence
of characters delimited by whitespace.
"""

import argparse
import math
import os.path
import sys
from glob import glob

SUCCESS = 0
NOSUCHFILE = -1
ISADIRECTORY = 1
PERMISSIONERROR = 2


def main():
    """Run program."""
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("files", nargs="*", help="file name (or glob pattern)", metavar="FILE")
    args = parser.parse_args()
    result = read_files(args.files)
    edit(result)
    return calc_exitcode(result)


def read_files(pathnames):
    """Return dict mapping pathname to line, word, byte counts, status flag."""
    result = {}
    for pathname in pathnames:
        if pnames := glob(pathname):
            for pname in pnames:
                lct = wct = bct = flg = 0
                try:
                    with open(pname, "rb") as file:
                        lct, wct, bct = wordcount(file)
                except PermissionError:
                    flg = ISADIRECTORY if os.path.isdir(pname) else PERMISSIONERROR
                result[pname] = lct, wct, bct, flg
        else:
            result[pathname] = 0, 0, 0, NOSUCHFILE
    return result


def wordcount(file):
    """Return line, word, and byte count in file."""
    lct = wct = bct = 0
    for line in file:
        lct += 1
        wct += len(line.split())
        bct += len(line)
    return lct, wct, bct


def edit(result):
    """Print output to screen."""
    tot = calc_totals(result)
    wid = calc_width(tot)
    nfile = 0
    for pname, (lct, wct, bct, flg) in result.items():
        if flg >= 0:
            if flg == ISADIRECTORY:
                print(f"wc: {pname}: Is a directory")
            elif flg == PERMISSIONERROR:
                print(f"wc: {pname}: Permission error")
            print(f"{lct:{wid}} {wct:{wid}} {bct:{wid}} {pname}")
            nfile += 1
        elif flg == NOSUCHFILE:
            print(f"wc: {pname}: No such file or directory")
    if nfile > 1:
        print(f"{tot[0]:{wid}} {tot[1]:{wid}} {tot[2]:{wid}} total")


def calc_totals(result):
    """Return total line, word, and byte counts."""
    totline = totword = totbyte = 0
    for lct, wct, bct, _ in result.values():
        totline += lct
        totword += wct
        totbyte += bct
    return totline, totword, totbyte


def calc_width(totals):
    """Return column width for printing."""
    width = 1
    if (maxcount := max(totals)) > 1:
        width = math.ceil(math.log10(maxcount))
    return width


def calc_exitcode(result):
    """Return 1 if an error was detected, otherwise 0."""
    for *_, flag in result.values():
        if flag < 0:
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
