import sys
import cProfile
from floydwarshall.floyd_warshall import floyd_recursive

NO_PATH = sys.maxsize
graph = [
    [0, 7, NO_PATH, 8],
    [NO_PATH, 0, 5, NO_PATH],
    [NO_PATH, NO_PATH, 0, 2],
    [NO_PATH, NO_PATH, NO_PATH, 0]
    ]

cProfile.run("floyd_recursive(graph)")
