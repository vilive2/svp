class NBA:
    def __init__(self, states, alphabets, initial_states, final_states, transitions):
        self.states = set(states)
        self.alphabets = set(alphabets)
        self.initial_states = set(initial_states)
        self.final_states = set(final_states)
        self.transitions = set(transitions)

    def print(self):
        print(self.states)
        print(self.alphabets)
        print(self.initial_states)
        print(self.final_states)
        print(self.transitions)
    
    def __str__(self):
        return f"Q:{self.states}\nInput:{self.alphabets}\nQ0:{self.initial_states}\nF:{self.final_states}\nTransitions:{self.transitions}"

class Vertex:
    def __init__(self, name, final, initial):
        self.name = name
        self.final = final
        self.initial = initial
    def __hash__(self):
        return hash(self.name)
    def __repr__(self):
        return f"'{self.name}|{['NF', 'F'][self.final]}|{['NI','I'][self.initial]}'"

class Edge:
    def __init__(self, source_vertex, destination_vertex, edge_label):
        self.source_vertex = source_vertex
        self.destination_vertex = destination_vertex
        self.edge_label = edge_label

class Graph:
    def __init__(self, V, E):
        self.V = V
        self.E = E
        self.AdjList = dict()
        for v in V:
            self.AdjList[v] = []
        
        for edge in E:
            self.AdjList[edge.source_vertex].append(tuple([edge.destination_vertex, edge.edge_label]))
    
    def print(self):
        print(self.AdjList)
