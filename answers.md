# CMPS 2200 Recitation 08

## Answers

**Name:**Jordan Sztejman
**Name:**_________________________


Place all written answers from `recitation-08.md` here for easier grading.



- **1b)**
The work of this algorithm is W(n)= O((V+E)log V), where V stands for the number of vertices and E stands for the number of edges. This is because each vertice is processed one and each edge are examined once. Additionally, the heap takes o(log(v)) time complexity. The span of this algorithm is W(n)=O(V(log(V)). In this algorithm, we can process up to V extraction by popping the minimum element from the heap which takes O(log(v)) time complexity. 


- **2b)*
The work of bfs_path is W(n)=O(V+E) where each vertex is visited once and each edge is examined once. The span is S(n)=O(V) where each vertex is proccesed by level which gives a worst case time complexcity of O(V). THe work of get_path is W(n)=O(V) where it traverses from destination to the source. Each step takes the worst time compleity of O(V). The span is S(n)=O(V) can not be parralleized due to the depenedncy on the previous steps.
