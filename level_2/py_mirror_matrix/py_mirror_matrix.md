"""
Given a 2D matrix s (list of lists), return a new matrix where each row is reversed individually.

The function must:
-> Reverse the order of elements inside each row
-> Keep the row order unchanged
-> Preserve the original dimensions of the matrix
-> Return a new matrix with modified rows

Test:

-> Basic test
reverse_matrix([[1, 2], [3, 4]])
[[2, 1], [4, 3]]

reverse_matrix([[1, 2, 3], [4, 5, 6]])
[3, 2, 1], [6, 5, 4]]

-> Single column
reverse_matrix([[1], [2], [3]])
[[1], [2], [3]]

-> Edge cases
reverse_matrix([[1]])
[[1]]

reverse_matrix([])
[]

-> Larger matrix
reverse_matrix([
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
])
[[3, 2, 1], [6, 5, 4], [9, 8, 7]]
"""
