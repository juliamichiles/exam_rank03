import sys


def run_tests(user_module) -> None:
    name = "shift_alphabet"
    func = getattr(user_module, name, None)
    if not func:
        print(f"Error: Function '{name}' not found.")
        return
    print(func("abz", 1))            # "bca"
    print(func("AbZ", 1))            # "BcA"
    print(func("Hello World!", 3))   # "Khoor Zruog!"
    print(func("bca", -1))           # "abz"
    print(func("abc", 26))           # "abc"
    print(func("xyz", 3))            # "abc"
    print(func("Python 3.8!", 5))    # "Udymts 3.8!"
    print(func("", 10))              # ""
    print(func("12345", 4))          # "12345"
    
    print(func("abc", 52))           # full double rotation → "abc"
    print(func("abc", 27))           # 27 == 1 → "bcd"
    print(func("abc", -27))          # -27 == -1 → "zab"
    
    print(func("zzz", 1))            # wrap → "aaa"
    print(func("AAA", 1))            # wrap uppercase → "BBB"
    print(func("ZzZz", 2))           # mixed wrap → "BbBb"
    
    print(func("aBcDeF", 2))         # preserve case → "cDeFgH"
    print(func("aBcDeF", -2))        # negative shift → "yZaBcD"
    
    print(func("!@#abcXYZ", 3))      # symbols unchanged → "!@#defABC"
    print(func("   abc   ", 1))      # spaces preserved → "   bcd   "
    
    print(func("The quick brown fox jumps over the lazy dog", 10))
    # pangram test
    
    print(func("MixedCASEwith123Numbers!", 4))
    # realistic mixed string
    
    print(func("x", 1))              # "y"
    print(func("y", 2))              # wrap → "a"
    print(func("A", -1))             # wrap → "Z"

if __name__ == "__main__":

    try:
        import py_whisper_cipher as reference_module
        run_tests(reference_module)
    except ImportError:
        print("Error: Could not find local 'py_whisper_cipher.py' to run standalone test.")
        sys.exit(1)
