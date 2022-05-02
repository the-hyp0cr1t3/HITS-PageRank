#!/usr/bin/env python3
import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set_style("darkgrid")

n_min = 2
n_max = 150
iters_ls = [10, 50, 100, 150, 200, 250, 300]
DATA_PATH = os.path.join("..", "data", "benchmarks")

fig, ax = plt.subplots(2, 2, constrained_layout=True)
for idx, iters in enumerate(iters_ls):
    df = pd.read_csv(os.path.join(DATA_PATH, f'n({n_min}-{n_max})_iters({iters}).csv'))

    plt.subplot(2, 2, 1)
    plt.title('PageRank execution time vs n', fontsize='15')
    plt.plot(df['n'], df['pagerank run_time (ms)'], label=f'{iters} iterations')
    plt.legend(loc="upper left")
    plt.xlabel('n')
    plt.ylabel('PageRank execution time (ms)')

    plt.subplot(2, 2, 2)
    plt.title('Cube root of PageRank execution time vs n\nshowing approximately linear relationship', fontsize='15', wrap=True)
    plt.plot(df['n'], df['pagerank run_time (ms)'] ** (1/3), label=f'{iters} iterations')
    plt.legend(loc="upper left")
    plt.xlabel('n')
    plt.ylabel('Cube root of PageRank execution time (ms)')

    plt.subplot(2, 2, 3)
    plt.title('HITS execution time vs n', fontsize='15')
    plt.plot(df['n'], df['hits run_time (ms)'], label=f'{iters} iterations')
    plt.legend(loc="upper left")
    plt.xlabel('n')
    plt.ylabel('HITS execution time (ms)')

    plt.subplot(2, 2, 4)
    plt.title('Square root of HITS execution time vs n\nshowing approximately linear relationship', fontsize='15', wrap=True)
    plt.plot(df['n'], df['hits run_time (ms)'] ** (1/2), label=f'{iters} iterations')
    plt.legend(loc="upper left")
    plt.xlabel('n')
    plt.ylabel('Square root of HITS execution time (ms)')

# plt.subplot_tool()
plt.show()