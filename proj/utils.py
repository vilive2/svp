from mytypes import *
import os
from graphviz import Digraph

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


def display(nba: NBA, filename="nba_display", view=True):

    dot = Digraph(format='png', filename=filename)
    dot.attr(rankdir='LR')  # Left to right orientation

    # Dummy start node to point to initial states
    dot.node("", shape="none")

    for state in nba.states:
        shape = 'doublecircle' if state in nba.final_states else 'circle'
        style = 'bold' if state in nba.initial_states else 'solid'
        dot.node(state, shape=shape, style=style)

    for init in nba.initial_states:
        dot.edge("", init)  # From dummy start node to initial state

    for (src, dest, label) in nba.transitions:
        dot.edge(src, dest, label=label)

    output_dir = "temp"
    os.makedirs(output_dir, exist_ok=True)

    # Full filepath including destination folder
    filepath = os.path.join("temp", filename)

    # This writes to: temp/nba.png
    dot.render(filepath, format='png',view=view, cleanup=False)

    print("States:", ', '.join(nba.states))
    print("Alphabets:", ', '.join(nba.alphabets))
    print("Initial states:", ', '.join(nba.initial_states))
    print("Final states:", ', '.join(nba.final_states))
    print("Transitions:")
    
    for (src, dest, label) in nba.transitions:
        print(f"  {src} --{label}--> {dest}")

        
def print_help():
    print("""
    ############################################################################  
        
    Available commands:
    empty <filename>                               # Check if language of nba is empty
    union <filename1> <filename2>                  # Union of two nba
    product <filename1> <filename2>                # Product of two nba
    display <filename>                             # Display 
    help                                           # Show this help message
          
    ############################################################################
    """)
    print(f"Note: {read_nba_from_file.__doc__}")
