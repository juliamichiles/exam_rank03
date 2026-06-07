import sys


def run_tests(user_module) -> None:
    name = "convert_base"
    func = getattr(user_module, name, None)
    if not func:
        print(f"Error: Function '{name}' not found.")
        return
    print(func("1010", 2, 10))
    print(func("10", 10, 2))
    print(func("1A", 16, 10))
    print(func("26", 10, 16))

    print(func("123", 10, 10))

    print(func("0", 10, 2))
    print(func("000", 2, 10))

    print(func("ZZZ", 36, 10))
    print(func("46655", 10, 36))

    print(func("A", 16, 10))
    print(func("F", 16, 10))

    print(func("1F4", 16, 10))
    print(func("500", 10, 16))

    print(func("2", 2, 10))
    print(func("G", 16, 10))


if __name__ == "__main__":

    try:
        import py_base_converter as reference_module
        run_tests(reference_module)
    except ImportError:
        print("Error: Could not find local 'py_base_converter.py' to run standalone test.")
        sys.exit(1)
