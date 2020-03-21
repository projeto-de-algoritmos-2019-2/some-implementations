
def get_adj_list(edges, reverse):
	
	from collections import defaultdict
	adj = defaultdict(lambda: [])

	for e, v in edges:
		if reverse:
			adj[v].append(e)
		else:
			adj[e].append(v)

	return adj


def connected_components(edges):
	
	adj = get_adj_list(edges, reverse = False)

	queue = set(adj)
	stack = []
	visited = set()

	def dfs(node):
		visited.add(node)

		for v in adj[node]:
			if v not in visited:
				dfs(v)

		stack.append(node)


	for node in queue:
		if node not in visited:
			dfs(node)

	adj = get_adj_list(edges, reverse = True)

	visited = set()

	def bfs(node):

		queue = [node]
		component = []

		while queue:
			node = queue.pop()
			
			component.append(node)
			visited.add(node)

			for v in adj[node]:
				if v not in visited:
					queue.append(v)
					visited.add(v)

		return component


	components = []

	while stack:
		node = stack.pop()

		if node not in visited:
			component = bfs(node)
			components.append(component)

	return components

edges = [
	[1, 2],
	[3, 1],
	[2, 3],
	[2, 4],
	[4, 5],
	[5, 6],
	[6, 7],
	[7, 4],
	[6, 8],
	[8, 9],
	[9, 10],
	[10, 11],
	[11, 9],
]



components = connected_components(edges)

print(components)