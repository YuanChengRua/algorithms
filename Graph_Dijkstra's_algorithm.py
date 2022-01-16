'''
For BFS algorithm, we all the edges have the same weight and so we only need to find the path which contains the smallest number of edges.
But when the edges have weights, we need to find the path which has the smallest weights
Note Dijkstra can only be used for directed acyclic graph

Dijkstra's step:
    1. From the chosen v1, we initially store the weights as inf except its neighbors
    2. From the chose v1, we choose the smallest weight and move to the next point v2
    3. Since the next point v2 has its neighbors, for example, v3, we can replace the inf weight (v1->v2->v3) with the w(v1->v2) + w(v2->v3)
    4. Suppose the distance between v2 to v3 is the smallest, we move from v2 to v3 so we can update the distance from v1 to v3's neighbors v4 v5 v6...
    5. we need to ensure that we have gone through all the v then we can end the algorithm.
'''