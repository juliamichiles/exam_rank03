#bracket

def bracket_validatos(s: str) -> bool:
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

def sort_str(str_list: list[str]) -> list[str]:
	vogal = "aAeEiIoOuU"
	def key_func(s):
		length = len(s)
		vogal_count = sum(1 for c in s if c in vogal)
		return (vogal_count, length, s.lower())
	return sorted(str_list, key=key_func)
