from abc import ABC, abstractmethod

from collections import Counter


class Rank(ABC):
    @abstractmethod
    def valid_for_cards(cards):
        pass


class Highcard(Rank):
    def valid_for_cards(cards):
        return True


class Pair(Rank):
    def valid_for_cards(cards):
        values_counter = Counter([card.value for card in cards])
        found_pairs = list(filter(lambda x: x[1] == 2, values_counter.items()))
        return len(found_pairs) == 1


class TwoPairs(Rank):
    def valid_for_cards(cards):
        values_counter = Counter([card.value for card in cards])
        found_pairs = list(filter(lambda x: x[1] == 2, values_counter.items()))
        return len(found_pairs) == 2


class ThreeOfAKind(Rank):
    def valid_for_cards(cards):
        values_counter = Counter([card.value for card in cards])
        found_tripples = list(filter(lambda x: x[1] == 3, values_counter.items()))
        return len(found_tripples) == 1


class Straight(Rank):
    def valid_for_cards(cards):
        prev_value = cards[0].value

        # Compare previous value against previous value
        for curr_idx in range(1, len(cards)):
            curr_value = cards[curr_idx].value
            if (prev_value + 1) != curr_value:
                return False
            prev_value = curr_value

        return True


class Flush(Rank):
    def valid_for_cards(cards):
        suits_found = set([card.suit for card in cards])
        return len(suits_found) == 1


class FullHouse(Rank):
    def valid_for_cards(cards):
        values_counter = Counter([card.value for card in cards])
        found_pairs = list(filter(lambda x: x[1] == 2, values_counter.items()))

        values_counter = Counter([card.value for card in cards])
        found_tripples = list(filter(lambda x: x[1] == 3, values_counter.items()))
        return (len(found_pairs) == 1) and (len(found_tripples) == 1)


class FourOfAKind(Rank):
    def valid_for_cards(cards):
        values_counter = Counter([card.value for card in cards])
        found_fourths = list(filter(lambda x: x[1] == 4, values_counter.items()))
        return len(found_fourths) == 1


class StraightFlush(Rank):
    def valid_for_cards(cards):
        # 1. Check if it is a Flush
        prev_value = cards[0].value

        for curr_idx in range(1, len(cards)):
            curr_value = cards[curr_idx].value
            if (prev_value + 1) != curr_value:
                return False
            prev_value = curr_value

        # 2. Check if all of the same suit
        suits_found = set([card.suit for card in cards])
        return len(suits_found) == 1


class RoyalFlush(Rank):
    def valid_for_cards(cards):
        # 1. Check if it is a Flush
        prev_value = cards[0].value

        for curr_idx in range(1, len(cards)):
            curr_value = cards[curr_idx].value
            if (prev_value + 1) != curr_value:
                return False
            prev_value = curr_value

        # 2. Check if all of the same suit
        suits_found = set([card.suit for card in cards])
        if len(suits_found) != 1:
            return False


        # 3. Check if the first card is a 10 (as only then Ace will be last one)
        return cards[0].value == 10
