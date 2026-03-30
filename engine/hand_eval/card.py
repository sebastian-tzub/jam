# Integer encoding for cards: rank * 4 + suit

card_ranks = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
card_suit = ["SPADE", "CLUB", "HEART", "DIAMOND"]

def rank_of(card):
    return card // 4

def suit_of(card):
    return card % 4 

def make_deck():
    return list(range(52))

    