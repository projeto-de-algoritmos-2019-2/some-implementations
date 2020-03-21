from collections import defaultdict
import queue


def dijkstra(adj, begin_at):

	dist = defaultdict(lambda: float('inf'))
	dist[begin_at] = 0

	visited = defaultdict(lambda: False)

	# min heap
	pq = queue.PriorityQueue()
	pq.put((0, begin_at))

	while not pq.empty():

		d, v = pq.get()

		if visited[v]:
			continue

		visited[v] = True

		for w, u in adj[v]:
			if dist[u] > d + w:
				dist[u] = d + w
				pq.put((dist[u], u))
	
	return dist

edges = [
	(1, 3, 5),
	(2, 1, 1),
	(2, 4, 3),
	(2, 5, 5),
	(3, 4, 4),
	(4, 5, 1),
	(5, 3, 2),
	(3, 6, 20),
	(5, 6, 1),
]


adj = defaultdict(lambda:[])

for u,v,w in edges:
	adj[u].append((w, v))

begin_at = 2

dist = dijkstra(adj, begin_at)

for i in range(1, 7):
	print(f'Distância de {begin_at} -> {i} = {dist[i]}')