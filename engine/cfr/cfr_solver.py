
nodes = dict()

# Generic node class; 
# Each node represents decison in pokre round, 
# Node must know current game state through action_history 
class Node: 
    def __init__(self, player, action_history, num_actions): 
        self.player = player 
        self.action_history = action_history 
        self.regret_sum = [0.0] * num_actions
        self.strategy_sum = [0.0] * num_actions

    # Returns optimal freqeuncy of actions based on current regret 
    def get_strategy(self): 
        curr_strategy = [0.0] * len(self.regret_sum)
        total_regret = 0 

        for regret in self.regret_sum:
            if(regret < 0): 
                continue

            total_regret += regret

        if total_regret == 0: # spread probabilites for each action uniformly 
            return [1.0 / len(self.regret_sum)] * len(self.regret_sum)
    
        for i, regret in enumerate(self.regret_sum):
            if (regret < 0):
                continue 

            curr_strategy[i] = regret/total_regret

        return curr_strategy

    # Returns average freqeuncies across all iterations --> GTO strategy 
    def get_average_strategy(self): 
        average_strategy = [0.0] * len(strategy_sum)
        sum = 0

        for frequency in strategy_sum:
            sum += frequency 

        for frequency in strategy_sum:
            average_strategy.append(frequency / sum)

        return average_strategy

# Recursive function traversing game tree 
def cfr(cards, history, reach_probs,
        is_terminal, get_payoff, get_valid_actions, num_players):

        #base case 
        if(is_terminal(history)): # if game over return payout 
            return get_payoff(history, cards)

        # get current player 
        # get remainder of action history div number of players to get curr player 
        current_player = len(history) % num_players 
        # get valid actions availible at this node! 
        valid_actions = get_valid_actions(history)

        key = (cards[current_player], tuple(history))
        if key not in nodes: 
            nodes[key] = Node(current_player, history, len(valid_actions)) 
        node = nodes[key]

