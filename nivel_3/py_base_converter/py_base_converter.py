"""
Test:

- Basic convertions
convert_base("1010", 2, 10) # "10"
convert_base("10", 10, 2) # "1010"
convert_base("1A", 16, 10) # "26"
convert_base("26", 10, 16) # "1A"

- Same base
convert_base("123", 10, 10) # "123"

- Edge cases
convert_base("0", 10, 2) # "0"
convert_base("000", 2, 10) # "0"

- Larger bases
convert_base("ZZZ", 36, 10) # "46655"
convert_base("46655", 10, 36) # "ZZZ"

- Uppercase handling
convert_base("A", 16, 10) # "10"
convert_base("F", 16, 10) # "15"

- Mixed digits and letters
convert_base("1F4", 16, 10) # "500"
convert_base("500", 10, 16) # "1F4"

- Invalid cases
convert_base("2", 2, 10) # Error / invalid input
convert_base("G", 16, 10) # Error / invalid input
"""

def convert_base(number: str, src_base: int, dest_base: int):
	digit = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

	try:
		num = int(number, src_base)
		if num == 0:
			return "0"
		result = ""
		while num > 0:
			result = digit[num % dest_base] + result
			num //= dest_base
	except Exception:
		return "ERROR"
	return result

def main() -> None:
	print(convert_base("1010", 2, 10))
	print(convert_base("10", 10, 2))
	print(convert_base("1A", 16, 10))
	print(convert_base("26", 10, 16))

	print(convert_base("123", 10, 10))

	print(convert_base("0", 10, 2))
	print(convert_base("000", 2, 10))

	print(convert_base("ZZZ", 36, 10))
	print(convert_base("46655", 10, 36))

	print(convert_base("A", 16, 10))
	print(convert_base("F", 16, 10))

	print(convert_base("1F4", 16, 10))
	print(convert_base("500", 10, 16))

	print(convert_base("2", 2, 10))
	print(convert_base("G", 16, 10))

if __name__ == "__main__":
	main()


def base_convert(number: str, src_base: int, dest_base: int):
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
