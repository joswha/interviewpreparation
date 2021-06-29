def allPathsToTarget(graph):
    queue = [[0]]
    res = []
    target = len(graph) - 1

    while len(queue) > 0:
        top = queue.pop(0)

        if top[-1] == target:
            res.append(top)
            continue
            
        for neighbour in graph[top[-1]]:
            queue.append(top + [neighbour])

    return res


graph = [[1,2],[3],[3],[]]
print(allPathsToTarget(graph))