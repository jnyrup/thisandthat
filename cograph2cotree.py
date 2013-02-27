# encoding: utf-8
"""Algorithms regarding cographs."""
import networkx as nx
__author__ = """\n""".join(['Jonas NYrup <jnyrup@gmail.com>'])
__all__= ['modularDecomposition', 'isCograph']

def modularDecomposition(G):
	""" Computes the cotree of a cograph.
	This is done by modular decomposition - http://en.wikipedia.org/wiki/Modular_decomposition

	Parameters
	----------
	G : graph
		A networkx graph
		As cotrees can only be computed for cographs an error is raised if the input graph is not a cograph

	Returns
	-------
	out : graph
		The resulting cotree
	"""
	if hasattr(G,'graph') and isinstance(G.graph,dict):
		Gres = nx.DiGraph()
		decomp(G,Gres)
		return Gres
	else:
		raise nx.NetworkXError("Input is not a correct NetworkX graph.")

def decomp(G, Gres):
	# list of modules from complement graph
	modules = nx.connected_component_subgraphs(nx.complement(G))
	if len(modules) == 1:
		if len(modules[0].nodes()) == 1:
			#return leaf node
			return modules[0].nodes()[0]
		else:
			raise nx.NetworkXUnfeasible("input graph is not a valid cograph and corresponding cotree cannot be computed")
	else:
		children = [decomp(module, Gres) for module in modules]
		# add internal node and connect all trees above as children
		root = 'a'+str(children[0]) # a good way to make a new unused node?
		Gres.add_node(root,label='')
		Gres.add_edges_from([(root, child) for child in children])
		#return new internal root node
		return root

def isCograph(G):
	""" Determines whether G is a valid cograph
	Parameters
	----------
	G : graph
		A networkx graph

	Returns
	-------
	out : bool
		Boolean stating whether input graph is a valid cograph
	"""
	modules = nx.connected_component_subgraphs(nx.complement(G))
	if len(modules) == 1:
		if len(modules[0].nodes()) == 1:
			#return leaf node
			return True
		else:
			return False
	else:
		return all(isCograph(module) for module in modules)
