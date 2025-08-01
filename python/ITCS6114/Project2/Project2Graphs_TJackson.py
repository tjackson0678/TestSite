"""
Terrence Jackson 
ITCS 6114 - Project 2
Summer 2025 - 31 July
"""

import os 
class Graph: 

    def __init__(self, vertices=0, directed=False): 
        self.V = vertices 
        self.graph = [] 
        self.directed = directed
        # Adjacency list for Dijkstra's algorithm
        self.adj_list = {chr(65+i): [] for i in range(vertices)}
        # Mapping between vertex letters and indices
        self.vertex_to_index = {chr(65+i): i for i in range(vertices)}
        self.index_to_vertex = {i: chr(65+i) for i in range(vertices)}

    # Function to add an edge to graph 
    def addEdge(self, u, v, w): 
        # Convert letters to indices for the edge list
        u_idx = self.vertex_to_index.get(u, ord(u) - 65)
        v_idx = self.vertex_to_index.get(v, ord(v) - 65)
        
        self.graph.append([u_idx, v_idx, w]) 
        # Add to adjacency list using letter identifiers
        self.adj_list[u].append((v, w))
        
        # If the graph is undirected, add the reverse edge as well
        if not self.directed:
            self.adj_list[v].append((u, w))

    # Function to read graph from a file
    @classmethod
    def from_file(cls, filename):
        """
        Read a graph from a file.
        
        Expected file format:
        First line: Number of vertices (n), Number of edges (m), Graph type (U/D)
        Next m lines: Each line represents an edge with format "u v w"
            where u and v are vertex letters (A, B, C, etc.) and w is the edge weight.
        Last line: Source vertex letter for algorithms
        
        """
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                
                # First line contains: vertices, edges, graph type
                first_line = lines[0].strip().split()
                if len(first_line) < 3:
                    raise ValueError("First line must contain: vertices, edges, graph type (U/D)")
                
                num_vertices = int(first_line[0])
                num_edges = int(first_line[1])
                graph_type = first_line[2].upper()
                
                if graph_type not in ['U', 'D']:
                    raise ValueError("Graph type must be 'U' for undirected or 'D' for directed")
                
                directed = (graph_type == 'D')
                
                # Create a new graph with the specified number of vertices and direction
                graph = cls(num_vertices, directed)
                
                # Read edges from the next num_edges lines
                for i in range(1, num_edges + 1):
                    if i >= len(lines):
                        raise ValueError(f"Expected {num_edges} edges, but file has fewer lines")
                        
                    line = lines[i].strip()
                    if not line:  # Skip empty lines
                        continue
                        
                    # Parse the edge information
                    parts = line.split()
                    if len(parts) < 3:
                        raise ValueError(f"Line {i+1} does not contain a valid edge (u v w)")
                        
                    u = parts[0]  # Vertex as letter
                    v = parts[1]  # Vertex as letter
                    w = int(parts[2])  # Weight as integer
                    graph.addEdge(u, v, w)
                
                # Last line contains the source vertex
                if num_edges + 1 < len(lines):
                    source = lines[num_edges + 1].strip()
                    if source and source in graph.adj_list:
                        graph.source = source
                    else:
                        print(f"Warning: Invalid source vertex '{source}' specified, using 'A' as default")
                        graph.source = 'A'
                else:
                    print("Warning: No source vertex specified, using 'A' as default")
                    graph.source = 'A'
                
                return graph
                
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
            return None
        except ValueError as e:
            print(f"Error: {str(e)}")
            return None
        except Exception as e:
            print(f"Error reading file '{filename}': {str(e)}")
            return None

    # A utility function to find set of an element i 
    # (truly uses path compression technique) 
    def find(self, parent, i): 
        if parent[i] != i: 
            # Reassignment of node's parent to root node as path compression requires 
            parent[i] = self.find(parent, parent[i]) 
        return parent[i] 

    # A function that does union of two sets of x and y 
    # (uses union by rank) 
    def union(self, parent, rank, x, y): 
        # Attach smaller rank tree under root of high rank tree (Union by Rank) 
        if rank[x] < rank[y]: 
            parent[x] = y 
        elif rank[x] > rank[y]: 
            parent[y] = x 
        # If ranks are same, then make one as root and increment its rank by one 
        else: 
            parent[y] = x 
            rank[x] += 1

    # The main function to construct MST using Kruskal's algorithm 
    def KruskalMST(self): 
        # This will store the resultant MST 
        result = [] 
        
        # An index variable, used for sorted edges 
        i = 0
        # An index variable, used for result[] 
        e = 0

        # Sort all the edges in non-decreasing order of their weight 
        self.graph = sorted(self.graph, key=lambda item: item[2]) 

        parent = [] 
        rank = [] 

        # Create V subsets with single elements 
        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 

        # Number of edges to be taken is less than to V-1 
        while e < self.V - 1 and i < len(self.graph): 
            # Pick the smallest edge and increment the index for next iteration 
            u, v, w = self.graph[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent, v) 

            # If including this edge doesn't cause cycle, include it in result
            if x != y: 
                e = e + 1
                result.append([u, v, w]) 
                self.union(parent, rank, x, y) 
            # Else discard the edge 

        minimumCost = 0
        print("Edges in the constructed MST") 
        for u, v, weight in result: 
            minimumCost += weight 
            # Convert indices back to letters for output
            u_letter = self.index_to_vertex[u]
            v_letter = self.index_to_vertex[v]
            print(f"{u_letter} -- {v_letter} == {weight}") 
        print("Minimum Spanning Tree", minimumCost) 
    
    # Dijkstra's algorithm to find shortest path from source vertex
    def dijkstra(self, src):
        import heapq
        
        # Initialize distances with infinity for all vertices
        dist = {v: float('inf') for v in self.adj_list}
        # Distance of source vertex from itself is 0
        dist[src] = 0
        # To track the shortest path
        prev = {v: None for v in self.adj_list}
        
        # Priority queue to get the vertex with minimum distance
        pq = [(0, src)]  # (distance, vertex)
        
        # Set to keep track of vertices included in shortest path tree
        visited = set()
        
        while pq:
            # Get the vertex with minimum distance
            current_dist, u = heapq.heappop(pq)
            
            # If we've already processed this vertex, skip it
            if u in visited:
                continue
                
            # Mark the vertex as visited
            visited.add(u)
            
            # If current distance is greater than the known distance, skip
            if current_dist > dist[u]:
                continue
                
            # Check all adjacent vertices of u
            for v, weight in self.adj_list[u]:
                # If there is a shorter path to v through u
                if dist[u] + weight < dist[v]:
                    # Update distance of v
                    dist[v] = dist[u] + weight
                    prev[v] = u
                    # Add v to the priority queue
                    heapq.heappush(pq, (dist[v], v))
        
        return dist, prev
    
    # Function to print the shortest path from source to a specific target
    def print_shortest_path(self, src, target):
        dist, prev = self.dijkstra(src)
        
        if dist[target] == float('inf'):
            print(f"No path exists from vertex {src} to vertex {target}")
            return
            
        # Reconstruct the path
        path = []
        at = target
        while at is not None:
            path.append(at)
            at = prev[at]
            
        # Reverse the path to get it from source to target
        path = path[::-1]
        
        # Print the path and distance
        print(f"Shortest path from {src} to {target}: {' -> '.join(path)}")
        print(f"Total distance: {dist[target]}")
    
    # Function to print all shortest paths from source
    def print_all_shortest_paths(self, src):
        dist, prev = self.dijkstra(src)
        
        print(f"Shortest paths from source vertex {src}:")
        for v in self.adj_list:
            if v == src:
                continue
                
            if dist[v] == float('inf'):
                print(f"No path to vertex {v}")
            else:
                # Reconstruct the path
                path = []
                at = v
                while at is not None:
                    path.append(at)
                    at = prev[at]
                    
                # Reverse the path to get it from source to target
                path = path[::-1]
                
                print(f"To vertex {v}: {' -> '.join(path)}, distance: {dist[v]}")

    # Run Dijkstra's algorithm from the source vertex specified in the input file
    def run_dijkstra_from_source(self):
        if hasattr(self, 'source'):
            print(f"\nRunning Dijkstra's algorithm from source vertex {self.source}:")
            self.print_all_shortest_paths(self.source)
        else:
            print("No source vertex specified. Using 'A' as default.")
            self.print_all_shortest_paths('A')


# Driver code 
if __name__ == '__main__': 
    # Example: get the file path: 
    running_directory = os.path.dirname(os.path.abspath(__file__))

    # Add current directory filename to running directory
    filename = running_directory + '/uwGraph1.txt'
    
    # Example: Reading a graph from a file
    print("\nExample: Reading a graph from a file")
    graph_from_file = Graph.from_file(filename)
    if graph_from_file:
         print(f"Graph loaded from {filename}")
         graph_from_file.KruskalMST()
         graph_from_file.run_dijkstra_from_source()
