# Find shortest path in undirected graph
# Given a graph g represented as adjacency list and nodes u and v, find shortest path between u and v. If no such path, return -1.

def shortest_path(g, u, v):
    """Find shortest path between u and v in g."""
    visited = set()
    from queue import Queue
    q = Queue()
    q.put([u])
    while not q.empty():
        path = q.get()
        if path[-1] == v:
            return path
        visited.add(path[-1])
        for neighbor in g[path[-1]]:
            if not neighbor in visited:
                q.put(path+[neighbor])
    return -1

assert shortest_path({'a': ['a']}, 'a', 'a') == ['a']
assert shortest_path({'a': [], 'b': []}, 'a', 'b') == -1
graph = {'a': ['b'], 'b': ['a', 'c', 'd'], 'c': ['b', 'd', 'e'], 'd': ['b', 'c', 'f'],
     'e': ['c', 'f', 'g'], 'f': ['d', 'e', 'g'], 'g': ['e', 'f']}
start = 'a'
end = 'g'
assert len(shortest_path(graph, start, end)) == 5
print('All passed!')