#!/usr/bin/env python3
import os
from typing import Tuple, List
import numpy as np
import numpy.typing as npt
import networkx as nx

class Graph:
	"""A simple graph class

	Attributes:
		n (int): The order of the graph
		m (int): The size of the graph
		adj (npt.NDArray[np.ubyte]): The adjacency matrix
		edge_list (List[List[int]]): The list of edges
	"""
	n: int = 0
	m: int = 0
	adj: npt.NDArray[np.ubyte]
	edge_list: List[List[int]] = None

	def __init__(self, n: int = 0):
		"""Constructor

		Args:
			n (int, optional): The order of the graph. Defaults to 0.
		"""
		self.n = n
		self.adj = np.zeros(shape=(n, n), dtype=np.ubyte)

	def __str__(self) -> str:
		"""String representation of the object

		Returns:
			str: The string representation of the graph for nice printing
		"""
		res = f'n = {self.n}, m = {self.m}\n'
		res += f'edge_list:\n{self.edge_list}\n'
		res += f'adj_list:\n{self.adj}\n'

		return res

	def add_edge(self, u: int, v: int) -> None:
		"""Adds a directed edge to the graph.

		Args:
			u (int): The source node
			v (int): The destination node
		"""
		self.m += 1
		self.adj[u, v] = 1
		if not self.edge_list:
			self.edge_list = []
		self.edge_list.append([u, v])

	def read_gpickle(self, filename: str) -> List[str]:
		"""Reads graphs from files in gpickle format and returns the associated data/documents if any

        Args:
			filename (str): The path to the file to be read

        Returns:
            List[str]: A list of documents corresponding to the nodes
        """

		graph = nx.read_gpickle(filename)
		self.n = len(graph.nodes())
		self.m = len(graph.edges())
		self.adj = nx.to_numpy_array(graph, dtype=np.ubyte)
		self.edge_list = []
		for u, v in graph.edges():
			self.edge_list.append([u, v])

		docs = nx.get_node_attributes(graph, 'page_content')
		return None if not docs else [ docs[i] for i in range(self.n) ]

	def read_graph(self, filename: str) -> None:
		"""Reads graphs from files in the format

		\\(n \\, m\\)

		\\(u_1 \\, v_1\\)

		\\(u_2 \\, v_2\\)

		.

		.

		\\(u_m \\, v_m\\)

		Args:
			filename (str): The path to the file to be read
		"""
		with open(filename, "r") as infile:
			lines = infile.readlines()
			self.n, self.m = (int(i) for i in lines[0].split())
			self.edge_list = [[int(i) for i in line.split()] for line in lines[1:]]
			self.adj = self.build_adj_matrix_from_edgelist(self.n, self.m, self.edge_list)


	def build_adj_matrix_from_edgelist(self, n: int, m: int, edge_list: List[List[int]]) -> npt.NDArray[np.ubyte]:
		"""Builds the adjacency matrix given the order, size and list of edges

		Args:
			n (int): The order of the graph
			m (int): The size of the graph
			edge_list (List[List[int]]): The list of edges

		Returns:
			npt.NDArray[np.ubyte]: A 2D adjaceny matrix
		"""
		assert n > 0, f"Number of nodes must be positive, found n = {n}"
		assert m >= 0, f"Number of edges must be non-negative, found m = {m}"
		assert m == len(edge_list), "m does not match size of edge_list"

		adj_list = np.zeros(shape=(n, n), dtype=np.ubyte)

		for u, v in edge_list:
			assert 0 <= u and u < n, f"Node id out of bounds, found u = {u}"
			assert 0 <= v and v < n, f"Node id out of bounds, found v = {v}"

			adj_list[u, v] = 1

		return adj_list


if __name__ == "__main__":
	DATA_PATH = "data"
	g = Graph()
	g.read_gpickle(os.path.join(DATA_PATH, "HITS_web_graph.gpickle"))
	print(g)

	g.read_graph(os.path.join(DATA_PATH, "sample.txt"))
	g.add_edge(0, 1)
	print(g)