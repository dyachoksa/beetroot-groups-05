class Graph:
    def __init__(self) -> None:
        self.data = {}
    
    def add_vertex(self, value):
        if value in self.data:
            return
        
        self.data[value] = []
    
    def add_edge(self, vertex_a, vertex_b, weight):
        self.data[vertex_a].append(
            (vertex_a, vertex_b, weight)
        )
    
    def get_vertexes(self):
        return list(self.data.keys())
    
    def get_edges(self):
        edges = []

        for vertex_edges in self.data.values():
            edges.extend(vertex_edges)
        
        return edges
    
    def get_vertex_edges(self, vertex):
        return self.data[vertex]
    
    def print_path(self, vertex_a, vertex_b):
        start_vertex = vertex_a

        final_path = []

        def inner(a, b):
            edges = self.data[a]
            # each edge contains start, end and weight in a form of tuple
            # e.g.: (a, b, weight)
            for edge in edges:
                if edge[1] == b:
                    return edge
               
                if edge[1] == start_vertex:
                    return None

                path = inner(edge[1], b)
                if path is not None:
                    final_path.extend([edge, path])
            
            return None
        
        inner(vertex_a, vertex_b)

        return final_path


if __name__ == "__main__":
    graph = Graph()

    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_vertex("E")

    graph.add_edge("A", "C", 1)
    graph.add_edge("A", "D", 1)
    graph.add_edge("B", "C", 1)
    graph.add_edge("D", "A", 1)
    graph.add_edge("C", "D", 1)
    graph.add_edge("C", "E", 1)

    print("Graph vertexes:", graph.get_vertexes())
    print("Graph edges:", graph.get_edges())
    print("Vertex A edges:", graph.get_vertex_edges("A"))
    print("Vertex B edges:", graph.get_vertex_edges("B"))
    print("Vertex C edges:", graph.get_vertex_edges("C"))
    print("Vertex D edges:", graph.get_vertex_edges("D"))
    print("Vertex E edges:", graph.get_vertex_edges("E"))
    
    path = graph.print_path("A", "E")
    print("Path between A and E:", path)
