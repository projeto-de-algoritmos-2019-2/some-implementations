from unionSet import UnionFind

def kruskall(edges):

    vertices = set()

    for u, v, w in edges:
        vertices.add(u)
        vertices.add(v)

    uf = UnionFind(vertices)

    edges = sorted(edges, key=lambda e: e[2])

    mst = []

    for u, v, w in edges:
        parent_u = uf.find(u)
        parent_v = uf.find(v)

        if parent_u == parent_v:
            continue
            
        uf.join(parent_u, parent_v)
        
        mst.append((u, v, w))
    
    for e in mst:
        print(e)

    


edges = [
    ['B', 'C', 6],
    ['C', 'E', 4],
    ['A', 'C', 1],
    ['A', 'B', 2],
    ['B', 'D', 3],
    ['E', 'F', 5],
    ['D', 'F', 1],
    ['C', 'F', 2],
]

kruskall(edges)
