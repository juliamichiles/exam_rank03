import sys


def run_tests(user_module) -> None:
    name = "anagram"
    func = getattr(user_module, name, None)
    if not func:
        print(f"Error: Function '{name}' not found.")
        return
    
    print(func("racecar", "carrace"))     # True
    print(func("racecar", "carace"))      # False
    print(func("abc", "bca"))             # True
    print(func("abc", "abcd"))            # False

    print(func("", ""))                   # True (both empty)
    print(func("a", "a"))                 # True
    print(func("a", "b"))                 # False
    print(func("", "a"))                  # False

    print(func("aabbcc", "abcabc"))       # True
    print(func("aabbcc", "aabbc"))        # False
    print(func("aaabbb", "ababab"))       # True
    print(func("aaabbb", "ab"))           # False

    print(func("abc", "ABC"))             # False (case-sensitive)
    print(func("Abc", "cba"))             # False
    print(func("Abc", "cbA"))             # True

    print(func("a b c", "abc"))           # False (space matters)
    print(func("a b c", "c b a"))         # True
    print(func("!@#", "#@!"))             # True
    print(func("!@#", "#@"))              # False

    print(func("listen", "silent"))       # True
    print(func("triangle", "integral"))   # True
    print(func("apple", "papel"))         # True
    print(func("apple", "appeal"))        # False

    print(func("aaa", "aaaa"))            # False
    print(func("abcd", "abce"))           # False
    print(func("aabb", "bbaa"))           # True
    print(func("aabb", "bbba"))           # False

    print(func("abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba"))  # True
    print(func("abcdefghijklmnopqrstuvwxy", "zyxwvutsrqponmlkjihgfedcba"))   # False


if __name__ == "__main__":

    try:
        import py_anagram as reference_module
        run_tests(reference_module)
    except ImportError:
        print("Error: Could not find local 'py_anagram.py' to run standalone test.")
        sys.exit(1)
