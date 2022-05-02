from src.Graph import Graph
from typing import List, Tuple
import numpy as np
import numpy.typing as npt
from numpy import linalg as LA
from itertools import repeat

class HITS:
	"""Given a directed graph, computes the hub and authority values of the nodes after a specified number of iterations

	Attributes:
		g (Graph): A directed graph
		iterations (int): The number of iterations to run the algorithm for
		hub (npt.NDArray[np.float64]): The hub values of the nodes after specified no. of iterations
		authority (npt.NDArray[np.float64]): The authority values of the nodes after specified no. of iterations
	"""
	g: Graph
	iterations: int
	hub: npt.NDArray[np.float64]
	authority: npt.NDArray[np.float64]

	def __init__(self, g: Graph, iterations: int) -> None:
		"""Constructor

		Args:
			g (Graph): A directed graph
			iterations (int): The number of iterations to run the algorithm for
		"""
		self.g = g
		self.iterations = iterations
		self.hub = np.ones(self.g.n)
		self.authority = np.ones(self.g.n)
		self.build()

	def build(self) -> Tuple[npt.NDArray[np.float64], npt.NDArray[np.float64]]:
		"""Computes the hub and authority values of the nodes after the specified number of iterations

		Returns:
			Tuple[npt.NDArray[np.float64], npt.NDArray[np.float64]]: The hub and authority values of the nodes after the specified number of iterations
		"""
		adj_adjT = np.matmul(self.g.adj, self.g.adj.T)
		adjT_adj = np.matmul(self.g.adj.T, self.g.adj)

		# self.hub = np.dot(LA.matrix_power(adj_adjT, self.iterations), self.hub)
		# self.authority = np.dot(LA.matrix_power(adjT_adj, self.iterations), self.authority)

		# # normalize
		# self.hub /= sum(self.hub)
		# self.authority /= sum(self.authority)

		for _ in repeat(None, self.iterations):
			self.hub = np.matmul(adj_adjT, self.hub)
			self.authority = np.matmul(adjT_adj, self.authority)

			# normalize
			self.hub /= sum(self.hub)
			self.authority /= sum(self.authority)

		return self.hub, self.authority

	def __str__(self) -> str:
		"""String representation of the object

		Returns:
			str: The string representation of the hub and authority values of each node for nice printing
		"""
		return f'hub = {self.hub}\nauthority = {self.authority}\n'