tasks = [
	('A', 1, 3),
	('B', 2, 3),
	('C', 4, 6),
	('D', 7, 8),
	('E', 3, 4),
	('F', 4, 5),
	('G', 5, 6),
]

tasks.sort(key=lambda tpl:tpl[2], reverse=True)

done = []

while tasks:
	task = tasks.pop()
	done.append(task)

	# remove all tasks that starts before the last
	# added task finishes
	while tasks and tasks[-1][1] < done[-1][2]:
		tasks.pop()

print(done)
