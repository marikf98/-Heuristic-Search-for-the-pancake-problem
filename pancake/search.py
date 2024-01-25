import heapq
import queue
from collections import defaultdict

from search_node import search_node

open_set_dict = {}
close_set_dict = {}

def create_open_set():
    #open_set = queue.PriorityQueue()
    # open_set = []
    open_set_dict.clear()
    return []


def create_closed_set():
    # closed_set =  set() # might need to change this data structure to something else
    close_set_dict.clear()
    return set()


def add_to_open(vn, open_set):
    if vn.prev is None:
        heapq.heappush(open_set, vn)
        open_set_dict[vn.state] = vn
        return

    prev_node = vn.prev
    while prev_node is not None:
        prev_node = prev_node.prev
    heapq.heappush(open_set, vn)
    open_set_dict[vn.state] = vn


def open_not_empty(open_set):
    # if open_set.empty():
    if len(open_set) == 0:
        return False
    return True


def get_best(open_set):
    # we use [1] here to extract the node itself, the set stores everything in tupples where [0] is the heap sorting value

    # return open_set.get()
    # return heapq.heappop(open_set)[1]
    return heapq.heappop(open_set)



def add_to_closed(vn, closed_set):
    closed_set.add(vn)
    open_set_dict[vn.state] = vn


# returns False if curr_neighbor state not in open_set or has a lower g from the node in open_set
# remove the node with the higher g from open_set (if exists)
def duplicate_in_open(vn, open_set):
    if vn.state in open_set_dict:
        if open_set_dict[vn.state].g >= vn.g:
            open_set.remove(open_set_dict[vn.state])
            heapq.heapify(open_set)
            return False
        else:
            return True
    return False

# returns False if curr_neighbor state not in closed_set or has a lower g from the node in closed_set
# remove the node with the higher g from closed_set (if exists)
def duplicate_in_closed(vn, closed_set):
    if vn.state in close_set_dict:
        if close_set_dict[vn.state].g >= vn.g:
            closed_set.discard(close_set_dict[vn.state])
            return False
        else:
            return True
    return False
    # for node in closed_set:
    #     if node == vn:
    #         if node.g >= vn.g:
    #             closed_set.discard(node)
    #             # closed_set.add(vn)
    #             return False
    #         else:
    #             return True
    # return False


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
        # print("The node that was chosen is " + current.state.state_str + " with h value of " + current.h.__str__() + " and g value of " + current.g.__str__())
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
                # print("Added the neighbor of " + current.state.state_str + " The neighbor is " + curr_neighbor.state.state_str + " With this h: " + curr_neighbor.h.__str__() + " and this g: " + curr_neighbor.g.__str__())
                add_to_open(curr_neighbor, open_set)

    return None
