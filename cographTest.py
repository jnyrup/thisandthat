import networkx as nx
from cographs import *

# adjacencyList forms a connected cograph
adjacencyList = [(1, 6),
         (1, 7),
         (1, 8),
         (1, 9),
         (1, 11),
         (1, 12),
         (2, 6),
         (2, 7),
         (2, 8),
         (2, 9),
         (2, 11),
         (2, 12),
         (3, 6),
         (3, 7),
         (3, 8),
         (3, 9),
         (3, 10),
         (1, 6),
         (4, 6),
         (4, 7),
         (4, 8),
         (4, 9),
         (4, 11),
         (4, 12),
         (5, 6),
         (5, 7),
         (5, 8),
         (5, 9),
         (5, 10),
         (6, 10),
         (6, 11),
         (6, 12),
         (7, 10),
         (7, 11),
         (7, 12),
         (8, 10),
         (8, 11),
         (8, 12),
         (9, 10),
         (9, 11),
         (9, 12)]
G = nx.Graph()
G.add_edges_from(adjacencyList)


# 1: Test a regular cograph
# 1a: Test if G is a cograph
if isCograph(G):
    print "1a: Success"
else:
    print "1a: Fail"

# 1b: Test modular decomposition
Gres = modularDecomposition(G)
A = nx.to_agraph(G)
A.layout('dot', args='-Gmargin=0 -Earrowhead=none')
A.draw('cograph-1b.pdf')
A = nx.to_agraph(Gres)
A.layout('dot', args='-Gmargin=0 -Gsplines=false -Earrowhead=none')
A.draw('cotree-1b.pdf')
print "Verify cograph-1b.pdf and cotree-1b.pdf manually"


# 2: Tests a non-connected cograph
# 2a: Test if G is a cograph
Gp = nx.complement(G)
if isCograph(G):
    print "2: Success"
else:
    print "2: Fail"
# 2b: Test modular decomposition
Gres = modularDecomposition(Gp)
A = nx.to_agraph(Gp)
A.layout('dot', args='-Gmargin=0 -Earrowhead=none')
A.draw('cograph-2b.pdf')
A = nx.to_agraph(Gres)
A.layout('dot', args='-Gmargin=0 -Gsplines=false -Earrowhead=none')
A.draw('cotree-2b.pdf')
print "Verify cograph-2b.pdf and cotree-2b.pdf manually"


# 3: Tests a non-cograph
# 3a: Test if G is a cograph
G.remove_edge(4, 6)
if isCograph(G):
    print "3a: Fail"
else:
    print "3a: Success"
# 2b: Test modular decomposition. Should raise an exception
try:
    Gres = modularDecomposition(G)
except nx.NetworkXUnfeasible:
    print "3: Success - an exception was raised"
