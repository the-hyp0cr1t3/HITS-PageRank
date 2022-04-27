from Graph import Graph
from typing import Tuple
import numpy as np
import numpy.typing as npt
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
        self.build()

    def build(self) -> Tuple[npt.NDArray[np.float64], npt.NDArray[np.float64]]:
        """Computes the hub and authority values of the nodes after the specified number of iterations

        Returns:
            Tuple[npt.NDArray[np.float64], npt.NDArray[np.float64]]: The hub and authority values of the nodes after the specified number of iterations
        """
        self.hub = np.ones((self.g.n,), dtype=np.float64)
        self.authority = np.ones((self.g.n,), dtype=np.float64)

        self.g.adj_T = self.g.adj.T
        for _ in repeat(None, self.iterations):
            # hub  = adj . auth
            # auth = adjT . hub
            self.hub = np.dot(self.authority, self.g.adj)
            self.authority = np.dot(self.hub, self.g.adj_T)

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