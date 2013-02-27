import networkx as nx
from cograph2cotree import *


list1=[(1,6),
(1,7),
(1,8),
(1,9),
(1,11),
(1,12),
(2,6),
(2,7),
(2,8),
(2,9),
(2,11),
(2,12),
(3,6),
(3,7),
(3,8),
(3,9),
(3,10),
(1,6),
(4,6),
(4,7),
(4,8),
(4,9),
(4,11),
(4,12),
(5,6),
(5,7),
(5,8),
(5,9),
(5,10),
(6,10),
(6,11),
(6,12),
(7,10),
(7,11),
(7,12),
(8,10),
(8,11),
(8,12),
(9,10),
(9,11),
(9,12)]


G = nx.Graph()
G.add_edges_from(list1)
print isCograph(G)
Gres = decomp(G)
A = nx.to_agraph(G)
A.layout('dot',args='-Gmargin=0 -Earrowhead=none')
A.draw('cograph.pdf')
A = nx.to_agraph(Gres)
A.layout('dot',args='-Gmargin=0 -Gsplines=false -Earrowhead=none')
A.draw('cotree.pdf')
