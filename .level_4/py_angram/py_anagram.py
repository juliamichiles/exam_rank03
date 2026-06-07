"""
Check if two strings are anagrams

Given two strings s and t, return true if t is an anagram of s, and false otherwise.
Two strings are anagrams if they contain the same characters with the same frequency.

Test:
 - print(Anagram("racecar","carrace")) --> True
 - print(Anagram("racecar","carace")) --> False
 - print(Anagram("Conversation","Voices rant on")) --> False
"""

def anagram(s: str, t: str) -> bool:
	if len(s) != len(t):
		return False
	return sorted(s) == sorted(t)

if __name__ == "__main__":
	result1 = anagram("racecar","carrace")
	result2 = anagram("racecar","carace")
	result3 = anagram("Conversation","Voices rant on")

	print(result1)
	print(result2)
	print(result3) 
