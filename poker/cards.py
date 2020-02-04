from functools import total_ordering

CARDS_VALUE_MAPPING = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}


class InvalidCardTokenError(Exception):
    """Is raised in case parsed card token is invalid."""
    pass

#####
#
#
# @TODO:
# Add more definitions for exceptions, eg. InvalidValueError, InvalidSuit etc...
#
#
#####


@total_ordering
class Card:
    """Represents a Card that can be instantiated from card_token.

    card_token is a two-element string that consists of card's value and suit
    (in this order), eg: "2H".

    Attributes
    ----------
    card_token : str
        A card_token that is used when instantiating the Card object

    value : int
        An integer representation of the card's value. It will be used
        internally for comparison purposes (comparing cards between each other)

    suit : str
        A single character string that represents the card's suit
    """

    def __init__(self, card_token):
        """Initialises an instance of a Card.

        Parameters
        ----------
        card_token : str
            It is a two-charactes string that will be used to determine card's
            value and suit.

        Raises
        ------
        InvalidCardTokenError
            Is raised if the card's token is a string of a length different
            than 2.
        """

        self.card_token = card_token

        if len(card_token) != 2:
            raise InvalidCardTokenError("Invalid card_token, should consist of 2 characters, but is '{}'".format(card_token))

        #####
        # Continue with validation if the token consists of valid characters
        # for value and suit...
        #####

        string_value, suit = card_token

        self.value = CARDS_VALUE_MAPPING[string_value]
        self.suit = suit

    def __eq__(self, other_card):
        return self.value == other_card.value

    def __neq__(self, other_card):
        return not (self.value == other_card.value)

    def __lt__(self, other_card):
        return self.value < other_card.value

    def __repr__(self):
        return "<Card: {}>".format(self.card_token)
