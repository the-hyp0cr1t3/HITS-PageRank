from src.Graph import Graph
import numpy as np
import numpy.typing as npt
from numpy import linalg as LA

class PageRank:
	"""Given a directed graph, computes the page ranks of each node

	Attributes:
		g (Graph): A directed graph
		alpha (np.float64): The random vertex teleport probability (zero if not allowed)
		iterations (int): The number of iterations to perform in matrix power method, None otherwise
		prob_matrix (npt.NDArray[np.float64]): The computed NxN transition probability matrix
		pageranks (npt.NDArray[np.float64]): The pageranks of the nodes
	"""
	g: Graph
	alpha: np.float64
	iterations: int
	prob_matrix: npt.NDArray[np.float64]
	pageranks: npt.NDArray[np.float64]

	def __init__(self, g: Graph, teleport_prob: np.float64, iterations: int) -> None:
		"""Constructor

		Args:
			g (Graph): A directed graph
			teleport_prob (np.float64): The probability to teleport to a random node (alpha)
			iterations (int): The number of iterations to perform in matrix power method, None otherwise
		"""
		self.g = g
		self.alpha = teleport_prob
		self.iterations = iterations
		self.build()

	def build(self) -> npt.NDArray[np.float64]:
		"""Builds the transition probability matrix and computes the pageranks of each node

		Returns:
			npt.NDArray[np.float64]: The pageranks of the nodes
		"""
		# here prob_matrix[i, j] = alpha / n + adj[i, j] * (1 - alpha) / sum(adj[i])
		f = lambda i, j: self.alpha / self.g.n + (0.0 if sum(self.g.adj[i]) == 0 else self.g.adj[i, j] * (1 - self.alpha) / sum(self.g.adj[i]))
		# vectorize creation using the above lambda to create the NxN transition probability matrix
		self.prob_matrix = np.fromfunction(np.vectorize(f), (self.g.n, self.g.n), dtype=int)

		# print(self.prob_matrix)

		# finding principal left eigenvector
		if self.iterations: # using power iteration method if iterations are specified
			principal_left_eig = np.dot(np.ones(self.g.n), LA.matrix_power(self.prob_matrix, self.iterations))
		else:			   # directly compute using linear algebra
			eigvalues, eigvectors = LA.eig(self.prob_matrix.T)
			principal_left_eig = eigvectors[:, np.argmax(eigvalues)].T

		# normalize
		self.pageranks = principal_left_eig / sum(principal_left_eig)

		return self.pageranks

	def __str__(self) -> str:
		"""String representation of the object

		Returns:
			str: The string representation of the page ranks for nice printing
		"""
		return self.pageranks.__str__()


