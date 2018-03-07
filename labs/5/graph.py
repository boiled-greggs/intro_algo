import sys
from collections import defaultdict

def make_graph(f):
    num_nodes = 0
    nodes = []
    G = defaultdict(list)
    for line in f:
        l = line.split()
        l[0] = int(l[0])
        l[1] = int(l[1])
        if l[0] not in nodes: 
            nodes.append(l[0])
            num_nodes += 1
        if l[1] not in nodes:
            nodes.append(l[1])
            num_nodes += 1
        if l[0] not in G:
            G[l[0]] = []
            G[l[0]].append(l[1])
        else:
            G[l[0]].append(l[1])
    return G, num_nodes

def reverse(G):
    Gr = defaultdict(list)
    for key in G:
        for c in G[key]:
            Gr[c].append(key)
    return Gr

def explore(G, u, visited, stack):
    visited[u] = True
    for i in G[u+1]:
        if visited[i-1] == False:
            explore(G, i-1, visited, stack)
    stack = stack.append(u+1)

def explore2(G, u, visited):
    visited[u-1] = True
    print(u,"", end="")
    for i in G[u]:
        if visited[i-1] == False:
            explore2(G, i, visited)

def SCC(G, Gr, n):
    stack = []
    visited = [False]*n
    for i in range(n):
        if visited[i] == False:
            explore(Gr, i, visited, stack)

    visited = [False]*n

    while stack:
        i = stack.pop()
        if visited[i-1] == False:
            explore2(G, i, visited)   
            print("")





if __name__ == "__main__":
    fname = sys.argv[1]
    f = open(fname)
    
    G, num_nodes = make_graph(f)

    Gr = reverse(G)

    SCC(G,Gr,num_nodes)
