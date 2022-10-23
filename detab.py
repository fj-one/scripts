"""Convert tabs into equivalent number of blanks."""

import argparse
import sys

STOPS = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128]


def main():
    """Run program."""
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("infile", nargs="?", default=sys.stdin, type=argparse.FileType("rt"))
    parser.add_argument("outfile", nargs="?", default=sys.stdout, type=argparse.FileType("wt"))
    parser.add_argument(
        "-s",
        nargs="+",
        default=STOPS,
        type=int,
        help="tab stops %(default)s",
        metavar="INT",
        dest="stops",
    )
    args = parser.parse_args()
    for line in args.infile:
        buff = []
        col = 1
        for char in line:
            if char == "\t":
                while True:
                    buff.append(" ")
                    col += 1
                    if tabpos(col, args.stops):
                        break
            else:
                buff.append(char)
                col += 1
        print("".join(buff), end="", file=args.outfile)


def tabpos(col, stops):
    """Return True if col is a tab stop."""
    return col in stops or col > max(stops)


if __name__ == "__main__":
    sys.exit(main())
