def run_tests(user_module) -> None:

    name = "py_cryptic_sorter" 
    func = getattr(user_module, name, None)
    if not func:
        print(f"Error: Function '{name}' not found.")
        return

    print(func(["apple", "bat", "car", "ae", "b"]))
    print(func(["dog", "cat", "hi", "a"]))
    print(func(["bat", "cat", "ant"]))
    print(func(["Apple", "banana", "Kiwi", "grape"]))
    print(func([]))
    print(func(["a", "e", "i", "o", "u"]))
    print(func(["bbb", "ccc", "ddd"]))


if __name__ == "__main__":
    
    try:
        import py_cryptic_sorter as reference_module
        run_tests(reference_module)
    except ImportError:
        print("Error: Could not find local 'py_cryptic_sorter.py' to run standalone test.")
        sys.exit(1)
