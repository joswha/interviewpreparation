#   "array": [5, 1, 22, 25, 6, -1, 8, 10],
#   "sequence": [1, 6, -1, 10]

def isValidSubsequence(array, sequence):
	j = 0
	n = len(sequence)
	for elem in array:
		if j >= n:
			break
		if sequence[j] == elem:
			j += 1
	return (len(sequence) == j)