import sys
from functools import lru_cache
from tail_recursion import tail_recursive

NO_PATH = sys.maxsize
graph = [
    [0, 7, NO_PATH, 8],
    [NO_PATH, 0, 5, NO_PATH],
    [NO_PATH, NO_PATH, 0, 2],
    [NO_PATH, NO_PATH, NO_PATH, 0]
    ]


def floyd_recursive(distance):
    """Prints the
    """
    # Find the number of nodes in the graph matrix.
    max_length = len(distance[0])

    @lru_cache(maxsize=None)
    @tail_recursive
    def shortest_distance(i, j, k):
        """Returns the shortest distance between nodes i and j using recursion.

        Arguments:
        i -- the start node
        j -- the end node
        k -- the intermediary node
        """
        # Recursion base case to stop the recursion.
        if k < 0:
            return distance[i][j]

        #print(i, j, k)
        # Recursive case to find the shortest distance.
        return min(shortest_distance(i, j, k-1),
                   shortest_distance(i, k, k-1) +
                   shortest_distance(k, j, k-1))

    for k in range(max_length):
        for i in range(max_length):
            for j in range(max_length):
                #Condition
                if i == j:
                    distance[i][j] = 0
                    continue
                distance[i][j] = shortest_distance(i, j, k)

    return distance


if __name__ == '__main__':
    # Call the function and pass the graph matrix.
    print(floyd_recursive(graph))
