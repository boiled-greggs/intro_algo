import sys
import heapdict
from collections import defaultdict

def make_graph(f):
    num_nodes = 0
    nodes = []
    G = defaultdict(list)
    for line in f:
        l = line.split()
        l[0] = int(l[0])-1
        l[1] = int(l[1])-1
        l[2] = int(l[2])
        if l[0] not in nodes: 
            nodes.append(l[0])
            num_nodes += 1
        if l[1] not in nodes:
            nodes.append(l[1])
            num_nodes += 1
        if l[0] not in G:
            G[l[0]] = []
            G[l[0]].append([l[1],l[2]])
        else:
            G[l[0]].append([l[1],l[2]])
    return G, num_nodes, nodes





if __name__ == "__main__":
    s = int(sys.argv[1])-1
    f = open("ex1.txt")
    #f = open("rome.txt")
    G,n,nodes = make_graph(f)
    dist = [float("inf")]*n
    prev = [None]*n
    dist[s] = 0

    H = heapdict.heapdict()
    for v in G:
        if v != s:
            dist[v] = float("inf")
        H[v] = dist[v]
    H[s] = dist[s]

    
    while len(H):
        u = H.popitem()
        for edge in G[u[0]]:
            if dist[edge[0]] > dist[u[0]]+edge[1]:
                dist[edge[0]] = dist[u[0]]+edge[1]
                prev[edge[0]] = u[0]
                H[edge[0]] = dist[edge[0]]
    for i in range(n):
        if (i == s):
            print(i+1,":",dist[i]," [%d]"%(i+1))
        else:
            print(i+1,":",dist[i]," ",end='')
            done = False
            path = [i+1]
            j = i
            while not done:
                if prev[j] != s:
                    path.append(prev[j]+1)
                    j = prev[j]
                else:
                    done = True
            path.append(s+1)
            print(list(reversed(path)))
        print()
