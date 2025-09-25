def alpha_beta_search(state, depth, alpha, beta, maximizing_player):
    # If leaf node or depth limit reached, return value of the node
    if depth == 0 or isinstance(state, int):
        return state

    if maximizing_player:
        max_eval = float('-inf')
        for child in state:
            eval = alpha_beta_search(child, depth-1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cutoff
        return max_eval
    else:
        min_eval = float('inf')
        for child in state:
            eval = alpha_beta_search(child, depth-1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cutoff
        return min_eval

# Define the game tree as nested lists where leaf nodes are integers (values)
# For example, this tree corresponds to a fixed structure:
#             Max
#           /      \
#         Min      Min
#       / | \     /  |  \
#      3  5  6   9  1   2

game_tree = [
    [3, 5, 6],  # Min node children
    [9, 1, 2]   # Min node children
]

optimal_value = alpha_beta_search(game_tree, depth=2, alpha=float('-inf'), beta=float('inf'), maximizing_player=True)
print("Optimal value (with Alpha-Beta Pruning):", optimal_value)

