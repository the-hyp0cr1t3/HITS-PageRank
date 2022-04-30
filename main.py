#!/usr/bin/env python3
import os
import argparse
from sys import argv
from Graph import Graph
from PageRank import PageRank
from HITS import HITS
from numpy import float64
from utils import tokenize, build_inv_idx_table, find_base_set

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("mode", choices=["pagerank", "hits"], help="run the PageRank or the HITS algorithm")
	parser.add_argument("-nt", "--no_teleports", action="store_true", help="run the pagerank algorithm without random teleports")
	parser.add_argument("-tp", "--teleport_prob", type=float64, default=0.1, help="specify the teleport probability")
	parser.add_argument("-it", "--iterations", type=int, default=None, help="specify the number of iterations")
	parser.add_argument("-f", "--file", required=True, help="specify the input graph file")
	args = parser.parse_args()

	if args.mode != 'pagerank' and ("--teleport_prob" in argv or "-tp" in argv):
		parser.error('--teleport_prob can only be set when in pagerank mode')
	if args.mode != 'pagerank' and args.no_teleports:
		parser.error('--no_teleports can only be set when in pagerank mode')
	if args.no_teleports and args.teleport_prob:
		parser.error('--teleport_prob can only be set when teleports are allowed')
	if args.mode == 'hits' and not args.iterations:
		parser.error('--iterations is required when in hits mode')

	if args.no_teleports:
		args.teleport_prob = 0.0

	if os.path.exists(os.path.join("data", args.file)):
		args.file = os.path.join("data", args.file)

	graph = Graph()
	if args.file.endswith('gpickle'):
		docs = graph.read_gpickle(args.file)
		if docs:
			inv_idx = build_inv_idx_table(docs)
	else:
		graph.read_graph(args.file)


	if args.mode == 'pagerank':
		print(PageRank(graph, args.teleport_prob, args.iterations))

	elif args.mode == 'hits':
		assert inv_idx, "Inverted index table could not be built."
		query = input('Enter query expression: ')
		graph = find_base_set(graph, inv_idx, tokenize(query))
		print(HITS(graph, args.iterations))