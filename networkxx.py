import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()
g.add_node('Miyagi')
g.add_nodes_from(['Aomori','Iwate','Akita','Yamagata','Fukushima'])

g.add_edge("Miyagi", "Fukushima", weight=68)

g.add_weighted_edges_from([('Iwate','Aomori',129),('Akita','Aomori',134),('Iwate','Akita',90),('Yamagata','Akita',166),('Yamagata','Fukushima',55),('Miyagi','Yamagata',45),('Miyagi','Iwate',161),('Miyagi','Fukushima',68)])

#nx.draw_networkx(g)
#plt.savefig("figure10.png")

tg = nx.minimum_spanning_tree(g)
nx.draw_networkx(tg)
plt.savefig("figure11.png")
