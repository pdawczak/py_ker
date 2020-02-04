from functools import total_ordering

from .cards import Card
from .ranking import Ranking

@total_ordering
class PokerHand:
    """Represents a hand of cards.

    It accepts a string representing set of cards at a hand. Instances of
    PokerHands can be compared between each other.

    Attributes
    ----------
    card_tokens : str
        It is an initial string passed in when instantiating a PokerHand

    rank : Rank
        Represents a rank of the cards at hand
    """

    def __init__(self, card_tokens):
        """
        Parameters
        ----------
        card_tokens : str
            It is a string representing set of cards, eg: "2S 5H AS KH JC"
        """
        self.card_tokens = card_tokens

        cards = sorted([Card(card_token) for card_token in card_tokens.split(" ")])
        self.rank = Ranking.rank(cards)

    def __repr__(self):
        return "<PokerHand [{}] {}>".format(self.rank, self.card_tokens)

    def __eq__(self, other_hand):
        # Delegate comparison to rank
        return self.rank.__eq__(other_hand.rank)

    def __neq__(self, other_hand):
        # Delegate comparison to rank
        return self.rank.__neq__(other_hand.rank)

    def __lt__(self, other_hand):
        # Delegate comparison to rank
        return self.rank.__lt__(other_hand.rank)
