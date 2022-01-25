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


'''
Implementation

We need 3 hashmaps: graph, cost, parents
'''

graph = {}  # This is a big hashmap
graph['start'] = {}
graph['start']['a'] = 6  # graph['start'] is also a hashmap
graph['start']['b'] = 2

graph['a'] = {}
graph['a']['fin'] = 1

graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5

graph['fin'] = {}

# define infinity
infinity = float("inf")

# cost hash means the distance from the start to all other vertices
cost = {}
cost['a'] = 6
cost['b'] = 2
cost['fin'] = infinity

# parents hash means the parents of all the vertices, the vertices which have not been reached noted as None
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

node = find_lowest_cost_node(costs)  # According to the costs hash, we find the cheapest node in the costs hash
processed = []
while node is not None:
    cost = costs[node]  # check current node's cost
    neighbors = graph[node]  # current node's neighbors

    for n in neighbors.keys():
        new_cost = cost + neighbors[n]  # temp sum in equal to the current cost + its neighbor's cost
        if cost[n] > new_cost:  # if the cost of current node is higher than temp_sum, we update the current cost
            cost[n] = new_cost
            parents[n] = node  # change this neighbor's parent to the node

    processed.append(node)
    node = find_lowest_cost_node(costs)

def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node

