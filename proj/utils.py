from mytypes import *

def nba_to_graph(A):
    V = []
    stateVertex = dict()
    for state in A.states:
        V.append(Vertex(state, state in A.final_states, state in A.initial_states))
        stateVertex[state] = V[-1]
    
    E = []
    for transition in A.transitions:
        source_vertex = stateVertex[transition[0]]
        destination_vertex = stateVertex[transition[1]]
        edge_label = transition[2]
        E.append(Edge(source_vertex, destination_vertex, edge_label))

    return Graph(V, E)

def graph_to_nba(G):
    states = []
    alphabets = []
    initial_states = []
    final_states = []
    transitions = []

    for vertex in G.V:
        states.append(vertex.name)
        if vertex.final:
            final_states.append(vertex.name)
        if vertex.initial:
            initial_states.append(vertex.name)
    
    for edge in G.E:
        source_vertex = edge.source_vertex
        destination_vertex = edge.destination_vertex
        edge_label = edge.edge_label
        transitions.append((source_vertex.name, destination_vertex.name, edge_label))
        alphabets.append(edge_label)
    return NBA(states, alphabets, initial_states, final_states, transitions)


def read_nba_from_file(filename):
    """
    File must contain
    First line         : states
    Second line        : alphabets
    Third line         : initial states
    Fourth line        : final states
    Fifth line         : number of transitions
    Sixth line onwards : each line contain three tuple source state, destination state, and label
    """
    f = open(filename, 'r')
    states = f.readline().strip().split()
    alphabets = f.readline().strip().split()
    initial_states = f.readline().strip().split()
    final_states = f.readline().strip().split()
    transitions = []
    m = int(f.readline())
    for _ in range(m):
        transitions.append(tuple(f.readline().strip().split()))

    return NBA(states, alphabets, initial_states, final_states, transitions)

def print_help():
    print("""
    Available commands:
    empty <filename>                               #check if language of nba is empty
    union <filename1> <filename2>                  #union of two nba
    product <filename1> <filename2>                #Product of two nba
    help                                           #Show this help message
    """)
    print(f"Note: {read_nba_from_file.__doc__}")
