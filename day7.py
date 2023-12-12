import math as maths

def get_input() -> list[str]:
    with open('day7_input.txt', 'r') as f:
        res = f.readlines()
        res = [i.strip(' \n\r') for i in res]
        return [i for i in res if i != '']
    

def parse_input(lines: list[str]) -> list[(list[str], int)]:
    res = []
    for line in lines:
        hand, bid = line.split(' ')
        res.append((list(hand), int(bid)))
    return res


def count_cards(cards: list[str]) -> { str: int }:
    res = {}
    for c in cards:
        res[c] = res.get(c, 0) + 1
    return res


def get_hand_strength(cards: list[str]) -> int:
    freq = count_cards(cards)

    if len(freq) == 1:
        # Five of a kind
        # (All the same)
        return 6

    if len(freq) == 2:
        if freq[max(freq, key=freq.get)] == 4:
            # Four of a kind
            # (4 the same, 1 different)
            return 5
        if freq[max(freq, key=freq.get)] == 3:
            # Full house
            # (3 the same, 2 sharing a label)
            return 4

    if len(freq) == 3:
        if freq[max(freq, key=freq.get)] == 3:
            # Three of a kind
            # (3 the same, 2 different)
            return 3
        
        if len([i for i in freq.keys() if freq[i] == 2]) == 2:
            # Two pair
            # (2 pairs of labels and one distinct label)
            return 2
        
    if len(freq) == 4:
        # One pair
        # One pair of cards, and 3 distinct cards
        return 1

    if len(freq) == 5:
        # High card
        # All distinct cards
        return 0
    
    raise ValueError("Unknown hand combination: " + str(cards))


def compare_hands(cards1: list[str], cards2: list[str]) -> int:
    strength1 = get_hand_strength(cards1)
    strength2 = get_hand_strength(cards2)
    
    #Cards 1 is stronger than cards 2
    if strength1 > strength2:
        return -1
    
    #Cards 2 is stronger than cards 1
    if strength1 < strength2:
        return 1
    
    #Order of cards from strongest to weakest
    order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

    for c1, c2 in zip(cards1, cards2):
        #Index of each card
        #Lower is stronger
        c1 = order.index(c1)
        c2 = order.index(c2)

        if c1 < c2:
            return -1
        if c1 > c2:
            return 1
    
    # raise ValueError("Hands have the same value:", cards1, cards2)
    return 0

def sort_hands(hands: list[list[str]]) -> list[list[str]]:
    res = []
    #just do a simple insertion sort here
    for hand in hands:
        i = 0
        while i < len(res):
            if compare_hands(res[i], hand) <= 0:
                break
            i += 1
        
        res.insert(i, hand)

    return res


if __name__ == "__main__":
    lines = get_input()

    data = parse_input(lines)

    sorted_hands = sort_hands([c for c, b in data])

    winnings = 0
    for i, hand in enumerate(sorted_hands):
        bid = None
        for h, b in data:
            if h == hand:
                bid = b
                break
        
        print(i + 1, hand, bid, (i + 1) * bid)

        winnings += (i + 1) * bid

    print()
    print("winnings:", winnings)