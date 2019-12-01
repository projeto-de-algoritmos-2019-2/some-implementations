from collections import defaultdict

def get_adj(edges):
	
	adj = defaultdict(lambda: [])

	for e, v in edges:
		adj[e].append(v)
		adj[v]

	return adj


def bipartite(edges):
	NONE, RED, BLUE = 0, 1, 2

	adj = get_adj(edges)
	colors = defaultdict(lambda: 0)

	def bfs(node):
		queue = [node]
		colors[node] = RED

		while queue:
			node = queue.pop()

			for v in adj[node]:
				if colors[v] == NONE:
					colors[v] = 3 - colors[node]
					queue.append(v)

				elif colors[v] == colors[node]:
					raise ValueError("Not Bipartite")

	for k in adj:
		if colors[k] == NONE:
			bfs(k)

	return "Is Bipartite"

edges = [
	[1, 2],
	[1, 9],
	# [1, 10],
	[1, 8],
	[2, 3],
	[2, 10],
	[9, 10],
	[9, 11],
	[9, 7],
	[8, 11],
	# [8, 12],
	[3, 4],
	[10, 4],
	[11, 12],
	[11, 6],
	[7, 6],
	[4, 5],
	[12, 5],
	[6, 5],
]

print(bipartite(edges))