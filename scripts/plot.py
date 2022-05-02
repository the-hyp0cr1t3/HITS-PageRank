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

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, constrained_layout=True)

for idx, iters in enumerate(iters_ls):
	df = pd.read_csv(os.path.join(DATA_PATH, f'n({n_min}-{n_max})_iters({iters}).csv'))

	ax1.plot(df['n'], df['pagerank run_time (ms)'], label=f'{iters} iterations')
	ax2.plot(df['n'], df['pagerank run_time (ms)'] ** (1/3), label=f'{iters} iterations')
	ax3.plot(df['n'], df['hits run_time (ms)'], label=f'{iters} iterations')
	ax4.plot(df['n'], df['hits run_time (ms)'] ** (1/2), label=f'{iters} iterations')

ax1.text(x=52, y=10400, fontsize='12', color='grey', s='$\\mathcal{O}(n^3)$ or $\\mathcal{O}(n^3 \\cdot \\mathrm{log}_2(iterations))$')
ax1.set_title('PageRank execution time vs n', fontsize='15')
ax1.legend(loc="upper left")
ax1.set_xlabel('n')
ax1.set_ylabel('PageRank execution time (ms)')

ax2.set_title('Cube root of PageRank execution time vs n\nshowing approximately linear relationship', fontsize='15', wrap=True)
ax2.legend(loc="upper left")
ax2.set_xlabel('n')
ax2.set_ylabel('Cube root of PageRank execution time (ms)')

ax3.text(x=63, y=550, fontsize='12', color='grey', s='$\\mathcal{O}(n^2 \\cdot iterations)$')
ax3.set_title('HITS execution time vs n', fontsize='15')
ax3.legend(loc="upper left")
ax3.set_xlabel('n')
ax3.set_ylabel('HITS execution time (ms)')

ax4.set_title('Square root of HITS execution time vs n\nshowing approximately linear relationship', fontsize='15', wrap=True)
ax4.legend(loc="upper left")
ax4.set_xlabel('n')
ax4.set_ylabel('Square root of HITS execution time (ms)')

# plt.subplot_tool()
plt.show()