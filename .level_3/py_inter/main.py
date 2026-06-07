import sys


def run_tests(user_module) -> None:
    name = "inter"
    func = getattr(user_module, name, None)
    if not func:
        print(f"Error: Function '{name}' not found.")
        return

    print(func("abc", "abc"))          # same strings → "abc"
    print(func("abc", "cba"))          # order should follow s1 → "abc"
    print(func("abc", "def"))          # no common chars → ""
    print(func("", "abc"))             # empty s1 → ""
    print(func("abc", ""))             # empty s2 → ""
    print(func("", ""))                # both empty → ""

    print(func("aabbcc", "abc"))       # duplicates in s1 → "abc"
    print(func("abc", "aabbcc"))       # duplicates in s2 → "abc"
    print(func("abacabad", "bda"))     # mixed duplicates → "abd"

    print(func("12345", "54321"))      # numbers → "12345"
    print(func("!@#abc", "abc$%^"))    # symbols + letters → "abc"

    print(func("hello", "world"))      # common letters → "lo"
    print(func("aaaaa", "a"))          # repeated single char → "a"

    print(func("ABC", "abc"))          # case-sensitive → ""
    print(func("AbC", "abcC"))         # mixed case → "bC" (depending on logic)

    print(func("abc", "abc"))          # same strings → "abc"
    print(func("abc", "cba"))          # order should follow s1 → "abc"
    print(func("abc", "def"))          # no common chars → ""
    print(func("", "abc"))             # empty s1 → ""
    print(func("abc", ""))             # empty s2 → ""
    print(func("", ""))                # both empty → ""

    print(func("aabbcc", "abc"))       # duplicates in s1 → "abc"
    print(func("abc", "aabbcc"))       # duplicates in s2 → "abc"
    print(func("abacabad", "bda"))     # mixed duplicates → "abd"

    print(func("12345", "54321"))      # numbers → "12345"
    print(func("!@#abc", "abc$%^"))    # symbols + letters → "abc"

    print(func("hello", "world"))      # common letters → "lo"
    print(func("aaaaa", "a"))          # repeated single char → "a"

    print(func("ABC", "abc"))          # case-sensitive → ""
    print(func("AbC", "abcC"))         # mixed case → "bC" (depending on logic)


if __name__ == "__main__":

    try:
        import py_inter as reference_module
        run_tests(reference_module)
    except ImportError:
        print("Error: Could not find local 'py_inter.py' to run standalone test.")
        sys.exit(1)
