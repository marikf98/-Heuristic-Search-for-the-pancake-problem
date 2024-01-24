from pancake import heuristics
from search import search, print_path
from pancake_state import pancake_state
from heuristics import *

if __name__ == '__main__':
    # goal_state = "4,3,2,1"
    # pancake_input = "4,2,3,1"
    goal_state = "6,5,4,3,2,1"
    pancake_input = "6,4,2,5,3,1"
    #pancake_input = "5,3,6,4,1,2"
    pancake_state = pancake_state(pancake_input)

    pancake_state.get_neighbors()
    search_result = search(pancake_state, base_heuristic, goal_state)
    # search_result = search(pancake_state, advanced_heuristic, goal_state)
    print_path(search_result)



