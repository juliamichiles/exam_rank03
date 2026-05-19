"""
Given a string 's', count the number of times two consecutive characters are digits such that the seconddigit is exactly one greater than the first.

The function must:
	-> Only consider adjacent characters in the string
	-> Count pairs where both are digits
	-> Increment count if int(s[i]) == int(s[i-1]) + 1
	-> Return the total count of such valid consecutive pairs

Test: 

-> Basic cases
print(pattern_tracker("123a345"))
4 -> (1, 2), (2, 3), (3, 4), (4, 5)

print(pattern_tracker("1a2b3c4d5"))
0 -> no adjacent digits

-> Mixed complex case
print(pattern_tracker("12asd34hkh45kjhj56jhj67kjhjh78kjhjh89kjhkhj110"))
counts valid pairs like (1, 2), (3, 4), ..., (8, 9)

-> Egde cases
print(pattern_tracker(""))
0

print(pattern_tracker("7"))
0

print(answer.pattern_tracker("111111"))
0 -> no increasing sequence

print(pattern_tracker("012345"))
5 -> (0, 1), (1, 2), (2, 3), (3, 4), (4, 5)

print(pattern_tracker("98"))
0 -> decreasing, not counted
"""

def pattern_tracker(s: str) -> int:
	count = 0
	for i in range(len(s) -1):
		if s[i].isdigit() and s[i + 1].isdigit() and s[i + 1] > s[i]:
			count += 1
	return count

def main() -> None:
	print(pattern_tracker("123a345"))
	print(pattern_tracker("1a2b3c4d5"))
	print(pattern_tracker("12asd34hkh45kjhj56jhj67kjhjh78kjhjh89kjhkhj110"))
	print(pattern_tracker(""))
	print(pattern_tracker("7"))
	print(pattern_tracker("111111"))
	print(pattern_tracker("012345"))
	print(pattern_tracker("98"))

if __name__ == "__main__":
	main()


def patter_tracker(s: str) -> int:
	count = 0
	for i in range(len(s) - 1):
		if s[i].isdigit() and s[i + 1].isdigit() and s[i + 1] > s[i]:
			count += 1
	return count
