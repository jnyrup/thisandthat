# encoding: utf-8

import networkx as nx,sys

def decomp(G):
	if hasattr(G,'graph') and isinstance(G.graph,dict):
		Gres = nx.DiGraph()
		decomp1(G,Gres)
		return Gres
	else:
		raise nx.NetworkXError("Input is not a correct NetworkX graph.")

def decomp1(G,Gres):
	# list of modules from complement graph
	modules = nx.connected_component_subgraphs(nx.complement(G))
	if len(modules) == 1:
		if len(modules[0].nodes()) == 1:
			#return leaf node
			return modules[0].nodes()[0]
		else:
			raise nx.NetworkXUnfeasible("input graph is not a valid cograph and corresponding cotree cannot be computed")
	else:
		children = [decomp1(module,Gres) for module in modules]
		# add internal node and connect all trees above as children
		root = 'a'+children[0] # a good way to make a new unused node?
		Gres.add_node(root,label='')
		Gres.add_edges_from([(root,child) for child in children])
		#return new internal root node
		return root

##read matrix from file
filename = sys.argv[1]
G = nx.Graph()
f = open(filename,'r')
n = int(f.readline())
names = ['g'+str(x+1) for x in xrange(n)]

i=0
for line in f:
	j = i
	for char in line:
		if char != ' ' and char != '\t': #strip spaces and tabs
			j += 1
			if char == '1':
				G.add_nodes_from([names[i],names[j]],layer=0)
				G.add_edge(names[i],names[j])
	i += 1

#calculate cotree
Gres = decomp(G)
A = nx.to_agraph(G)
A.layout('dot',args='-Gmargin=0 -Earrowhead=none')
A.draw(filename+'-cograph.pdf')
A = nx.to_agraph(Gres)
A.layout('dot',args='-Gmargin=0 -Gsplines=false -Earrowhead=none')
A.draw(filename+'-cotree.pdf')
