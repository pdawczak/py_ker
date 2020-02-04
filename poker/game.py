from functools import total_ordering

from .cards import Card
from .ranking import Ranking

@total_ordering
class PokerHand:
    def __init__(self, card_tokens):
        self.card_tokens = card_tokens

        cards = sorted([Card(card_token) for card_token in card_tokens.split(" ")])
        self.rank = Ranking.rank(cards)

    def __repr__(self):
        return "<PokerHand [{}] {}>".format(self.rank, self.card_tokens)

    def __eq__(self, other_hand):
        return self.rank.__eq__(other_hand.rank)

    def __neq__(self, other_hand):
        return self.rank.__neq__(other_hand.rank)

    def __lt__(self, other_hand):
        return self.rank.__lt__(other_hand.rank)
