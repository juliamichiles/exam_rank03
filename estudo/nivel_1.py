#bracket
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

#cryptic
def sort_string(str_list: list[str]) -> list[str]:
	vogal = "aAeEiIoOuU"
	def key_func(s):
		length = len(s)
		vogal_count = sum( 1 for c in s if c in vogal)
		return (vogal_count, length, s.lower())
	return sorted(str_list, key=key_func)

#palindrome
def is_palindrome(s: str) -> bool:
	clean = ''.join(c.lower() for c in s if c.isalnum())
	return clean == clean[::-1]

#convert base
def convert_base(number: str, src_base: int, dest_base: int):
	digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	try:
		num = int(number, src_base)
		if num == 0:
			return "0"
		result = ""
		while num > 0:
			result = digits[num % dest_base] + result
			num //= dest_base
	except Exception:
		return "ERROR"
	return result

#mirror reverse
def mirror_matrix(s: list[list[int]]) -> list[list[int]]
	return [e[::-1] for e in s]

#shadow merge
def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
	list1 = list1 or []
	list2 = list2 or []
	mixed = list1 + list2
	mixed.sort()
	return mixed

#patter tracker
def patter(s: str) -> int:
	count = 0 
	if s[i].isdigit() and s[i + 1].isdigit() and s[i + 1] > s[i]:
		count += 1
	return count
#twister
def twister(nums: list[int], n: int) -> list[int]:
	if n < 0:
		count = -n 
	else:
		count = len(nums) - n
	list1 = [count:]
	list2 = [:count]
