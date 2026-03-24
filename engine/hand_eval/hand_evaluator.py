from card import rank_of, suit_of
from itertools import combinations
from collections import Counter

#0 — High card
#1 — One pair
#2 — Two pair
#3 — Three of a kind
#4 — Straight
#5 — Flush
#6 — Full house
#7 — Four of a kind
#8 — Straight flush

# takes in 5 cards and outputs highteset touple (best hand)
def best_of_seven_cards(cards):
    best_five = (max(combinations(cards, 5)), key = evaluate)
    return best_five


# takes in 5 cards and outputs tuple in form of (...)
def evaluate(cards):
    ranks = [rank_of(card) for card in cards]
    suits = [suit_of(card) for card in cards]
    rank_counts = Counter(ranks)

    is_flush = len(set(suits)) == 1
    is_straight = (len(set(ranks)) == 5 and max(ranks) - min(ranks) == 4)
    is_straight_flush = is_straight and is_flush
    is_four_pair = max(rank_counts.values()) == 4
    is_three_pair = max(rank_counts.values()) == 3
    is_one_pair = max(rank_counts.values()) == 2 and len(rank_counts) == 4
    is_two_pairs = max(rank_counts.values()) == 2 and len(rank_counts) == 3
    if_full_house = max(rank_counts.values()) == 3 and min(rank_counts.values()) == 2
   
   #TODO: Make this more clean 
    if is_straight_flush:
        return (8, max(ranks))
    elif is_four_pair:
        return (7, max([rank for rank, count in rank_counts.items() if count == 4]), 
        min([rank for rank, count in rank_counts.items() if count == 1]))
    elif if_full_house:
        return (6, max([rank for rank, count in rank_counts.items() if count == 3]), 
        max([rank for rank, count in rank_counts.items() if count == 2]))
    elif is_flush:
        return (5, max(ranks))
    elif is_straight:
        return (4, max(ranks))
    elif is_three_pair:
        kickers = sorted([rank for rank, count in rank_counts.items() if count == 1], reverse=True)
        return (3, max([rank for rank, count in rank_counts.items() if count == 3]), *kickers)
    elif is_two_pairs:
        kicker = [rank for rank, count in rank_counts.items() if count ==1][0]
        return(2,max([rank for rank, count in rank_counts.items() if count == 2]),
            min([rank for rank, count in rank_counts.items() if count == 2]), kicker)
    elif is_one_pair:
        kickers = sorted([rank for rank, count in rank_counts.items() if count == 1], reverse=True)
        return (1, max([rank for rank, count in rank_counts.items() if count == 2]), *kickers)
    else:
        return(0, *sorted(ranks, reverse=True))
