from collections import defaultdict, deque

class Graph:

	def __init__(self, edges):

		self.edges = defaultdict(set)

		for edge in edges:
			nodeA, nodeB = edge
			self.edges[nodeA].add(nodeB)
			self.edges[nodeB].add(nodeA)


	def bfs(self, start_at, process=lambda x : print(x,end=', ')):

		visited = defaultdict( lambda : False )
		queue = deque()

		queue.append(start_at)
		visited[start_at] = True

		while queue:
			at = queue.popleft()

			process(at)

			for node in self.edges[at]:
				if not visited[node]:
					queue.append(node)
					visited[node] = True

		print()

	def dfs(self, start_at, visited = defaultdict(lambda:False)):

		if visited[start_at]:
			return

		visited[start_at] = True

		print(start_at, end=', ')

		for node in sorted(self.edges[start_at]):
			self.dfs(node, visited)

	def connected_components(self):

		visited = defaultdict(lambda:False)
		comp_id = 0

		for node in sorted(self.edges.keys()):
			if not visited[node]:
				comp_id += 1
				print(f'Component {comp_id}: ')
				self.dfs(node, visited)
				print()

	def __repr__(self):

		repr = ''

		for nodeA, nodeList in sorted(self.edges.items()):
			repr += str(nodeA) + ' ' + str(nodeList) + '\n'

		return repr

def main():

	edges = [
		[1, 4],
		[2, 3],
		[3, 4], [3, 5], [3, 6],
		[4, 1], [4, 3], [4, 5], [4, 7],
		[5, 3], [5, 4], [5, 6], [5, 7],
		[6, 3], [6, 5],
		[7, 4], [7, 5], [7, 8],
		[8, 7], [8, 9],
		[9, 7], [9, 8],
		[10, 11], [10, 12],
		[11, 10], [11, 12],
		[12, 10], [12, 11]
	]

	graph = Graph(edges)
	graph.connected_components()

if __name__ == '__main__':

	main()