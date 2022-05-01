import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from Graph import Graph
from typing import Tuple, List, Set, DefaultDict
from collections import defaultdict

nltk.download('punkt')
nltk.download('stopwords')

def tokenize(data: str) -> List[str]:
	"""Preprocesses and tokenizes a string using nltk (stop word removal and stemming)

	Args:
		data (str): The data to be tokenized

	Returns:
		List[str]: A list of tokens after preprocessing
	"""

	# get tokens using nltk tokenize
	tokens = nltk.word_tokenize(data)

	# initialize stemmer
	stemmer = PorterStemmer()

	# stemming and removing duplicates
	filtered_tokens = [
		stemmer.stem(tok) for tok in tokens if tok not in stopwords.words("english")
	]
	filtered_tokens = list(set(filtered_tokens))

	return filtered_tokens


def build_inv_idx_table(docs: List[str]) -> DefaultDict[str, Set[int]]:
	"""Builds an inverted index table on the word tokens within each document

	Args:
		docs (List[str]): A list of documents

	Returns:
		DefaultDict[str, Set[int]]: The inverted index table
	"""
	inv_idx: DefaultDict[str, Set[int]] = defaultdict(set)

	for doc_id, doc in enumerate(docs):
		for tok in tokenize(doc):
			inv_idx[tok].add(doc_id)

	return inv_idx


def find_base_set(g: Graph, inv_idx: DefaultDict[str, Set[int]], query: List[str]):
	"""Finds the base set by first finding the root set from the query and then extending it

	Args:
		g (Graph): A directed graph
		inv_idx (DefaultDict[str, Set[int]]): The inverted index table
		query (List[str]): The tokenized list of query terms

	Returns:
		Graph: An induced subgraph of g, the base set
	"""

	# Constructing the root set
	is_root_set = [False] * g.n
	for word in query:
		if word in inv_idx:
			for docid in inv_idx[word]:
				is_root_set[docid] = True
		else:
			print(f'No occurrences of {word} found.')

	# Constructing the base set by extending root set
	base = Graph(g.n)
	is_base_set = is_root_set.copy()
	for u, v in g.edge_list:
		if is_root_set[u]: 			# u ∈ root set, add child v to base set
			is_base_set[v] = True
		elif is_root_set[v]:		# v ∈ root set, add parent u to base set
			is_base_set[u] = True
		if is_base_set[u] and is_base_set[v]:
			base.add_edge(u, v)

	return base