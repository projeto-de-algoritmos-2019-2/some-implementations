from queue import Queue
from collections import Counter

class Graph:

	def __init__(self, edges):

		self.graph = Counter()

		for f, t in edges:
			self.check_vertice(f)
			self.graph[f].append(t)

	def add_edge(self, edge):

		f, t = edge

		self.check_vertice(f)
		self.graph[f].append(t)


	def print(self):
		for k, v in sorted(self.graph.items()):
			print(k, v)

	def check_vertice(self, f):
		if not self.graph[f]:
			self.graph[f] = []

	def bfs(self, at=1):
		visited = []
		queue = Queue()
		visited.append(at)
		queue.put(at)

		while not queue.empty():
			at = queue.get()
			print(at, end='->')

			self.check_vertice(at)

			for v in self.graph[at]:
				if v in visited:
					continue

				visited.append(v)
				queue.put(v)

	def dfs(self, at=1):

		if at in self.visited:
			return

		self.visited.append(at)

		print(' ', at, end='')

		self.check_vertice(at)

		for v in self.graph[at]:
			self.dfs(v)


	def connected_components(self):
		self.visited = []
		qnt = 0

		for v in sorted(self.graph.keys()):
			if v in self.visited:
				continue

			qnt += 1
			print(f'Component {qnt}:')
			self.dfs(v)
			print()
def main():

	edges = [
		[1, 2], [1, 3], [1, 4],
		[2, 3], [2, 4],
		[3, 5],
		[4, 5],
		[4, 7],
		[5, 1],
		[9, 10]
	]

	g = Graph(edges)
	g.add_edge([5, 2])

	g.connected_components()


main()