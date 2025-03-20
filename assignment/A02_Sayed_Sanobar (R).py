#r: networkx
#r: matplotlib

import networkx as nx #type: ignore
import matplotlib.pyplot as plt #type: ignore

#create a Graph
G = nx.Graph()

#add nodes
G.add_node('Veranda')
G.add_node('Foyer')
G.add_node('Formal Living')
G.add_node('Family Living')
G.add_node('Dining')
G.add_node('Kitchen')
G.add_node('Utility')
G.add_node('Bedroom')
G.add_node('Bathroom')
G.add_node('Passage')
G.add_node('Closet')
G.add_node('Patio')

#add edges
G.add_edge('Veranda', 'Foyer')
G.add_edge('Foyer', 'Formal Living')
G.add_edge('Foyer', 'Passage')
G.add_edge('Formal Living', 'Patio')
G.add_edge('Passage', 'Family Living')
G.add_edge('Family Living', 'Dining')
G.add_edge('Family Living', 'Patio')
G.add_edge('Dining', 'Kitchen')
G.add_edge('Passage', 'Kitchen')
G.add_edge('Kitchen', 'Utility')
G.add_edge('Dining', 'Patio')
G.add_edge('Passage', 'Bedroom')
G.add_edge('Bedroom', 'Bathroom')
G.add_edge('Bedroom', 'Closet')


#add position to display
pos = nx.spring_layout(G)

#draw serttings
fig = plt.figure(figsize=(10,10))
ax = plt.subplot()
ax.set_title('Residential Bubble Diagram', fontsize=20, fontweight='bold', color='Grey', loc='center')
nx.draw(G, pos, node_size=6000, with_labels=True, node_color='red', font_size=9, font_color='white', font_weight='bold', edge_color='black', width=2)

#draw the graph
plt.tight_layout()


#plot
path= r"C:\Users\Sayed\Desktop\S2\images\MDPA_plot1.png"
plt.savefig(path, format="PNG")
