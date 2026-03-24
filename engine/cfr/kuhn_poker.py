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
def get_valid_actions(history): 
    if (history == []):
        return [actions[1], actions [2]]
    elif (history == ["b"]):
        return [actions[0], actions [3]]
    elif (history == ["ch"]):
        return [actions[1], actions[2]]

# Checks if current round over given round history 
# Returns true if so 
def is_terminal(history):
    match history: 
        case ["ch","ch"]:
            return True
        case ["b","f"]:
            return True
        case ["b","c"]:
            return True
        case ["ch","b", "f"]:
            return True
        case ["ch","b", "c"]:
            return True

    return False 

# Return player 1's payout 
# Since zero sum game - negate payoff to get player 2 payout 
# Array of two cards passed in 
def determine_payout(history, cards):
     
    #determine pot size from bets from history 
    pot_size = history.count("b") + 2 # each player antes a chip at the start of a round 

    #determine winner from history and cards 
    if(history.count("f") == 0): #no folds, showdown, determine winner by highest card
        if(cards[0] > cards[1]):
            return pot_size
        else: 
            return -pot_size
    else: # fold occured, folding player loses 
        if(len(history) % 2 == 0): # player 2 acted last 
            return pot_size 
        else: 
            return -pot_size

