
# Generic node class; 
# Each node represents decison in pokre round, 
# Node must know current game state through action_history 
class Node: 
    def __init__(self, player, action_history, num_actions): 
        self.player = player 
        self.action_history = action_history 
        regret_sum = [0.0] * num_actions
        strategy_sum = [0.0] * num_actions

# Recursive function traversing game tree 
def cfr(cards, history, reach_probs,
        is_terminal, get_payoff, get_valid_actions, num_players):

        #base case 
        if(is_terminal(history)): # if game over return payout 
            return get_payoff(history, cards)
