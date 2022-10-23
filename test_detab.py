"""Tests for detab.py"""

import os
from subprocess import getstatusoutput

SCRIPT = "detab.py"
INVOC = f"python {SCRIPT}"

BLANKFILE = ".\\testinputs\\blankfile.txt"
FOX = ".\\testinputs\\fox.txt"
FOXTAB = ".\\testinputs\\fox-tab.txt"


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
    expected = ""
    assert output == expected


def test_tabless_file():
    """Prints correct output for tabless file."""
    exitcode, output = getstatusoutput(f"{INVOC} {FOX}")
    assert exitcode == 0
    expected = "The quick brown fox jumps over the lazy dog."
    assert output == expected


def test_tabbed_file_default_stops():
    """Prints correct output for file with tabs using default stops."""
    exitcode, output = getstatusoutput(f"{INVOC} {FOXTAB}")
    assert exitcode == 0
    expected = "The    quick brown fox jumps over the  lazy dog."
    assert output == expected


def test_tabbed_file_custom_stops():
    """Prints correct output for file with tabs using custom stops."""
    exitcode, output = getstatusoutput(f"{INVOC} {FOXTAB} -s 12 50")
    assert exitcode == 0
    expected = "The        quick brown fox jumps over the        lazy dog."
    assert output == expected


if __name__ == "__main__":
    test_exists()
    test_usage()
    test_blank_file()
    test_tabless_file()
    test_tabbed_file_default_stops()
    test_tabbed_file_custom_stops()
    print("all tests passed!")
