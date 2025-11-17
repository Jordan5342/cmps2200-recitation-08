from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    heap = [(0, 0, source)]
    visited = {}  # Maps vertex to (weight, num_edges)
    
    while heap:
      weight, num_edges, vertex = heappop(heap)
        
      # Skip if we've already found a better path to this vertex
      if vertex in visited:
        continue
        
      # Record this as the best path to this vertex
      visited[vertex] = (weight, num_edges)
        
      # Explore neighbors
      if vertex in graph:
        for neighbor, edge_weight in graph[vertex]:
          if neighbor not in visited:
            heappush(heap, (weight + edge_weight, num_edges + 1, neighbor))
    
    return visited
    

    
    
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    parents = {source: None}
    queue = deque([source])
    
    while queue:
        vertex = queue.popleft()
        
        # Explore neighbors
        if vertex in graph:
            for neighbor in graph[vertex]:
                if neighbor not in parents:
                    parents[neighbor] = vertex
                    queue.append(neighbor)
    
    return parents

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    path = []
    current = destination
    
    while current is not None:
        path.append(current)
        current = parents[current]
    
    path.pop(0)
    path.reverse()
    return ''.join(path)