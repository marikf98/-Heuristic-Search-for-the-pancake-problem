#Original version
def base_heuristic(_pancake_state):
    pancake_stack = _pancake_state.get_state_str().split(',')
    pancake_stack = [int(num) for num in pancake_stack]
    for i in range(0, len(pancake_stack)):
        if pancake_stack[i] != len(pancake_stack) - i:
            return sum(pancake_stack[i:])
    return 0

# def base_heuristic(_pancake_state):
#     pancake_stack = _pancake_state.get_state_str().split(',')
#     pancake_stack = [int(num) for num in pancake_stack]
#
#     n = len(pancake_stack)
#     for i, num in enumerate(pancake_stack):
#         if num != n - i:
#             return sum(pancake_stack[i:])
#     return 0


def advanced_heuristic(_pancake_state):
    # # like the heuristic that in the slides of the practical session
    #
    # heuristic = 0
    # pancake_stack = _pancake_state.get_state_str().split(',')
    # pancake_stack = [int(num) for num in pancake_stack]
    #
    # if pancake_stack[0] != len(pancake_stack):
    #     heuristic += 1
    #
    # for i in range(0, len(pancake_stack)):
    #     if i == len(pancake_stack) - 1:
    #         break
    #     if abs(pancake_stack[i] - pancake_stack[i + 1]) > 1:
    #         heuristic += 1
    #
    # return heuristic
    return base_heuristic(_pancake_state)
