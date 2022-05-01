#!/usr/bin/env python3
import os
import networkx as nx
import pandas as pd
from random import randint
from datetime import timedelta
from timeit import timeit
from Graph import Graph
from PageRank import PageRank
from HITS import HITS

n_min = 2
n_max = 150
iters_ls = [10, 50, 100, 150, 200, 250, 300, 400]
DATA_PATH = os.path.join("data", "benchmarks")

for iters in iters_ls:
    print(f'iters = {iters}')
    res = []

    for n in range(2, 150, 2):
        m = randint(1, n * (n - 1))
        G = nx.gnm_random_graph(n, m, seed=42, directed=True)

        graph = Graph(n)
        for u, v in G.edges():
            graph.add_edge(u, v)

        # print(graph)

        pgrktm = timeit(lambda: PageRank(graph, 0.1, iters), number=10)
        hitstm = timeit(lambda: HITS(graph, iters), number=10)
        print(f'n: {n} took {pgrktm * 1000:.5f} ms, {hitstm * 1000:.5f} ms')

        res.append([n, pgrktm * 1000, hitstm * 1000])

    df = pd.DataFrame(res, columns =['n', 'pagerank run_time (ms)', 'hits run_time (ms)'])
    df.to_csv(os.path.join(DATA_PATH, f'n({n_min}-{n_max})_iters({iters}).csv'), index=False)

"""
Pagerank:
- n^3                   (direct via eigen vectors)
- n^3 * log(iters)      (power iteration via binary exponentiation)

HITS:
- n^2 * iters

"""