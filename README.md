# HITS & PageRank Implementation
This is an implementation of the [HITS](https://en.wikipedia.org/wiki/HITS_algorithm) and [PageRank](https://en.wikipedia.org/wiki/PageRank) algorithms from scratch.

To install dependencies
```sh
pip install -r requirements.txt
```

## Usage

```bash
./main.py [-h] [-nt] [-tp TELEPORT_PROB] [-it ITERATIONS] -f FILE {pagerank,hits}
```

#### Options:
```brainfuck
positional arguments:
  {pagerank,hits}       run the PageRank or the HITS algorithm

optional arguments:
  -h, --help            show this help message and exit
  -nt, --no_teleports   run the pagerank algorithm without random teleports
  -tp TELEPORT_PROB, --teleport_prob TELEPORT_PROB
                        specify the teleport probability
  -it ITERATIONS, --iterations ITERATIONS
                        specify the number of iterations
  -f FILE, --file FILE  specify the input graph file
```

#### Examples:
```
# Run HITS algorithm
./main.py hits --file HITS_web_graph.gpickle --iterations 50

# Run PageRank algorithm with random teleportations using power iteration method
./main.py pagerank --file sample.txt --teleport_prob 0.23 --iterations 100

# Run PageRank algorithm with random teleportations using linear algebra packages (do not specify iterations)
./main.py pagerank --file sample.txt    # teleport_prob is 0.1 by default if not specified

# Run PageRank algorithm without random teleportations using power iteration method
./main.py pagerank --file sample.txt --no_teleports --iterations 100

# Run PageRank algorithm without random teleportations using linear algebra packages (do not specify iterations)
./main.py pagerank --file sample.txt --no_teleports
```

**Note:** `--file` must be in `./data`.