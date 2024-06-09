from lib.print_diamond import print_diamond


def test_print_diamond_with_A():
    assert print_diamond("A") == "A"

def test_print_diamond_with_C():
    assert print_diamond("C") == (
        "  A  \n"
        " B B \n"
        "C   C\n"
        " B B \n"
        "  A  "
    )