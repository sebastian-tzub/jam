# Simplified version of poker (K,Q,J) to test correctness of CFR implementation 
# by comparing result strategy against known equilibrium 

cards = [0,1,2] # J Q K 
players = [0,1] # Player 1 and 2 
actions = ["c", "ch", "b","f"] # Call, check, bet, fold 

# Round history (history) is list of actions from actions list (represented by strings)

# Returns the two vaid actions from actions list
#   given the current round situation represented by string 
# "" --> No actions taken in round yet 
# "b" --> Player has bet
# "ch" --> Player has checked 
def get_valid_actions(round_history): 
    if (round_history == ""):
        return [actions[1], actions [2]]
    elif (round_history == "b"):
        return [actions[0], actions [3]]
    elif (round_history == "ch"):
        return [actions[1], actions[2]]

# Checks if current round over given round history 
# Returns true if so 
def is_terminal(history):

# Return player 1's payout 
# Since zero sum game - negate payoff to get player 2 payout 
def determine_payout(history, cards):
