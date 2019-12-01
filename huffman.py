from collections import Counter
from heapq import heappush, heappop

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

text = 'O tema da redação do Exame Nacional do Ensino Médio (Enem) deste ano é "Democratização do acesso ao cinema no Brasil", segundo informações do Instituto Nacional de Estudos e Pesquisas Educacionais (Inep). O texto deve ser dissertativo-argumentativo, com até 30 linhas, desenvolvido a partir da situação-problema e de subsídios oferecidos pelos textos motivadores.'

# text = 'durval'

hist = Counter(text)
min_heap = MinHeap()

class Node:
    def __init__(self, weight, value, left=None, right=None):
        self.weight = weight
        self.value = value
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.weight < other.weight

    def __le__(self, other):
        return self.weight <= other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __ge__(self, other):
        return self.weight >= other.weight

    def __eq__(self, other):
        return self.weight == other.weight

    def __ne__(self, other):
        return self.weight != other.weight

    def __hash__(self):
        return hash(self.weight)

    def __str__(self):
        return f"{{ {self.weight}, {self.value}, {self.left}, {self.right} }}"

for value, weight in hist.items():
    node = Node(weight, value)
    min_heap.push(node)

while min_heap.size() > 1:
    a = min_heap.pop()
    b = min_heap.pop()

    node = Node(a.weight + b.weight, value=None, left=a, right=b)

    min_heap.push(node)


d = {}

def dfs(node, context=''):

    if node.value:
        d[node.value] = context
        return

    if node.left:
        dfs(node.left, context + '0')

    if node.right:
        dfs(node.right, context + '1')

node = min_heap.pop()
dfs(node)

# total = 0
# for k, v in d.items():
#     print(k, v)
#     total += len(v) * hist[k]
# print(d)
# print('total', total, 'bits')

bin_msg = ''

for l in text:
    bin_msg += d[l]

# print(bin_msg)
# print()

at = node

for b in bin_msg:

    if b == '0':
        at = at.left

    if b == '1':
        at = at.right


    if at.value:
        print(at.value, end='')
        at = node
print()