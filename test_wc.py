"""Tests for wc.py"""

import os
from subprocess import getstatusoutput

SCRIPT = "wc.py"
INVOC = f"python {SCRIPT}"

BLANKFILE = ".\\testinputs\\blankfile.txt"
SINGLECHAR = ".\\testinputs\\singlechar.txt"
FOX = ".\\testinputs\\fox.txt"
FOX10 = ".\\testinputs\\fox10.txt"

# number of characters per newline
NLCHAR = 2 if os.name == "nt" else 1


def test_exists():
    """Module exists."""
    assert os.path.isfile(SCRIPT)


def test_usage():
    """Prints usage in response to -h/--help."""
    for flag in ["-h", "--help"]:
        exitcode, output = getstatusoutput(f"{INVOC} {flag}")
        assert exitcode == 0
        assert output.lower().startswith("usage")


def test_blank_file():
    """Prints correct output for blank file."""
    exitcode, output = getstatusoutput(f"{INVOC} {BLANKFILE}")
    assert exitcode == 0
    actual = parse_output(output)
    expected = 0, 0, 0, BLANKFILE
    assert actual == expected


def test_single_character():
    """Prints correct output for file with single character."""
    exitcode, output = getstatusoutput(f"{INVOC} {SINGLECHAR}")
    assert exitcode == 0
    actual = parse_output(output)
    expected = 1, 1, 1, SINGLECHAR
    assert actual == expected


def test_fox():
    """Prints correct output for 'The quick brown fox jumps over the lazy dog'."""
    exitcode, output = getstatusoutput(f"{INVOC} {FOX}")
    assert exitcode == 0
    actual = parse_output(output)
    expected = 1, 9, 44, FOX
    assert actual == expected


def test_fox10():
    """Prints correct output for 10 lines of 'fox'."""
    exitcode, output = getstatusoutput(f"{INVOC} {FOX10}")
    assert exitcode == 0
    actual = parse_output(output)
    nlines = 10
    nwords = nlines * 9
    nchars = 44
    nbytes = (nchars + NLCHAR) * nlines
    expected = nlines, nwords, nbytes, FOX10
    assert actual == expected


def parse_output(output):
    """Parse one line of output into line, word, byte count, path name."""
    # assumed no space in path
    lct, wct, bct, path = output.split()
    return int(lct), int(wct), int(bct), path
