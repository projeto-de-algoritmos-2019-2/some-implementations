arr = [7, 4, 18, -6, 1, 12, 14, 28, 19]

def median(arr, k):

	set_left = []
	set_right = []

	for elem in arr:
		if elem == arr[0]:
			continue

		if elem > arr[0]:
			set_right.append(elem)
		
		else:
			set_left.append(elem)

	if len(set_left) == k:
		return arr[0]

	if len(set_left) > k:
		return median(set_left, k)

	else:
		new_median_position = k - len(set_left) - 1
		return median(set_right, new_median_position)

median_pos = len(arr)//2

print(median(arr, median_pos))
