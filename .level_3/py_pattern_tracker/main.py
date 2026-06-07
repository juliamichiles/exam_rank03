import sys


def run_tests(user_module) -> None:
    name = "pattern_tracker"
    func = getattr(user_module, name, None)
    if not func:
        print(f"Error: Function '{name}' not found.")
        return

    print(func("123a345"))
    print(func("1a2b3c4d5"))
    print(func("12asd34hkh45kjhj56jhj67kjhjh78kjhjh89kjhkhj110"))
    print(func(""))
    print(func("7"))
    print(func("111111"))
    print(func("012345"))
    print(func("98"))
    print(func("12a23b34"))   # (1,2), (2,3), (3,4) → 3
    print(func("1!2@3#4"))    # no adjacent digits → 0
    print(func("01a12b23"))   # (0,1), (1,2), (2,3) → 3
    print(func("789"))        # (7,8), (8,9) → 2
    print(func("890"))        # (8,9) only → 1 (9→0 NOT valid)
    print(func("099"))        # (0,9)? no → 0
    print(func("009"))        # (0,0)? no, (0,9)? no → 0
    print(func("0123456789"))     # full increasing → 9
    print(func("123456789123456789"))  # repeated → 16
    print(func("a1b2c3d4e5f6g7h8i9"))  # no adjacent digits → 0
    print(func("xx12yy23zz34aa45"))    # (1,2),(2,3),(3,4),(4,5) → 4
    print(func("00"))         # same digits → 0
    print(func("01"))         # valid → 1
    print(func("10"))         # invalid → 0
    print(func("9"))          # single char → 0
    print(func("a"))          # non-digit → 0

if __name__ == "__main__":

    try:
        import py_pattern_tracker as reference_module
        run_tests(reference_module)
    except ImportError:
        print("Error: Could not find local 'py_pattern_tracker.py' to run standalone test.")
        sys.exit(1)
