"""
Given a string s containing only the characters'(', ')', '{', '}', '[', and ']', determine whether the
input string is valid

A string is considered valid if:
	-> Open brackets are closed by the same type of brackets
	-> Open brackets are closed in the correct order
	-> Every closing brackets has a corresponding opening bracket

Test:

- Valid cases
bracket_validator("()") # True
bracket_validator("()[]{}") # True
bracket_validator("{[()]}") # True
bracket_validator("") # True (empty string is valid)
bracket_validator("hello(hhhh)world{ho}w are") # True

- Invalid cases
bracket_validator("(]") # False
bracket_validator("([)]") # False
bracket_validator("(((") # False
bracket_validator("())") # False
bracket_validator("{[(])}") # False
"""

def bracket_validator(s: str) -> bool:
	stack = []
	peers = {')': '(', ']': '[', '}': '{'}
	for char in s:
		if char in "([{":
			stack.append(char)
		elif char in ")]}":
			if not stack or stack.pop() != peers[char]:
				return False
	return len(stack) == 0

def main() -> None:
	print(bracket_validator("()"))
	print(bracket_validator("()[]{}"))
	print(bracket_validator("{[()]}"))
	print(bracket_validator(""))
	print(bracket_validator("hello(hhhh)world{ho}w are"))
	print(bracket_validator("(]"))
	print(bracket_validator("([)]"))
	print(bracket_validator("((("))
	print(bracket_validator("())"))
	print(bracket_validator("{[(])}"))

if __name__ == "__main__":
	main()
