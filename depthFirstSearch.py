import networkx as nx
import random
import matplotlib.pyplot as plt

text = "nilaye" #nilay inel

G = nx.Graph() # Boş bir graf oluşturma

for char in text: # nilaye nin her harfini grafa ekleme
    G.add_node(char)

for i in range(len(text)): # düğümlerin rastgele bağlanması
    for j in range(i + 1, len(text)):
        if random.random() < 0.5:
            G.add_edge(text[i], text[j])
    

for node in G.nodes: # bağlantısız bağımsız düğüm kalmasını önlemek için
    if G.degree(node) == 0:
        other_node = random.choice(list(G.nodes))
        G.add_edge(node, other_node)
        while other_node == node:
            other_node = random.choice(list(G.nodes))
            G.add_edge(node, other_node)


nx.draw(G,node_color='pink', font_color='black', node_size=500,with_labels=True) # grafiği çizdirmek için networkx kütüphanesi kullanılır

visited = set() # gezilen düğümlerin tutulduğu set

def depthFirstSearch(visited, graph, startNode):  
    stack = [startNode] # stack isimli bir liste başlangıç node u eleman olarak atanır
    while stack:
        node = stack.pop() # stack in en üstündeki node a atanır
        if node not in visited: # eğer o node daha önce ziyaret edilmediyse
            print(node, end=" -> ")
            visited.add(node)
            stack.extend(reversed(sorted(graph[node])))  # alfabetik sıralama


print("n, i, l, a, y, e harfleriyle rastgele bir graf oluşturulacaktır.")
harf=input("Başlangıç düğümü harfi giriniz: ")

print("Depth First Search Algoritmasının Bulduğu Yol :") 
depthFirstSearch(visited, G, harf) 
print("")
plt.show() # grafı göster.

