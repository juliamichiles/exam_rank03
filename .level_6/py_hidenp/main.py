import sys


def run_tests(user_module) -> None:
    name = "hidenp"
    func = getattr(user_module, name, None)
    if not func:
        print(f"Error: Function '{name}' not found.")
        return
    print(func("abc", "axbycz"))          # True
    print(func("abc", "acb"))             # False (wrong order)
    print(func("abc", "aabbcc"))          # True
    print(func("abc", "ab"))              # False (missing 'c')
    print(func("", "qualquercoisa"))      # True (empty is subsequence)
    print(func("a", ""))                  # False
    
    print(func("ace", "abcde"))           # True
    print(func("aec", "abcde"))           # False (order wrong)
    print(func("aaa", "aaabbb"))          # True
    print(func("aaaa", "aaabbb"))         # False (not enough 'a')
    
    print(func("123", "1a2b3c"))          # True
    print(func("135", "12345"))           # True
    print(func("531", "12345"))           # False
    
    print(func("!@#", "!!@@##"))          # True
    print(func("!@#", "!#@"))             # False
    
    print(func("long", "loooooong"))      # True
    print(func("longer", "loooooong"))    # False
    
    print(func("abc", "ABC"))             # False (case-sensitive)
    print(func("AbC", "AxxbxxC"))         # False (case mismatch on 'b')
    
    print(func("a b", "a--- ---b"))       # True (spaces count)
    print(func("ab", "a b"))              # True
    
    print(func("z", "abc"))               # False
    print(func("abc", "abc"))             # True (exact match)

if __name__ == "__main__":

    try:
        import py_hidenp as reference_module
        run_tests(reference_module)
    except ImportError:
        print("Error: Could not find local 'py_hidenp.py' to run standalone test.")
        sys.exit(1)
