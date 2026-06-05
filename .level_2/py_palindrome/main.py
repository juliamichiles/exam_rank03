def run_tests(user_module) -> None:
    name = "is_palindrome"
    func = getattr(user_module, name, None)
    if not func:
        print(f"Error: Function '{name}' not found.")
        return
    print(func("madam"))
    print(func("racecar"))
    print(func("A man, a plan, a canal: Panama"))
    print(func("No 'x' in Nixon"))
    print(func(""))
    print(func("a"))

    print(func("hello"))
    print(func("python"))
    print(func("PaintingHi"))

    print(func("12321"))
    print(func("12345"))
    print(func("Able was I ere I saw Elba"))


if __name__ == "__main__":
    try:
        import py_palindrome as reference_module
        run_tests(reference_module)
    except ImportError:
        print("Error: Could not find local 'py_palindrome.py' to run standalone test.")
        sys.exit(1)
