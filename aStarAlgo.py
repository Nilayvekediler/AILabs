graph = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Oradea': 71, 'Arad': 75},
    'Oradea': {'Sibiu': 151, 'Zerind': 71},
    'Sibiu': {'Fagaras': 99, 'Rimnicu Vilcea': 80, 'Arad': 140, 'Oradea': 151},
    'Timisoara': {'Lugoj': 111, 'Arad': 118},
    'Lugoj': {'Mehadia': 70, 'Timisoara': 111},
    'Mehadia': {'Drobeta': 75, 'Lugoj': 70},
    'Drobeta': {'Craiova': 120, 'Mehadia': 75},
    'Craiova': {'Rimnicu Vilcea': 146, 'Drobeta': 120, 'Pitesti': 138},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Fagaras': {'Bucharest': 211, 'Sibiu': 99},
    'Pitesti': {'Bucharest': 101, 'Rimnicu Vilcea': 97, 'Craiova': 138},
    'Bucharest': {'Giurgiu': 90, 'Urziceni': 85, 'Pitesti': 101, 'Fagaras': 211},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Vaslui': 142, 'Hirsova': 98, 'Bucharest': 85},
    'Hirsova': {'Eforie': 86, 'Urziceni': 98},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Iasi': 92, 'Urziceni': 142},
    'Iasi': {'Neamt': 87, 'Vaslui': 92},
    'Neamt': {'Iasi': 87}
}

heuristics = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Drobeta': 242,
    'Eforie': 161,
    'Fagaras': 178,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 98,
    'Rimnicu Vilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374
}

def aStarAlgo(start, end):
    myList = [(0 + heuristics[start], start)]
    closedList = []
    path = {}
    cost = {}
    path[start] = None
    cost[start] = 0

    while len(myList) > 0:
        myList.sort()
        current = myList.pop(0)[1]
        if current == end:
            path_list = []
            while current is not None:
                path_list.append(current)
                current = path[current]
            path_list.reverse()
            return path_list, cost[end]
        
        closedList.append(current)

        for neighbor, neighbor_cost in graph[current].items():
            if neighbor in closedList:
                continue
            new_cost = cost[current] + neighbor_cost

            if neighbor not in [item[1] for item in myList]:
                cost[neighbor] = new_cost
                priority = new_cost + heuristics[neighbor]
                myList.append((priority, neighbor))
                path[neighbor] = current

            else:
                for i, item in enumerate(myList):
                    if item[1] == neighbor:
                        if cost[neighbor] > new_cost:
                            cost[neighbor] = new_cost
                            priority = new_cost + heuristics[neighbor]
                            myList[i] = (priority, neighbor)
                            path[neighbor] = current
                        break

    return None #bulamazsak

path, cost = aStarAlgo('Arad', 'Bucharest')
print('Yol:', path)
print('Maliyet:', cost)