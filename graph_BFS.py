'''
we use hashmap to implement graph and each key connect to other vertices
and note that the this graph is a single edge graph (undirected graph)
for some vertices, two edges connect each other (directed graph)
'''


graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


'''
Two important data structure, queue and stack. For queue, it is FIFO structure and for stack, it is LIFO. In the 
BFS algorithm, we use queue structure to implement this.
BFS step:
    1. Create an queue to store the elements in the first stage for the starting point 
    2. Each time pop one element 
    3. Check if it is destination
    4. if yes: finish, if no, add all its neighbors to the end of queue
    5. back to step 2
    6. If queue length = 0, no destination
'''

from collections import deque

def BFS(name):
    search_queue = deque()
    search_queue += graph[name]  # create the initial stage around the starting poing

    searched = []  # to store the searched elements to avoid repeative search (to reduce search time) and periodic loop (like only elements and connect each other)
    while search_queue:  # if search_queue is not empty
        person = search_queue.popleft()  # to pop out the first one
        if person not in searched:  # we check this person only when this person was not searched before
            if person_is_seller(person):  # if we reach the destination
                print(f"{person} is seller")
                return True   # to stop the function
            else:
                search_queue += graph['person']  # if person is not seller, we need to add this person's neighbors to the end of queue
                searched.append(person)

    return False   # if search_queue's length is 0, we return false


def person_is_seller(name):
    return name[-1] == 'm'   # just a success condition to check if we reach the destination


'''
BFS time complexity is O(E + V) E is number of edge and v is the number of vertices: to check if one person is seller, we need O(1) and multiply by V
BFS use queue to insure the order so that it can reach the shortest path
'''