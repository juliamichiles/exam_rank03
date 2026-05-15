"""
Given a string 's', determine whether it is a palindrome.
A string is considered a palindrome if it reads the same forward and backard

The function must:
	-> Ignore case differences (A == a)
	-> Ignore non-alphanumeric characters
	-> Return True if 's' is a palindrome, otherwise False

Test:

-> Valid cases
is_palindrome("madam") #True
is_palindrome("racecar") #True
is_palindrome("A man, a plan, a canal: Panama") #True
is_palindrome("No 'x' in Nixon") #True
is_palindrome("") #True
is_palindrome("a") #True

-> Invalid cases
is_palindrome("hello") #False
is_palindrome("python") #False
is_palindrome("OpenAI") #False

-> Edge cases
is_palindrome("12321") #True
is_palindrome("12345") #False
is_palindrome("Able was I ere I saw Elba") #True
"""

def is_palindrome(s: str) -> bool:
	clean = ''.join(c.lower() for c in s if c.isalnum())
	return clean == clean[::-1]

def main() -> None:
	print(is_palindrome("madam"))
	print(is_palindrome("racecar"))
	print(is_palindrome("A man, a plan, a canal: Panama"))
	print(is_palindrome("No 'x' in Nixon"))
	print(is_palindrome(""))
	print(is_palindrome("a"))

	print(is_palindrome("hello"))
	print(is_palindrome("python"))
	print(is_palindrome("OpenAI"))

	print(is_palindrome("12321"))
	print(is_palindrome("12345"))
	print(is_palindrome("Able was I ere I saw Elba"))

if __name__ == "__main__":
	main()
