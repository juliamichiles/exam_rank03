import sys


def run_tests(user_module) -> None:
    name = "sculptor"
    func = getattr(user_module, name, None)
    if not func:
        print(f"Error: Function '{name}' not found.")
        return
    print(func("Hello world"))            # "hElLo WoRlD"
    print(func("Hello, world!"))          # "hElLo, WoRlD!"
    print(func("123abcDEF"))              # "123aBcDeF"
    print(func("a-bC-dEf-ghIj"))          # "a-Bc-DeF-gHiJ"
    
    print(func(""))                       # ""
    print(func("12345"))                  # "12345"
    print(func("A"))                      # "a"
    print(func("ab"))                     # "aB"
    
    print(func("ABCDEF"))                 # "aBcDeF"
    print(func("abcdef"))                 # "aBcDeF"
    print(func("aBcDeF"))                 # "aBcDeF"
    
    print(func("a1b2c3d4"))               # "a1B2c3D4"
    print(func("!@#a$b%c^"))              # "!@#a$B%c^"
    print(func("   abc   def   "))        # "   aBc   DeF   "
    
    print(func("ZzZzZz"))                 # "zZzZzZ"
    print(func("Python3.8!"))             # "pYtHoN3.8!"
    print(func("x"))                      # "x"
    print(func("xy"))                     # "xY"
    print(func("xYz"))                    # "xYz"
    
    print(func("longstringwithonlyletters"))  # alternating long alpha string
    print(func("mixED CaSe WITH 123 NUM83R5")) # mixed real-world stringi


if __name__ == "__main__":

    try:
        import py_string_sculptor as reference_module
        run_tests(reference_module)
    except ImportError:
        print("Error: Could not find local 'py_string_sculptor.py' to run standalone test.")
        sys.exit(1)
