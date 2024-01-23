import heapq
import queue
from collections import defaultdict

from search_node import search_node


def create_open_set():
    #open_set = queue.PriorityQueue()
    open_set = []
    return open_set


def create_closed_set():
    closed_set = set()  # might need to change this data structure to something else
    return closed_set


def add_to_open(vn, open_set):
    if vn.prev is None:
        heapq.heappush(open_set, (vn.f, vn))
        # open_set.put(vn)
        return

    prev_node = vn.prev
    sum = 0
    while prev_node is not None:
        sum += prev_node.g
        prev_node = prev_node.prev

    vn.g = sum
    heapq.heappush(open_set, (vn.f, vn))
    # open_set.put(vn)


def open_not_empty(open_set):
    # if open_set.empty():
    if len(open_set) == 0:
        return False
    return True


def get_best(open_set):
    # we use [1] here to extract the node itself, the set stores everything in tupples where [0] is the heap sorting value

    # return open_set.get()
    return heapq.heappop(open_set)[1]


def add_to_closed(vn, closed_set):
    closed_set.add(vn)


# returns False if curr_neighbor state not in open_set or has a lower g from the node in open_set
# remove the node with the higher g from open_set (if exists)
def duplicate_in_open(vn, open_set):
    #queue_list = sorted(open_set)
    for node in open_set:
        if node[1] == vn: # the state is a string so no need for a custom __eq__ function
            if node[1].g >= vn.g:
                open_set.remove(node)
                heapq.heapify(open_set)

                return False
            else:
                return True
    return False


# returns False if curr_neighbor state not in closed_set or has a lower g from the node in closed_set
# remove the node with the higher g from closed_set (if exists)
def duplicate_in_closed(vn, closed_set):
    for node in closed_set:
        if node.state == vn.state:
            if node.g >= vn.g:
                closed_set.discard(node)
                return False
            else:
                return True
    return False


def print_path(path):
    for i in range(len(path) - 1):
        print(f"[{path[i].state.get_state_str()}]", end=", ")
    print(path[-1].state.state_str)


def search(start_state, heuristic, goal_state):
    open_set = create_open_set()
    closed_set = create_closed_set()
    start_node = search_node(start_state, 0, heuristic(start_state))
    add_to_open(start_node, open_set)

    while open_not_empty(open_set):

        current = get_best(open_set)

        if current.state.get_state_str() == goal_state:
            path = []
            while current:
                path.append(current)
                current = current.prev
            path.reverse()
            return path

        add_to_closed(current, closed_set)

        for neighbor, edge_cost in current.get_neighbors():
            curr_neighbor = search_node(neighbor, current.g + edge_cost, heuristic(neighbor), current)
            if not duplicate_in_open(curr_neighbor, open_set) and not duplicate_in_closed(curr_neighbor, closed_set):
                add_to_open(curr_neighbor, open_set)

    return None
