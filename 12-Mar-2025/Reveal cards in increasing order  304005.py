# Problem: Reveal cards in increasing order  - https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        indexes = deque(i for i in range(len(deck)))
        result = [0 for i in range(len(deck))]

        for i in range(len(deck)):
            index = indexes.popleft()
            if indexes:
                indexes.append(indexes.popleft()) 
            result[index] = deck[i]
        return result           

