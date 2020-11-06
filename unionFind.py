
   def find_parent(parent, i):
        if parent[i] == -1:
            return i
        if parent[i] != -1:
            return find_parent(parent, parent[i])

    def union(self, parent, x, y):
        x_set = find_parent(parent, x)
        y_set = find_parent(parent, y)
        parent[x_set] = y_set

    def isCyclic(self):

        parent = [-1]*(V)
        for i in graph:
            for j in graph[i]:
                x = find_parent(parent, i)
                y = find_parent(parent, j)
                if x == y:
                    return True
                union(parent, x, y)
