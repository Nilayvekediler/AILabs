from graphExercises import Graph
graph = Graph(directed=True)

graph.add_edge('S', 'A', 3)
graph.add_edge('S', 'B', 1)
graph.add_edge('S', 'C', 8)
graph.add_edge('A', 'D', 3)
graph.add_edge('A', 'E', 7)
graph.add_edge('A', 'G', 15)
graph.add_edge('B', 'G', 20)
graph.add_edge('C', 'G', 5)

start,goal='5', 'G'

traced_path = graph.breadth_first_search (start, goal) 
if(traced_path): print('Path:', end=' '); Graph.print_path (traced_path, goal); print()



