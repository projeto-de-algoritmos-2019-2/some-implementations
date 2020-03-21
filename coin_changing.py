from collections import Counter

coins = [
	1,
	5,
	10,
	25,
	50,
	100
]

value = int(input())
change = []

coins.sort()

i = -1

while value:

	if coins[i] > value:
		i -= 1
		continue

	change.append(coins[i])
	value -= coins[i]

change  = dict(Counter(change))

print(change)
