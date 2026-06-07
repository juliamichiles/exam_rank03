import sys


def run_tests(user_module) -> None:
    name = "twister"
    func = getattr(user_module, name, None)
    if not func:
        print(f"Error: Function '{name}' not found.")
        return
    print(func([1, 2, 3, 4, 5], 2))        # basic right rotation
    print(func([4, 2, 1, -1, 'a'], 4))     # mixed types
    print(func([1, 2, 3], 3))              # rotation == length
    print(func([1, 2, 3], 5))              # rotation > length
    print(func([1, 2, 3, 4], -1))          # left rotation
    print(func([], 3))                     # empty list
    print(func([1], 10))                   # single element
    
    print(func([1, 2, 3, 4, 5], 0))        # zero rotation
    print(func([1, 2, 3, 4, 5], 1))        # rotate by 1
    print(func([1, 2, 3, 4, 5], -2))       # left rotation by 2
    
    print(func([10, 20, 30, 40], 8))       # multiple full rotations
    print(func([10, 20, 30, 40], -8))      # negative multiple rotations
    
    print(func([1, 2, 3, 4], 6))           # > length, not multiple
    print(func([1, 2, 3, 4], -6))          # negative > length
    
    print(func(['a', 'b', 'c', 'd'], 2))   # all strings
    print(func([True, False, True], 1))    # booleans
    
    print(func([1, 2, 3, 4, 5, 6], 3))     # even length split
    print(func([1, 2, 3, 4, 5], 7))        # odd length, large n
    
    print(func([0, 0, 0, 0], 2))           # all same values
    print(func([-1, -2, -3, -4], 1))       # all negatives
    

if __name__ == "__main__":

    try:
        import py_twist_sequence as reference_module
        run_tests(reference_module)
    except ImportError:
        print("Error: Could not find local 'py_twist_sequence.py' to run standalone test.")
        sys.exit(1)
