#!/usr/bin/env python
# coding: utf-8

from collections import defaultdict

H_dist = {}
Graph_nodes = {}

def get_neighbors(v):
    return Graph_nodes.get(v, [])

def heuristic(n):
    return H_dist[n]

def aStarAlgo(start_node, stop_node):
    open_set = {start_node}
    closed_set = set()
    g = {}               # store distance from starting node
    parents = {}         # parents contains an adjacency map of all nodes

    # distance of starting node from itself is zero
    g[start_node] = 0
    parents[start_node] = start_node

    while len(open_set) > 0:
        n = None

        # node with lowest f() is found
        for v in open_set:
            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v

        if n == stop_node or Graph_nodes.get(n) is None:
            pass
        else:
            for (m, weight) in get_neighbors(n):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)

        if n is None:
            print('Path does not exist!')
            return None

        # reached target node
        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print('Path found: {}'.format(path))
            return path

        open_set.remove(n)
        closed_set.add(n)

    print('Path does not exist!')
    return None

# Input reading
graph = defaultdict(list)
n, e = map(int, input().split())

for i in range(e):
    u, v, cost = input().split()
    graph[u].append((v, float(cost)))
    graph[v].append((u, float(cost)))

for i in range(n):
    node, h = input().split()
    H_dist[node] = float(h)

Graph_nodes = graph

# Call using the nodes present in your input (start: 'A', goal: 'J')
aStarAlgo('A', 'J')