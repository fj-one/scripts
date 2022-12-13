"""Concatenate files and print to standard output."""

import argparse
import glob


def main(argv=None):
    """Run program."""
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="*", help="file name (or glob pattern)", metavar="FILE")
    args = parser.parse_args(argv)
    for pathspec in args.files:
        for pathname in glob.glob(pathspec):
            with open(pathname) as file:
                for line in file:
                    print(line, end="")


if __name__ == "__main__":
    main()
