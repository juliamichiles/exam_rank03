"""
Given a string 'text', return a new string where alphabetic characters alternate between lowrcase and uppercase

The function must:
	-> Start with lowercase for the first alphabetic character
	-> Alternate case for each subsequent alphabetic character
	-> Ignore non-alphabetic characters(they remain unchanged)
	-> Non-alphabetic characters do NOT affect the alternation

Test:

-> Basic case
print(sculptor("Hello world"))
"hElLo WoRlD"

-> With punctuation
print(sculptor("Hello, world!"))
"hElLo, WoRlD!"

-> With numbers
print(sculptor("123abcDEF"))
"123aBcDeF"

-> Mixed characters
print(sculptor("a-bC-dEf-ghIj"))
"a-Bc-DeF-gHiJ"

-> Edge cases
print(sculptor(""))
""

print(sculptor("12345"))
"12345"

print(sculptor("A"))
"a"

print(sculptor("ab"))
"aB"
"""

def sculptor(text: str) -> str:
	result = ""
	count = 0
	p = True
	while count < len(text):
		if text[count].isalpha():
			if p:
				result += text[count].lower()
			else:
				result += text[count].upper()
			p = not p
		else:
			result += text[count]
		count += 1
	return result

def main() -> None:
    print(sculptor("Hello, world!"))
    print(sculptor("123abcDEF"))
    print(sculptor("a-bC-dEf-ghIj"))
    print(sculptor(""))
    print(sculptor("12345"))
    print(sculptor("A"))
    print(sculptor("ab"))

if __name__ == "__main__":
    main()

