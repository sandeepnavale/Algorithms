# Dijkstra's Algorithm in Python.
graph = {
    'a': {
        'b': 10,
        'c': 3
    },
    'b': {
        'c': 1,
        'd': 2
    },
    'c': {
        'b': 4,
        'd': 8,
        'e': 2
    },
    'd': {
        'e': 7
    },
    'e': {
        'd': 9
    }
}


def dijkstras(graph, start, end):
    shortest_dist = {}
    predecessor = {}
    unseenNodes = graph
    infinity = 999999
    path = []

    for node in unseenNodes:
        shortest_dist[node] = infinity
    shortest_dist[start] = 0
    # print(shortest_dist)

    while unseenNodes:
        minNode = None
        i = 0
        # print('####')
        for node in unseenNodes:

            # Temp Debug start
            # i += 1
            # print(node, i)
            # Temp debug end

            if minNode is None:
                minNode = node
            elif shortest_dist[node] < shortest_dist[minNode]:
                minNode = node

            # main Algorithm
            for childNode, weight in graph[minNode].items():
                if weight + shortest_dist[minNode] < shortest_dist[childNode]:
                    shortest_dist[childNode] = weight + shortest_dist[minNode]
                    predecessor[childNode] = minNode

        unseenNodes.pop(minNode)
    CurrNode = end
    while CurrNode != start:
        try:
            path.insert(0, CurrNode)
            CurrNode = predecessor[CurrNode]
        except KeyError:
            print('Path not found')
            break

    path.insert(0, start)
    if shortest_dist[end] != infinity:
        print('shortest dist is ', str(shortest_dist[end]))
        print('Path is ', str(path))


dijkstras(graph, 'a', 'c')
# dijkstras(graph, 'a', 'd')
# dijkstras(graph, 'a', 'b')
# dijkstras(graph, 'a', 'e')
