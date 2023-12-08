import sys
from collections import Counter
from functools import cmp_to_key
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    lines = [ line.strip().split() for line in f.readlines() if line.strip() ]

arr = []
for hand, _ in lines:
    num_each_card = Counter(hand)
    if len(num_each_card) == 1:
        # 5 of a kind
        arr.append((hand, 5))
    elif len(num_each_card) == 2 and any(v == 1 for k, v in num_each_card.items()):
        # 4 of a kind
        arr.append((hand, 4))
    elif len(num_each_card) == 2 and any(v == 2 for k, v in num_each_card.items()):
        # full house
        arr.append((hand, 3.5))
    elif len(num_each_card) == 3 and any(v == 3 for k,v in num_each_card.items()): 
        # 3 of a kind
        arr.append((hand, 3))
    elif len(num_each_card) == 3 and set(num_each_card.values()) == {1,2}: 
        # 2 pair
        arr.append((hand, 2))
    elif len(num_each_card) == 4: 
        # 1 pair
        arr.append((hand, 1))
    elif len(num_each_card) == 5:
        # high card
        arr.append((hand, 0))

def compare(c1, c2):
    if (d := c1[1]-c2[1]) != 0: return d
    card_to_val = { c: i for i, c in enumerate("23456789TJQKA") }
    for i in range(len(c1[0])):
        if card_to_val[c1[0][i]] > card_to_val[c2[0][i]]:
            return 1
        if card_to_val[c1[0][i]] < card_to_val[c2[0][i]]:
            return -1
    return 0

sorted_by_strength = sorted(arr, key=cmp_to_key(compare))
hand_to_bid = { hand: int(bid) for hand, bid in lines }
print(sum( [hand_to_bid[hand]*(i+1) for i, (hand, _) in enumerate(sorted_by_strength) ]))
