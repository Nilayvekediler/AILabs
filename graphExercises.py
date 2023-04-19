from collections import deque 
from queue import heappop, heappush
from math import inf # matematiksel işlemlerde sınır değerleri veya maksimum/minimum değerleri deneme amaçlı

class Graph:
    def __init__(self, directed=True):

        self.edges = {} #dict grafın kenarları
        self.huristics = () #tuple grafın maliyetleri
        self.directed = directed #bool t or f

    def add_edge(self, nodel, node2, cost = 1, reversed=False): 
        try: neighbors = self.edges[nodel]
        except KeyError: neighbors = {}
        
        neighbors[node2]=cost

        self.edges[nodel] = neighbors

        if not self.directed and not reversed: self.add_edge (node2, nodel, cost, True)

    def set_haristics (self, huristics={}): 
        self.huristics = huristics

    def neighbors (self, node): 
        try: return self.edges[node] 
        except KeyError: return []

    def cost (self, nodel, node2):

        try: return self.edges[nodel][node2] 
        except: return inf

    @staticmethod
    def print_path(came_from, goal): 
        parent = came_from[goal]
        if parent:

            Graph.print_path (came_from, parent) 
        else: print (goal, end='');return 
        print('=>', goal, end='')

    def _str_(self): 
        return str(self.edges)
    
    def breadth_first_search (self, start, goal):

        print("Breadth First Search")
        found, fringe, visited, came_from= False, deque([start]), set([start]), {start: None}
        print('{:11s} | {}'.format('Expand Node', 'Fringe'))

        print('-------------------------------------')
        print('{:11s} | {}'.format('-', start))

        while not found and len (fringe):

            current = fringe.pop()

            print('{:11s}'.format (current), end=' | ')

            if current == goal: found = True; break 
            for node in self.neighbors (current):

                if node not in visited: visited.add(node); fringe.appendleft (node); came_from[node]=current

            print(''.join(fringe))

        if found: print(); return came_from
        else: print('No path from {} to {}'.format(start, goal))