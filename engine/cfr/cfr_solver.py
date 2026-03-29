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
        average_strategy = [0.0] * len(self.strategy_sum)
        sum = 0

        for frequency in self.strategy_sum:
            sum += frequency 

        if sum == 0: 
            return [1.0 / len(self.strategy_sum)] * len(self.strategy_sum)

        for i, frequency in enumerate(self.strategy_sum):
            average_strategy[i] = (frequency / sum)

        return average_strategy

# Recursive function traversing game tree 
def cfr(cards, history, reach_probs,
        is_terminal, get_payoff, get_valid_actions, num_players):

    #base case 
    if(is_terminal(history)): # if game over return payout 
        return get_payoff(history, cards)

    # get current player 
    # get remainder of action history div number of players to get curr player 
    current_player = len(history) % num_players #TODO UPDATE THIS LOGIC 
    # get valid actions availible at this node! 
    valid_actions = get_valid_actions(history)

    # Generate key based on current situation to get node from node dictionary
    key = (cards[current_player], tuple(history))
    if key not in nodes: 
        nodes[key] = Node(current_player, history, len(valid_actions)) 
    node = nodes[key]

    # Update nodes strategy sum based on the current strategy and the probability of reaching this specific node 
    strategy = node.get_strategy()
    reach_probability = reach_probs[current_player]
    for i, strat_freq in enumerate(strategy):
        node.strategy_sum[i] += reach_probability * strat_freq
    
    #RECURSING DOWN EACH ACTION BRANCH 
    #Build history by appending action 
    #Update reach probabilities 
    #Recurse and get value of action 

    action_payoffs = [0.0] * len(valid_actions)
    for i, action in enumerate(valid_actions):
        
        history_i = history + [action]
        new_reach_probs = reach_probs.copy()
        new_reach_probs[current_player] = reach_probs[current_player] * strategy[i]
        payoff = cfr(cards, history_i, new_reach_probs,
                    is_terminal, get_payoff, get_valid_actions, num_players)
        action_payoffs[i] = payoff 

    #Return exepected value of current strategy (weighted sum of action values)
    ev = sum(action_payoffs[i] * strategy[i] for i in range(len(valid_actions))) 

    #Compute and update regret 
    opponent = 1 - current_player # works only for kuhn poker 
    for i, action in enumerate(valid_actions): 
        regret = action_payoffs[i] - ev
        node.regret_sum[i] += regret * reach_probs[opponent] #weigh regret by chance of opponents actions leading to this node 

    return ev


def kuhn_solver(cards): 
    possible_situations = list(combinations(cards,2))
    for situation in possible_situations: 
        for i in range(100): 
            train(situation)

def train(situation): #TODO create situation class 
    cfr(situation)