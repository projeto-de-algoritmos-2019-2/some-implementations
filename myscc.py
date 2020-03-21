
from collections import defaultdict

edges = [
    [1,2],
    [2,3],
    [3,1],
    [3,4],
    [4,6],
    [6,7],
    [6,5],
    [5,4],
    [7,4],
    [7,8],
    [8,9],
    [9, 10],
    [10, 8],
]

def strong_connected_components(edges):

    adj = defaultdict(list)

    for v,u in edges:
        adj[v].append(u)

    stack = []
    visited = defaultdict(lambda:False)
    keys = set(adj)

    def dfs(u):
        if visited[u]:
            return
        
        visited[u] = True

        for v in adj[u]:
            dfs(v)
        
        stack.append(u)



    for u in keys:
        dfs(u)
    


    adj.clear()
    for u, v in edges:
        adj[v].append(u)

    visited.clear()
    components = []

    while stack:
        
        def dfs(u, component=[]):
            visited[u] = True
            component.append(u)

            for v in adj[u]:
                if not visited[v]:
                    component = dfs(v, component)

            return component
        
        nxt = stack.pop()

        if not visited[nxt]:
            component = dfs(nxt)
            components.append(component)
        
    
    print(components)

strong_connected_components(edges)