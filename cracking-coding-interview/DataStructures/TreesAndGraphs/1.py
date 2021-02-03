from collections import defaultdict

# Given a directeed graph and two nodes(S and E) design an algorithm to find out whether there is a route from s to E.

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
 
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFS(self, s, t, visited):
        # print(v, " ")
        if s == t:
            return True

        visited.append(s)

        for neighbour in self.graph[s]:
            if neighbour not in visited:
                if self.DFS(neighbour, t, visited):
                    return True
        return False


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

# print("Following is DFS from (starting from vertex 2)")
# g.DFS(2)
print(g.DFS(0, 3, []))