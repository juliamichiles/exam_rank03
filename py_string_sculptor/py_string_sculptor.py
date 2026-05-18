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
print(sculptor("Hw+ello, world!"))
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
	
