# Kruskal's Algorithm Analysis

## Pseudocode for Kruskal's Algorithm

```
KRUSKAL-MST(G):
    1. Create an empty set A to store edges of MST
    2. For each vertex v in G.V:
        3. MAKE-SET(v)
    4. Sort the edges of G.E in non-decreasing order by weight
    5. For each edge (u,v) in the sorted G.E:
        6. If FIND-SET(u) ≠ FIND-SET(v):
            7. Add edge (u,v) to set A
            8. UNION(u,v)
    9. Return A
```

## Detailed Runtime Analysis

Let's analyze the time complexity of the implementation in the provided code:

### Data Structure Operations

1. **find operation**: Uses path compression technique
   - Average time complexity: O(α(n)) where α is the inverse Ackermann function
   - For practical purposes, this is nearly constant time O(1)

2. **union operation**: Uses union by rank
   - Time complexity: O(α(n)), effectively O(1)

### Main Algorithm Components

1. **Initialization**:
   - Creating parent and rank arrays: O(V) where V is the number of vertices

2. **Sorting edges**:
   - The line `self.graph = sorted(self.graph, key=lambda item: item[2])`
   - Time complexity: O(E log E) where E is the number of edges
   - Note: Since E can be at most V², this can also be written as O(E log V)

3. **Processing edges**:
   - For each edge, we perform find and possibly union operations
   - Number of edges processed: O(E)
   - Each operation takes O(α(n)) ≈ O(1)
   - Total: O(E)

4. **Result compilation**:
   - Printing and calculating minimum cost: O(V-1) since MST has V-1 edges

### Overall Time Complexity

The dominant factor is the sorting operation, making the overall time complexity:
**O(E log E)** or equivalently **O(E log V)**

### Space Complexity

- Graph representation: O(E)
- Parent and rank arrays: O(V)
- Result array: O(V)

Overall space complexity: **O(E + V)**

## Additional Notes

1. The implementation uses two key optimizations for the disjoint-set data structure:
   - **Path compression** in the find operation
   - **Union by rank** in the union operation

2. These optimizations ensure that the amortized time complexity of find and union operations is nearly constant, which is crucial for the algorithm's efficiency.

3. Kruskal's algorithm is guaranteed to find the minimum spanning tree because it follows the greedy approach of always selecting the edge with the smallest weight that doesn't create a cycle.

4. The example in the driver code creates a graph with 4 vertices and 5 edges, demonstrating a simple use case for the algorithm.