tasks = [
	# (label, time_needed, deadline),
	('A', 3, 6),
	('B', 1, 8),
	('C', 5, 5),
	('D', 3, 4),
	('E', 5, 9),
	('F', 2, 4),
	('G', 2, 2),
	('H', 4, 7),
]

tasks.sort(key=lambda x : x[2], reverse=True)

lateness = 0
at = 0

while tasks:
	label, time_needed, deadline = tasks.pop()

	at = at + time_needed

	if at > deadline:
		lateness += (at - deadline)

	# print((label, time_needed, deadline))
	# print('at', at)
	# print('lateness', lateness)
	# input()

print('lateness', lateness)