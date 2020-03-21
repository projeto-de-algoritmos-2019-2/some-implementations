from collections import deque, defaultdict

edges = [
	['A', 'B'],
	['A', 'G'],
	['B', 'C'],
	['B', 'D'],
	['C', 'E'],
	['C', 'H'],
	['D', 'E'],
	['D', 'F'],
	['E', 'F'],
	['G', 'H'],
	['H', 'E'],
	['H', 'F'],
]

adj_list = {}
for u,v in edges:
	adj_list[u] = []
	adj_list[v] = []

for u, v in edges:
	adj_list[u].append(v)

GRAY = 0
BLACK = 1

def toplogical(adj_list):

	# ordem da ordenação topologica	
	order = deque()

	# var para verificar se o nó não foi, foi ou está sendo processado
	state = defaultdict(lambda:None)

	# fila de nós na ordem que serão processados
	enter = set(adj_list)

	def dfs(node):

		# está sendo processado
		state[node] = GRAY

		for v in adj_list[node]:

			sv = state[v]

			# se esse nó filho não está sendo processado há um ciclo
			if sv == GRAY:
				raise ValueError('Cycle detected')

			# se esse nó já foi processado só continue
			if sv == BLACK:
				continue

			# caso esse nó seja novo, comece a processá-lo
			enter.discard(v)
			dfs(v)

		order.appendleft(node)
		state[node] = BLACK

	while enter:
		dfs(enter.pop())

	return order

print(toplogical(adj_list))