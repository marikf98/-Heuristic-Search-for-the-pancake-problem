

class pancake_state:

    def __init__(self, state_str):
        self.state_str = state_str
        #you may add data stractures to improve the search


    #returns an array of tuples of neighbor states and the cost to reach them: [(pancake_state1, cost1), (pancake _state2, cost2)...]
    def get_neighbors(self):
        pancake_stack = self.state_str.split(',')
        pancake_stack = [int(num) for num in pancake_stack]
        neighbors = []
        for i in range(0, len(pancake_stack)):
            reverse_part = pancake_stack[i:][::-1]
            pancake_stack_str = [str(x) for x in pancake_stack]  # Corrected this line
            # print("string : ", pancake_stack_str)
            pancake_str = (",".join(map(str, pancake_stack[:i] + reverse_part)))
            pancake_cost = sum(reverse_part)
            neighbors.append((pancake_state(pancake_str), pancake_cost))
            # neighbors.append((pancake_state((",".join(map(str, pancake_stack[:i] + reverse_part))), sum(reverse_part))))
        return neighbors

    #you can change the body of the function if you want
    def __hash__(self):
        return hash(self.state_str)

    #you can change the body of the function if you want
    def __eq__(self, other):
        return self.state_str == other.state_str

    def get_state_str(self):
        return self.state_str
