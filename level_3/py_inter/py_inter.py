"""
Returns a string containing the characters that appear in both strings, without repetitions.

The characters are added in the order they appear in the first string.
"""

def inter(s1, s2):
	result = ""
	for char in s1:
		if char in s2 and char not in result:
			result += char
	return result
