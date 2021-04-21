# Python3 program for the above approach

# Function to find the last element
# remaining in the array after
# performing the given operations
def printLastElement(arr, N):

	# Checks if traversal is from
	# left to right or vice versa
	leftTurn = True

	# Store the elements currently
	# present in the array
	remainElements = N

	# Store the distance between 2
	# consecutive array elements
	step = 1

	# Store the first element
	# of the remaining array
	head = 1

	# Iterate while elements
	# are greater than 1
	while (remainElements > 1):

		# If left to right turn
		if (leftTurn):

			# Update head
			head = head + step

		# Otherwise, check if the
		# remaining elements are odd
		else:

			# If true, update head
			if (remainElements % 2 == 1):
				head = head + step

		# Eleminate half of the array elements
		remainElements = remainElements // 2

		# Double the steps after each turn
		step = step * 2

		# Alter the turn
		leftTurn = not leftTurn

	# Print the remaining element
	print(arr[head - 1])


# Driver Code
if __name__ == "__main__":

	arr = [ 2, 3, 5, 6 ]
	N = len(arr)

	printLastElement(arr, N)

# This code is made by 'naman_d0shi'
