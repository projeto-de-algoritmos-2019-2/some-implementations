from heapq import heappush, heappop
from collections import defaultdict

edges = [
	['A', 'B', 1],
	['A', 'C', 3],
	['A', 'D', 2],

	['B', 'A', 1],
	['B', 'C', 2],

	['C', 'B', 2],
	['C', 'A', 3],
	['C', 'D', 1],

	['D', 'A', 2],
	['D', 'C', 1],
]

def prim(edges):
	
	adj_list = defaultdict(lambda:[])

	for u, v, w in edges:
		adj_list[u].append((v, w))

	class min_heap():
		def __init__(self):
			self.heap = []

		def push(self, val):
			heappush(self.heap, val)

		def pop(self):
			return heappop(self.heap)

	visited = set()
	heap = min_heap()
	path = list() # answer
	dist = defaultdict(lambda: float('inf'))
	parent = defaultdict(lambda: None)

	for k in adj_list:
		heap.push((float('inf'), k))

	while len(path) < len(adj_list) - 1:
		
		_, node = heap.pop()

		if node in visited:
			continue

		visited.add(node)

		if parent[node]:
			path.append(parent[node])

		for v, w in adj_list[node]:

			heap.push((w, v))

			if dist[v] > w:
				dist[v] = w
				parent[v] = str(node) + str(v)

	print(path)
	return path

mst = prim(edges)