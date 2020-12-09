class Graph:
    def __init__(self):
        self.adj_list = {}
        self.edge_dist = {}

    def add_city(self, new_city):
        self.adj_list[new_city] = []
    
    def add_edge(self, from_city, to_city, weight):
        self.edge_dist[(from_city, to_city, weight)] = weight
        self.adj_list[from_city].append(to_city)

class Vertex:
    def __init__(self, address):
        self.address = address

