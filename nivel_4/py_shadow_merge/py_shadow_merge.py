"""
Given two lists of integers 'list1' and 'list2', return a new list containing all elements from both lists, sorted in ascending order.

The function must:
	-> Combine all elements from both input list
	-> Handle empty or None lists correctly
	-> Return a new sorted list (ascending order)

Test:

answer = Solution()

-> Basic cases
print(answer.merge_list([1, 3, 5, -1], [0, 8, 2, 1]])
[-1, 0, 1, 1, 2, 3, 5, 8]

print(answer.merge_list([99, -22, 10, 9], []))
[-22, 9, 10, 99]

-> Both lists non-empty
print(answer.merge_list([4, 2], [1, 3]))
[1, 2, 3, 4]

-> One list in None
print(answer.merge_list(None, [5, 3, 1]))
[1, 3, 5]

print(answer.merge_list([7, 6, 8], None))
[6, 7, 8]

-> Edge cases
print(answer.merge_list([], []))
[]

print(answer.merge_list([1, 1, 1], [1, 1]))
[1, 1, 1, 1, 1]

print(answer.merge_list([-5, -2], [-3, -1]))
[-5, -3, -2, -1]
"""

def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
	list1 = list1 or []
	list2 = list2 or []

	mixer = list1 + list2
	mixer.sort()
	return mixer
	
	#return sorted(list1 + list2)

def main() -> None:
	print(shadow_merge([1, 3, 5, -1], [0, 8, 2, 1]))
	print(shadow_merge([99, -22, 10, 9], []))
	print(shadow_merge([4, 2], [1, 3]))
	print(shadow_merge(None, [5, 3, 1]))
	print(shadow_merge([7, 6, 8], None))
	print(shadow_merge([], []))
	print(shadow_merge([1, 1, 1], [1, 1]))
	print(shadow_merge([-5, -2], [-3, -1]))

if __name__ == "__main__":
	main()
