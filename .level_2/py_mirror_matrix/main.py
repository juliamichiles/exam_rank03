def run_tests(user_module) -> None:
    name = "reverse_matrix"
    func = getattr(user_module, name, None)
    if not func:
        print(f"Error: Function '{name}' not found.")
        return
    
    print(func([[1, 2], [3, 4]]))
    print(func([[1, 2, 3], [4, 5, 6]]))
    print(func([[1], [2], [3]]))
    print(func([[1]]))
    print(func([]))
    print(func([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


if __name__ == "__main__":
    try:
        import py_mirror_matrix as reference_module
        run_tests(reference_module)
    except ImportError:
        print("Error: Could not find local 'py_mirror_matrix.py' to run standalone test.")
        sys.exit(1)
