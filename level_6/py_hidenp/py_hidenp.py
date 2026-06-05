"""
Checks if the string 'small' is a subsequence of the string 'big'.

A subsequence means that all the characters of 'small' appear in 'big'
in the same order, but they don't necessarily have to be together.
"""

def hidenp(small, big):
	it = iter(big)
	return all(c in it for c in small)


print(hidenp("abc", "axbycz"))
print(hidenp("abc", "acb"))
print(hidenp("abc", "aabbcc"))
print(hidenp("abc", "ab"))
print(hidenp("", "qualquercoisa"))
print(hidenp("a", ""))

