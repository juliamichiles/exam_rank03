#bracket
def ():
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
def ():
	vogais = "aAeEiIoOuU"
	def key_func(s):
		length = len(s)
		vogal_count = sum(1 for c in s if c in vogais)
		return (length, s.lower(), vogal_count)
	return sorted(str_list, key= key_func)

#palindrome
def ():
	clean = ''.join(c.lower() for c in s if c.isalnum())
	return clean == clean[::-1] 

#convert base
def ():
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
def ():
	return [e[::-1] for e in s]

#shadow merge
def (): 
	list1 = list1 or []
	list2 = list2 or []
	mixed = list1 + list2
	mixed.sort()
	return mixed

#patter tracker
def ():
	count = 0
	for i in range(len(s) - 1):
		if s[i].isdigit() and s[i + 1].isdigit() and s[i + 1] > s[i] and int(s[i + 1]) == int(s[i] + 1):
			count += 1
	return count

#twister
def ():
	if n < 0:
		count = -n
	else:
		count = len(arr) - n
	list1 = arr[count:]
	list2 = arr[:count]
	return list1 + list2

#wis 
def ():
	result = ""
	for i in s:
		if 'a' <= i <= 'z':
			result += chr((ord(i) - ord('a') + n) % 26 + ord('a'))
		elif 'A' <= i <= 'Z':
			result += chr((ord(i) - ord('A') + n) % 26 + ord('A'))
		else:
			result += i
	return result 

#anagram
def ():
	if len(s) != len(t):
		return False
	return sorted(s) == sorted(t)

#sculpter
def ():
	result = ""
	p = True
	count = 0
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
#hiden
def ():
	it = iter(big)
	return all(c in it for c in small)

#inter








#brackets
def ():
	stack = []
	peers = {')': '(', ']': '[', '}': '{'}
	for char in s:
		if char in "([{":
			stack.append(char)
		elif char in ")]}":
			if not stack or stack.pop() != peers[char]:
				return False 
	return len(stack) == 0

#vogal
def ():
	vogal = "aAeEiIoOuU"
	def key_func(s):
		length = len(s)
		vogal_count = sum(1 for c in s if c in vogal)
		return (lenght, s.lower(), vogal_count)
	return sorted(str_list, key=key_func)

#palindrome
def ():
	clean = ''.join(c.lower() for c in s if c.isalnum())
	return clean == clean[::-1]

#mirror 
def():
	return [e[::-1]for e in s]

#shadom
def():
	list1 = list1 or []
	list2 = list2 or []
	mixed = list1 + list2
	mixed.sort()
	return mixed

#patter
def():
	count = 0
	for i in range(len(s) - 1):
		if s[i].isdigit() and s[i + 1].isdigit() and s[i+ 1] > s[i] and int(s[i + 1]) == int(s[i] + 1):
			count += 1
	return count

#base
def ():
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

#twister
def():
	if n < 0:
		count = -n
	else:
		count = len(arr) - n
	list1 = arr[count:]
	list2 = arr[:count]
	return list1 + list2

#wis
def():
	result = ""
	for i in s:
		if 'a' <= i <= 'z':
			result += chr((ord(i) - ord('a') + n) % 26 + ord('a'))
		elif 'A' <= i <= 'Z':
			result += chr((ord(i) - ord('A') + n) % 26 + ord('A'))
		else:
			result += i
	return result

#sculpter
def():
	p = True
	result = ""
	count = 0
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

#anagram 
def ():
	if len(s) != len(t):
		return False
	return sorted(s) == sorted(t)












































