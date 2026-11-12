# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 09:16:55 2026

@author: User
"""

# BFS
graph={
    "1" : ["2", "3"],
    "2" : ["4", "5"],
    "3" : ["6", "7"],
    "4" : [],
    "5" : [],
    "6" : [],
    "7" : []
}
visited = []
queue = []   #FIFO
def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        current = queue.pop(0)
        print(current, " ")

        for neighbour in graph[current]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
print("Breadth First Search")
bfs(visited, graph, "1")

# DFS

graph={
    "1" : ["2", "3"],
    "2" : ["4", "5"],
    "3" : ["6", "7"],
    "4" : [],
    "5" : [],
    "6" : [],
    "7" : []
}

visited = []

def dfs(visited, graph, node):
    if node not in visited:
        visited.append(node)
        print(node)

        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

print("Deapth First Search")
dfs(visited, graph, "1")
