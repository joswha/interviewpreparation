# Initialization
visited = []
queue = []
graph = {}
vertices_no = 0

# Add a vertex to the dictionary
def add_vertex(v):
  global graph
  global vertices_no
  if v in graph:
    print("Vertex ", v, " already exists.")
  else:
    vertices_no = vertices_no + 1
    graph[v] = []

# Add an edge between vertex v1 and v2 with edge weight e
def add_edge(v1, v2, e):
  global graph
  # Check if vertex v1 is a valid vertex
  if v1 not in graph:
    print("Vertex ", v1, " does not exist.")
  # Check if vertex v2 is a valid vertex
  elif v2 not in graph:
    print("Vertex ", v2, " does not exist.")
  else:
    # Since this code is not restricted to a directed or 
    # an undirected graph, an edge between v1 v2 does not
    # imply that an edge exists between v2 and v1
    temp = [v2, e]
    graph[v1].append(temp)

# Print the graph
def print_graph():
  global graph
  for vertex in graph:
    for edges in graph[vertex]:
      print(vertex, " -> ", edges[0], " edge weight: ", edges[1])

# Performs DFS on a graph, using adjacency list
def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour[0]) #neighbour[0] as we use weighted graphs; [1] is the weight


# Perform BFS on a graph, using adjacency list
def bfs(visited, graph, node):

    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" \n")

        for neighbour in graph[s]:
            if neighbour[0] not in visited:
                visited.append(neighbour[0])
                queue.append(neighbour[0])

# Shortest spanning tree

# 1) Prim's algorithm
# def prim()

# def Dijkstras_Shortest_Path(self, source) :

#     # Initialize the distance of all the nodes from source to infinity
#     distance = [999999999999] * self.node_count
#     # Distance of source node to itself is 0
#     distance[source] = 0

#     # Create a dictionary of { node, distance_from_source }
#     dict_node_length = {source: 0}

#     while dict_node_length :

#         # Get the key for the smallest value in the dictionary
#         # i.e Get the node with the shortest distance from the source
#         source_node = min(dict_node_length, key = lambda k: dict_node_length[k])
#         del dict_node_length[source_node]

#         for node_dist in self.adjlist[source_node] :
#             adjnode = node_dist.name
#             length_to_adjnode = node_dist.dist

#             # Edge relaxation
#             if distance[adjnode] > distance[source_node] + length_to_adjnode :
#                 distance[adjnode] = distance[source_node] + length_to_adjnode
#                 dict_node_length[adjnode] = distance[adjnode]

#     for i in range(self.node_count) :
#         print("Source Node ("+str(source)+")  -> Destination Node(" + str(i) + ")  : " + str(distance[i]))

# 1) Dijkstra's algorithm
# def dijkstra(graph, node):
#     # S = []
#     # prio_queue = [1,2,3,4]
#     distance = [999999999999] * (len(graph) + 1)
#     distance[node] = 0 

#     dict_node_length = {node: 0}

#     while dict_node_length:

#         source_node = min(dict_node_length, key = lambda k: dict_node_length[k])
#         del dict_node_length[source_node]

#         for weight in graph[source_node]:
#             adjnode = weight[0]
#             length_to_adjnode = weight[1]

#             if distance[adjnode] > distance[source_node] + length_to_adjnode:
#                 distance[adjnode] = distance[source_node] + length_to_adjnode
#                 dict_node_length[adjnode] = distance[adjnode]

#     for i in range(len(graph)):
#         print("Source Node (" + str(node) +") -> Destination Node (" + str(i) + ") : " + str(distance[i]))

# Add the vertices to the graph
add_vertex(1)
add_vertex(2)
add_vertex(3)
add_vertex(4)

# Add the edges between the vertices by specifying
# the from and to vertex along with the edge weights.
add_edge(1, 2, 1)
add_edge(1, 3, 1)
add_edge(2, 3, 3)
add_edge(3, 4, 4)
add_edge(4, 1, 5)
# print_graph()

# Reminder: the second element of each list inside the dictionary
# denotes the edge weight.
print ("Internal representation: ", graph)

# dfs(visited, graph, 4)
# bfs(visited, graph, 4)
# dijkstra(graph,1)

class Node_Distance :

    def __init__(self, name, dist) :
        self.name = name
        self.dist = dist

class Graph :

    def __init__(self, node_count) :
        self.adjlist = {}
        self.node_count = node_count

    def Add_Into_Adjlist(self, src, node_dist) :
        if src not in self.adjlist :
            self.adjlist[src] = []
        self.adjlist[src].append(node_dist)

    def Dijkstras_Shortest_Path(self, source) :

        # Initialize the distance of all the nodes from source to infinity
        distance = [999999999999] * self.node_count
        # Distance of source node to itself is 0
        distance[source] = 0

        # Create a dictionary of { node, distance_from_source }
        dict_node_length = {source: 0}

        while dict_node_length :

            # Get the key for the smallest value in the dictionary
            # i.e Get the node with the shortest distance from the source
            source_node = min(dict_node_length, key = lambda k: dict_node_length[k])
            del dict_node_length[source_node]

            for node_dist in self.adjlist[source_node] :
                adjnode = node_dist.name
                length_to_adjnode = node_dist.dist

                # Edge relaxation
                if distance[adjnode] > distance[source_node] + length_to_adjnode :
                    distance[adjnode] = distance[source_node] + length_to_adjnode
                    dict_node_length[adjnode] = distance[adjnode]

        for i in range(self.node_count) :
            print("Source Node ("+str(source)+")  -> Destination Node(" + str(i) + ")  : " + str(distance[i]))

def main() :

    g = Graph(6)

    # Node 0: <1,5> <2,1> <3,4>
    g.Add_Into_Adjlist(0, Node_Distance(1, 5))
    g.Add_Into_Adjlist(0, Node_Distance(2, 1))
    g.Add_Into_Adjlist(0, Node_Distance(3, 4))

    # Node 1: <0,5> <2,3> <4,8> 
    g.Add_Into_Adjlist(1, Node_Distance(0, 5))
    g.Add_Into_Adjlist(1, Node_Distance(2, 3))
    g.Add_Into_Adjlist(1, Node_Distance(4, 8))

    # Node 2: <0,1> <1,3> <3,2> <4,1>
    g.Add_Into_Adjlist(2, Node_Distance(0, 1))
    g.Add_Into_Adjlist(2, Node_Distance(1, 3))
    g.Add_Into_Adjlist(2, Node_Distance(3, 2))
    g.Add_Into_Adjlist(2, Node_Distance(4, 1))

    # Node 3: <0,4> <2,2> <4,2> <5,1>
    g.Add_Into_Adjlist(3, Node_Distance(0, 4))
    g.Add_Into_Adjlist(3, Node_Distance(2, 2))
    g.Add_Into_Adjlist(3, Node_Distance(4, 2))
    g.Add_Into_Adjlist(3, Node_Distance(5, 1))

    # Node 4: <1,8> <2,1> <3,2> <5,3>
    g.Add_Into_Adjlist(4, Node_Distance(1, 8))
    g.Add_Into_Adjlist(4, Node_Distance(2, 1))
    g.Add_Into_Adjlist(4, Node_Distance(3, 2))
    g.Add_Into_Adjlist(4, Node_Distance(5, 3))

    # Node 5: <3,1> <4,3> 
    g.Add_Into_Adjlist(5, Node_Distance(3, 1))
    g.Add_Into_Adjlist(5, Node_Distance(4, 3))

    g.Dijkstras_Shortest_Path(0)
    print("\n")
    g.Dijkstras_Shortest_Path(5)

if __name__ == "__main__" :
   main()

