from Graph import Graph
from typing import Tuple, List, Set, DefaultDict
from collections import defaultdict

def build_inv_idx_table(docs: List[str]) -> DefaultDict[str, Set[int]]:
	inv_idx = defaultdict(Set[int])
	# print(f'docs\n{type(docs[0])}')
	for idx, doc in enumerate(docs):
		for word in doc.split():
			if word not in inv_idx:
				inv_idx[word] = set()
			inv_idx[word].add(idx) 

	return inv_idx

def find_root_set(g: Graph, inv_idx_table: DefaultDict[str, Set[int]], query: List[str]):
	is_root_set = [False] * g.n
	for word in query:
		if word not in inv_idx_table:
			continue
		for docid in inv_idx_table[word]:
			is_root_set[docid] = True

	is_base_set = is_root_set.copy()
	for i in range(g.n):
		for j in range(g.n):
			if not g.adj[i, j]: continue
			if is_root_set[i]:
				is_base_set[j] = True
			elif is_root_set[j]:
				is_base_set[i] = True

	base = Graph(g.n)

	for i in range(g.n):
		for j in range(i, g.n):
			if g.adj[i, j] and is_base_set[i] and is_base_set[j]:
				base.add_edge(i, j)

	return base