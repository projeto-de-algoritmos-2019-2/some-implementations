class UnionFind():
    def __init__(self, vertices):
        self.rank = {}
        self.parent = {}

        for i in vertices:
            self.parent[i] = i
            self.rank[i] = 0
    
    def find(self, i):
        while i != self.parent[i]:
            i = self.parent[i]

        return i
    
    def join(self, i, j):
        pi = self.find(i)
        pj = self.find(j)

        if pi == pj:
            return

        if self.rank[pi] > self.rank[pj]:
            self.parent[pj] = i
                
        else:
            self.parent[pi] = pj

            if self.rank[pi] == self.rank[pj]:
                self.rank[pj] += 1