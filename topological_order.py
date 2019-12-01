from collections import deque, defaultdict

edges = [
	['3', '1'],
	['4', '1'],
	['2', '3'],
	['5', '2'],
	['4', '0'],
]

adj_list = {}
for i in range(6):
	adj_list[str(i)] = []

for u, v in edges:
	adj_list[u].append(v)

GRAY = 0
BLACK = 1

def toplogical(adj_list):

	order = deque()

	state = defaultdict(lambda:None)
	enter = set(adj_list)

	def dfs(node):

		state[node] = GRAY

		for v in adj_list[node]:

			sv = state[v]

			if sv == GRAY:
				raise ValueError('Cycle detected')

			if sv == BLACK:
				continue

			enter.discard(v)
			dfs(v)

		order.appendleft(node)
		state[node] = BLACK

	while enter:
		dfs(enter.pop())

	return order

print(toplogical(adj_list))