import networkx as nx
import os

def create_uWGraph(filepath):
    """
    Reads a file containing edge data (source, target, weight) and
    creates an undirected weighted graph using NetworkX.

    Args:
        filepath (str): The path to the input file.

    Returns:
        networkx.Graph: An undirected weighted graph.
    """
    G = nx.Graph()  # Initialize an undirected graph
    dG = nx.DiGraph()

    with open(filepath, 'r') as f:
        line1 = f.readline().strip().split()
        vert, edges, type = line1

        for line in f:
            parts = line.strip().split()  # Split by whitespace
            if len(parts) == 3:
                u, v, weight_str = parts
                try:
                    weight = float(weight_str)  # Convert weight to a float
                    if type == 'D': 
                        dG.add_edge(u, v, weight=weight)  # Add directed edge with weight 
                    else: 
                        G.add_edge(u, v, weight=weight)  # Add edge with weight
                except ValueError:
                    print(f"Warning: Could not convert weight '{weight_str}' to a number. Skipping edge: {line.strip()}")
            elif len(parts) == 1:
                start = parts
            else:
                print(f"Warning: Skipping malformed line in file: {line.strip()}")
    if type == 'D': 
        return start, line1, dG            
    return start, line1, G

# Example usage:
running_directory = os.path.dirname(os.path.abspath(__file__))
current_directory = os.getcwd()
file_path = running_directory + '/uwGraph.txt'
start, line1, my_graph = create_uWGraph(file_path)
vert, edges, type = line1
print("This is the first line: ", line1[0])
print("Starting node: ", start[0])


shortest_paths = nx.single_source_dijkstra(my_graph, '0', target=None, weight='weight')
# Print edges and their weights to verify
print(f"Smallest cost and paths from node {start[0]}:", shortest_paths)
