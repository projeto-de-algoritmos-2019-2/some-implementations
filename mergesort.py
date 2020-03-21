
def merge(left, right):
	
	sorted_arr = []
	i, j = 0, 0

	while i < len(left) and j < len(right):

		if left[i] <= right[j]:
			sorted_arr.append(left[i])
			i += 1

		else:
			sorted_arr.append(right[j])
			j += 1

	while i < len(left):
		sorted_arr.append(left[i])
		i += 1

	while j < len(right):
		sorted_arr.append(right[j])
		j += 1

	print(left, right)
	print(sorted_arr)
	print()

	return sorted_arr

def mergesort(arr):

	if(len(arr) == 1):
		return arr

	mid = len(arr) // 2

	left = arr[:mid]
	left = mergesort(left)

	right = arr[mid:]
	right = mergesort(right)

	return merge(left, right)

def main():
	arr = [8, 2, 1, 5, 2, 6, 4, 3, 10]

	sorted_arr = mergesort(arr)

main()