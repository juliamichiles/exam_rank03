"""
Given a strig 's' and an integer 'n', shift each alphabetic character in the string by 'n' positions in the alphabet

The function must:
	-> Preserve case (lowercase and uppercase separately)
	-> Wrap around the alphabet (e.g., 'z' -> 'a')
	-> Leave non-alphabetic characters unchanged
	-> Support positive and negative shifts

Test:

-> Basic cases
print(shift_alphabet("abz", 1))
"bca"

print(shift_alphabet("AbZ", 1))
"BcA"

-> With spaces and punctuation
print(shift_alphabet("Hello World!", 3))
"Khoor Zruog!"

-> Negative shift
print(shift_alphabet("bca", -1))
"abz

-> Large shift (wrap around)
print(shift_alphabet("abc", 26))
"abc"

print(shift_alphabet("xyz", 3))
"abc"

-> Mixed characters
print(shift_alphabet("Python 3.8!", 5))
"Udymts 3.8!"

-> Edge cases
print(shift_alphabet("", 10))
""

print(shift_alphabet("12345", 4))
"12345"
"""

def shift_alphabet(s: str, n: int) -> str:
	result = ""
	for i in s:
		if 'a' <= i <= 'z':
			result += chr((ord(i) - ord('a') + n) % 26 + ord('a'))
		elif 'A' <= i <= 'Z':
			result += chr((ord(i) - ord('A') + n) % 26 + ord('A'))
		else:
			result += i
	return result

def main() -> None:
	print(shift_alphabet("abz", 1))
	print(shift_alphabet("AbZ", 1))
	print(shift_alphabet("Hello World!", 3))
	print(shift_alphabet("bca", -1))
	print(shift_alphabet("abc", 26))
	print(shift_alphabet("xyz", 3))
	print(shift_alphabet("Python 3.8!", 5))
	print(shift_alphabet("", 10))
	print(shift_alphabet("12345", 4))

if __name__ == "__main__":
	main()
