"""
The function must:
	-> Sort strings by the number of vowels (ascending)
	-> If equal, sort by string length (ascending)
	-> If still equal, sort lexicographically (alphabetically)
	-> Vowels are: a, e, i, o, u (case-insensitive)

Test:

- Basic cases
print(sort_string(["apple", "bat", "car", "ae", "b"])) 
['b', 'ae', 'bat', 'car', 'apple']

- Same vowel count, different lengths
print(sort_string(["dog", "cat", "hi", "a"]))
['a', 'hi', 'cat', 'dog']

- Same vowel count and length -> lexicographical order
print(sort_string(["bat", "cat", "ant"]))
['ant', 'bat', 'cat']

- Mixed uppercase and lowercase
print(sort_string(["Apple", "banana", "Kiwi", "grape"]))
sorted by vowel count (case-insensitive)

- Edge cases
print(sort_string([]))
[]

print(sort_string(["a", "e", "i", "o", "u"]))
['a', 'e', 'i', 'o', 'u']

print(sort_string(["bbb", "ccc", "ddd"]))
['bbb', 'ccc', 'ddd'] (no vowels, same length -> lex order)
"""

def sort_string(str_list: list[str]) -> list[str]:
	def is_vowel(c):
 		return c.lower() in 'aeiou'
	def key_func(s):
		length = len(s)
		vowel_count = sum(1 for c in s if is_vowel(c))
		return (vowel_count, length, s.lower())
	return sorted(str_list, key=key_func)

def main() -> None:
	print(sort_string(["apple", "bat", "car", "ae", "b"]))
	print(sort_string(["dog", "cat", "hi", "a"]))
	print(sort_string(["bat", "cat", "ant"]))
	print(sort_string(["Apple", "banana", "Kiwi", "grape"]))
	print(sort_string([]))
	print(sort_string(["a", "e", "i", "o", "u"]))
	print(sort_string(["bbb", "ccc", "ddd"]))

if __name__ == "__main__":
	main()


def sort_string(str_list: list[str]) -> list[str]:
	vogal = "aAeEiIoOuU"
	def key_func(s):
		length = len(s)
		vogal_count = sum(1 for c in s if c in vogal)
		return (vogal_count, length, s.lower())
	return sorted(str_list, key=key_func)

