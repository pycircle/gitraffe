#!/usr/bin/env python3.2

from subprocess import getoutput

graph = getoutput('git log --graph --pretty=format:""')
graph = graph.split('\n')
j = 0
for i in range(len(graph)):
    if not '*' in graph[i-j]:
        del graph[i-j]
        j += 1
    while graph[i-j][-1] == ' ':
        graph[i-j] = graph[i-j][:-1]
for i in range(1, len(graph)-1):
    if len(graph[i]) < len(graph[i+1]):
        graph[i] = graph[i].replace(' ', '-')
        graph[i] += '-\\'
    if len(graph[i]) < len(graph[i-1]):
        if graph[i-1][-1] != '/' or len(graph[i-1]) > len(graph[i])+2:
            graph[i] = graph[i].replace(' ', '-')
            graph[i] += '-/'
for line in graph:
    print(line)
print(graph)
