from hand_evaluator import best_of_seven_cards

# ASSUMES EXACT HAND OF PLAYERS IS KNOWN (specific hand not range)
# Returns list of equities for each player 
def hand_equity(hands, board):

     # take out hand and board cards from deck
    dealt = board + [card for hand in hands for card in hand]
    remaining = set(make_deck()) - set(dealt)

    #get current street and call corresponding function to evaluate current street 
    length = len(board)

    if length == 3: 
        return hand_equity_flop(hand, board, remaining)
    elif length == 4: 
        return hand_equity_turn(hand, board, remaining)
    elif length == 5: 
        return hand_equity_river(hand, board, remaining)
    else: 
        return hand_equity_preflop()


def hand_equity_river(hand, board, remaining): 

    hand_tuples = [] #list of tuples for each hand returned by hand_evaluator methods 

    #if river (run each hand the hand eval)
    for hand in hands:
        curr_hand_tuple = best_of_seven_cards(hand + board)
        hand_tuples.append(curr_hand_tuple)

    #return equity for each hand 
    curr_max = ()
    max_indices = [0]
    for i, hand_tuple in enumerate(hand_tuples):
        if hand_tuple > curr_max:
            curr_max = hand_tuple 
            max_indices = [i] #reset list to this new max player
        elif hand_tuple == curr_max: 
            max_indices.append(i) # tie, append new index of tied max 
    
    #build equity for each player 
    equity_per_player = 1 / len(max_indices)    
    equities = [equity_per_player if i in max_indices else 0 for i in range(len(hands))]

    return equities 

# For street that isnt river.. 
# Generate each possible runout from remaining deck 
# Combine each runout with current board 
# Evaluate each players hand with complete board 
# Track wins across each runout 
# Dive by wins by total runouts to get equity 
def hand_equity_turn(hand, board, remaining): 

    # for each possible run out calculate 

    # divide wins for each player by total runouts to get equity 

    return equities 
def hand_equity_flop(hand, board, remaining): 

    return equities 

# TOO MANY COMBINATIONS ! 
def hand_equity_preflop(): 
