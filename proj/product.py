from mytypes import *
from utils import *

def product(A: NBA, B: NBA) -> NBA:
    G1 = nba_to_graph(A)
    G2 = nba_to_graph(B)

    V3 = []
    stack = []
    visited = dict()
    vertexmap = dict()
    for v1 in G1.V:
        for v2 in G2.V:
            for flag in [1, 2, 3]:
                name = f"{v1.name}_{v2.name}_{flag}"
                final = (flag == 3)
                initial = (v1.initial and v2.initial and flag == 1)
                V3.append(Vertex(name, final, initial))
                vertexmap[name] = V3[-1]

                if initial:
                    stack.append((v1, v2, flag))
                    visited[name] = True
    
    E3 = []

    while stack:
        v1, v2, flag = stack[-1]
        stack.pop()

        source_vertex_name = f"{v1.name}_{v2.name}_{flag}"
        source_vertex = vertexmap[source_vertex_name]

        nextflag = flag
        if flag == 1 and v1.final:
            nextflag = 2
        elif flag == 2 and v2.final:
            nextflag = 3
        elif flag == 3:
            nextflag = 1

        for edge1 in G1.AdjList[v1]:
            for edge2 in G2.AdjList[v2]:
                if edge1[1] != edge2[1]:
                    continue
                
                destination_vertex_name = f"{edge1[0].name}_{edge2[0].name}_{nextflag}"
                destination_vertex = vertexmap[destination_vertex_name]
                label = edge1[1]
                E3.append(Edge(source_vertex, destination_vertex, label))

                if destination_vertex_name not in visited:
                    visited[destination_vertex_name] = True
                    stack.append((edge1[0], edge2[0], nextflag))
                

    V3 = list(filter(lambda x: x.name in visited, V3))
    G3 = Graph(V3, E3)
    return graph_to_nba(G3)