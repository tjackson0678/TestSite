class Graph: 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        # Adjacency list for Dijkstra's algorithm
        self.adj_list = [[] for _ in range(vertices)]

    # Function to add an edge to graph 
    def addEdge(self, u, v, w): 
        self.graph.append([u, v, w]) 
        # Also add to adjacency list (for Dijkstra)
        self.adj_list[u].append((v, w))
        self.adj_list[v].append((u, w))  # For undirected graph

    # A utility function to find set of an element i 
    # (truly uses path compression technique) 
    def find(self, parent, i): 
        if parent[i] != i: 

            # Reassignment of node's parent 
            # to root node as 
            # path compression requires 
            parent[i] = self.find(parent, parent[i]) 
        return parent[i] 

    # A function that does union of two sets of x and y 
    # (uses union by rank) 
    def union(self, parent, rank, x, y): 

        # Attach smaller rank tree under root of 
        # high rank tree (Union by Rank) 
        if rank[x] < rank[y]: 
            parent[x] = y 
        elif rank[x] > rank[y]: 
            parent[y] = x 

        # If ranks are same, then make one as root 
        # and increment its rank by one 
        else: 
            parent[y] = x 
            rank[x] += 1

    # The main function to construct MST 
    # using Kruskal's algorithm 
    def KruskalMST(self): 

        # This will store the resultant MST 
        result = [] 

        # An index variable, used for sorted edges 
        i = 0

        # An index variable, used for result[] 
        e = 0

        # Sort all the edges in 
        # non-decreasing order of their 
        # weight 
        self.graph = sorted(self.graph, 
                            key=lambda item: item[2]) 

        parent = [] 
        rank = [] 

        # Create V subsets with single elements 
        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 

        # Number of edges to be taken is less than to V-1 
        while e < self.V - 1: 

            # Pick the smallest edge and increment 
            # the index for next iteration 
            u, v, w = self.graph[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent, v) 

            # If including this edge doesn't 
            # cause cycle, then include it in result 
            # and increment the index of result 
            # for next edge 
            if x != y: 
                e = e + 1
                result.append([u, v, w]) 
                self.union(parent, rank, x, y) 
            # Else discard the edge 

        minimumCost = 0
        print("Edges in the constructed MST") 
        for u, v, weight in result: 
            minimumCost += weight 
            print("%d -- %d == %d" % (u, v, weight)) 
        print("Minimum Spanning Tree", minimumCost) 
    
    # Dijkstra's algorithm to find shortest path from source vertex
    def dijkstra(self, src):
        import heapq
        
        # Initialize distances with infinity for all vertices
        dist = [float('inf')] * self.V
        # Distance of source vertex from itself is 0
        dist[src] = 0
        # To track the shortest path
        prev = [None] * self.V
        
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
        print(f"Shortest path from {src} to {target}: {' -> '.join(map(str, path))}")
        print(f"Total distance: {dist[target]}")
    
    # Function to print all shortest paths from source
    def print_all_shortest_paths(self, src):
        dist, prev = self.dijkstra(src)
        
        print(f"Shortest paths from source vertex {src}:")
        for i in range(self.V):
            if i == src:
                continue
                
            if dist[i] == float('inf'):
                print(f"No path to vertex {i}")
            else:
                # Reconstruct the path
                path = []
                at = i
                while at is not None:
                    path.append(at)
                    at = prev[at]
                    
                # Reverse the path to get it from source to target
                path = path[::-1]
                
                print(f"To vertex {i}: {' -> '.join(map(str, path))}, distance: {dist[i]}")


# Driver code 
if __name__ == '__main__': 
    g = Graph(4) 
    g.addEdge(0, 1, 10) 
    g.addEdge(0, 2, 6) 
    g.addEdge(0, 3, 5) 
    g.addEdge(1, 3, 15) 
    g.addEdge(2, 3, 4) 

    # Function call 
    g.KruskalMST()
    
    # Test Dijkstra's algorithm
    print("\nTesting Dijkstra's algorithm:")
    source = 0
    g.print_all_shortest_paths(source)
    
    # Test finding path to a specific vertex
    print("\nFinding path to a specific vertex:")
    g.print_shortest_path(0, 3)
