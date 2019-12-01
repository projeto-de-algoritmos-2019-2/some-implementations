from heapq import heappush, heappop

tasks = [
	('A', 1, 3),
	('B', 2, 3),
	('C', 4, 6),
	('D', 7, 8),
	('E', 3, 4),
	('F', 4, 5),
	('G', 5, 6),
]

tasks.sort(key=lambda tpl:tpl[1], reverse=True)

class MinHeap():
	def __init__(self):
		self.heap = []

	def push(self, val):
		heappush(self.heap, val)

	def pop(self):
		return heappop(self.heap)

	def top(self):
		return self.heap[0]

	def empty(self):
		return len(self.heap) == 0

	def size(self):
		return len(self.heap)

min_heap = MinHeap()
rooms = 0

while tasks:
	task, beg, end = tasks.pop()

	# if the next task starts after the last task ends, 
	# no new room needs to be allocated
	if min_heap.size() and beg >= min_heap.top()[0]:
		min_heap.pop()

	else:
		rooms += 1

	# the min heap should returns the time 
	# where the next task finishes
	min_heap.push((end, beg, task))

print(rooms)