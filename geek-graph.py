from collections import defaultdict

class Graph:

	def __init__(self):
		"""
		If a key does not exist in dict, the key value will be 
		instantiated as an empty list!
		"""
		self.graph = defaultdict(list)

	def addEdge(self, u, v):
		self.graph[u].append(v)

	def DFS_recursive(self, s, visited=defaultdict(lambda: False), 
		process=lambda x: print(x, end=' ')):

		if visited[s]:
			return

		visited[s] = True

		process(s)

		for v in sorted(self.graph[s]):
			self.DFS_recursive(v, visited)

	def DFS_iterative(self, s, visited=defaultdict(lambda: False),
		process=lambda x: print(x, end=' ')):

		stack = []
		stack.append(s)

		while stack:
			s = stack[-1]

			if not visited[s]:
				visited[s] = True
				process(s)

			for v in sorted(self.graph[s]):
				if not visited[v]:
					stack.append(v)
					break

			if stack[-1] == s:
				stack.pop()

	def BFS(self, s, process = lambda x: print(x, end=' ')):

		visited = defaultdict(lambda : False)
		queue = []

		queue.append(s)
		visited[s] = True

		while queue:
			s = queue.pop(0) # pop_front
			process(s)

			for i in self.graph[s]:
				if not visited[i]:
					queue.append(i)
					visited[i] = True

	def connected_components(self):
		visited = defaultdict(lambda : False)
		qnt = 0

		for k in sorted(self.graph.keys()):
			if visited[k]:
				continue

			qnt += 1
			print(f'Component {qnt}:')
			self.DFS(k, visited)
			print()


def main():
	g = Graph()
	g.addEdge(1, 2)
	g.addEdge(1, 3)

	g.addEdge(2, 5)
	g.addEdge(2, 4)
	
	g.addEdge(3, 6)
	g.addEdge(3, 7)
	
	g.addEdge(7, 8)
	g.addEdge(8, 9)

	g.DFS_iterative(1)
	print()
	g.DFS_recursive(1)

main()
