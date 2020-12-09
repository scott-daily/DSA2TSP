class Graph:
    def __init__(self):
        self.adj_list = {}
        self.edge_dist = {}

    def add_address(self, new_address):
        self.adj_list[new_address] = []
    
    def add_edge(self, from_address, to_address, weight):
        self.edge_dist[(from_address, to_address)] = weight
        self.adj_list[from_address].append(to_address)

class Vertex:
    def __init__(self, address):
        self.address = address

