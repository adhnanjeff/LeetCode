#Problem 950
#Solved on 10.4.24

from collections import deque
def deckRevealedIncreasing(deck):
    deck_sorted = sorted(deck, reverse=True)
    ordered_deck = deque()

    for card in deck_sorted:

        if len(ordered_deck) > 1:
            ordered_deck.rotate(1)
        ordered_deck.appendleft(card)

    return list(ordered_deck) 

deck = [17,13,11,2,3,5,7]
ans = deckRevealedIncreasing(deck)
print(ans)

