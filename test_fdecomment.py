"""Tests for fdecomment.py"""

import os
from subprocess import getstatusoutput

SCRIPT = "fdecomment.py"
INVOC = f"python {SCRIPT}"

BLANKFILE = ".\\testinputs\\blankfile.txt"
FREE = ".\\testinputs\\comments_and_escapes.f90"
FREE_DEC = ".\\testinputs\\comments_and_escapes_decommented.f90"
FIXED = ".\\testinputs\\comments_and_escapes.f"
FIXED_DEC = ".\\testinputs\\comments_and_escapes_decommented.f"
FREE2 = ".\\testinputs\\learnfortran.f90"
FREE2_DEC = ".\\testinputs\\learnfortran_decommented.f90"


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


def test_free():
    """Prints correct output for free format Fortran."""
    exitcode, output = getstatusoutput(f"{INVOC} {FREE}")
    assert exitcode == 0
    expected = open(FREE_DEC).read()
    assert output.splitlines() == expected.splitlines()


def test_fixed():
    """Prints correct output for fixed format FORTRAN."""
    exitcode, output = getstatusoutput(f"{INVOC} {FIXED}")
    assert exitcode == 0
    expected = open(FIXED_DEC).read()
    assert output.splitlines() == expected.splitlines()


def test_free2():
    """A second test for free format Fortran."""
    exitcode, output = getstatusoutput(f"{INVOC} {FREE2}")
    assert exitcode == 0
    expected = open(FREE2_DEC).read()
    assert output.splitlines() == expected.splitlines()


if __name__ == "__main__":
    test_exists()
    test_usage()
    test_blank_file()
    test_free()
    test_fixed()
    test_free2()
    print("all tests passed!")
