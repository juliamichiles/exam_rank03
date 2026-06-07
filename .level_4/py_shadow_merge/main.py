import sys


def run_tests(user_module) -> None:
    name = "shadow_merge"
    func = getattr(user_module, name, None)
    if not func:
        print(f"Error: Function '{name}' not found.")
        return
    
    print(func([1, 3, 5, -1], [0, 8, 2, 1]))        # basic mixed values
    print(func([99, -22, 10, 9], []))               # second empty
    print(func([4, 2], [1, 3]))                     # both unsorted
    print(func(None, [5, 3, 1]))                    # first None
    print(func([7, 6, 8], None))                    # second None
    print(func([], []))                             # both empty
    print(func([1, 1, 1], [1, 1]))                  # duplicates
    print(func([-5, -2], [-3, -1]))                 # negatives only
    
    print(func([0], [0]))                           # single elements equal
    print(func([1], []))                            # one element + empty
    print(func([], [2]))                            # empty + one element
    print(func(None, None))                         # both None
    
    print(func([5, 4, 3, 2, 1], [10, 9, 8, 7, 6]))  # reverse ordered lists
    print(func([1, 2, 3], [4, 5, 6]))               # already sorted input
    print(func([4, 5, 6], [1, 2, 3]))               # disjoint ranges
    
    print(func([-10, 0, 10], [-5, 5]))              # mix negative, zero, positive
    print(func([1000, -1000], [500, -500]))         # large magnitude values
    
    print(func([1, 2, 2, 3], [2, 3, 4]))            # overlapping duplicates
    print(func([0, 0, 0], [0, 0]))                  # all same values
    
    print(func(list(range(10)), list(range(10, 0, -1))))  # longer lists mixed order

if __name__ == "__main__":

    try:
        import py_shadow_merge as reference_module
        run_tests(reference_module)
    except ImportError:
        print("Error: Could not find local 'py_shadow_merge.py' to run standalone test.")
        sys.exit(1)
