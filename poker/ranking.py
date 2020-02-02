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
        return count_occurrences_of_a_value(cards, look_for_counts_of=2) == 1


class TwoPairs(Rank):
    def valid_for_cards(cards):
        return count_occurrences_of_a_value(cards, look_for_counts_of=2) == 2


class ThreeOfAKind(Rank):
    def valid_for_cards(cards):
        return count_occurrences_of_a_value(cards, look_for_counts_of=3) == 1


class Straight(Rank):
    def valid_for_cards(cards):
        return all_cards_in_increasing_value(cards)


class Flush(Rank):
    def valid_for_cards(cards):
        suits_found = set([card.suit for card in cards])
        return len(suits_found) == 1


class FullHouse(Rank):
    def valid_for_cards(cards):
        found_pairs = count_occurrences_of_a_value(cards, look_for_counts_of=2)
        found_tripples = count_occurrences_of_a_value(cards, look_for_counts_of=3)

        return (found_pairs == 1) and (found_tripples == 1)


class FourOfAKind(Rank):
    def valid_for_cards(cards):
        return count_occurrences_of_a_value(cards, look_for_counts_of=4) == 1


class StraightFlush(Rank):
    def valid_for_cards(cards):
        # 1. Check if it is Straight
        if not all_cards_in_increasing_value(cards):
            return False

        # 2. Check if it is Flush
        suits_found = set([card.suit for card in cards])
        return len(suits_found) == 1


class RoyalFlush(Rank):
    def valid_for_cards(cards):
        # 1. Check if it is Straight
        if not all_cards_in_increasing_value(cards):
            return False

        # 2. Check if it is Flush
        suits_found = set([card.suit for card in cards])
        if len(suits_found) != 1:
            return False


        # 3. Check if the first card is a 10 (as only then Ace will be last one)
        return cards[0].value == 10


def count_occurrences_of_a_value(cards, look_for_counts_of=2):
    # 1. Count occurrences of values, eg:
    #
    #    "2C 2H 3C 3H 5H"
    #
    # will be:
    #
    #    {
    #        2: 2, # There are two 2s
    #        3: 2, # There are two 3s
    #        5: 1, # There is one 5
    #    }
    #
    values_counter = Counter([card.value for card in cards])

    # 2. Find only the entries of expected look_for_counts_of, eg:
    #
    # For previous count occurrences and assumed look_for_counts_of=1:
    #
    #     [(5, 1)]
    #
    # but for look_for_counts_of=2:
    #
    #     [(2, 2), (3, 2)]
    #
    found_occurrences = list(filter(lambda x: x[1] == look_for_counts_of, values_counter.items()))

    # 3. Finally, count those occurrences
    return len(found_occurrences)


def all_cards_in_increasing_value(cards):
    # 1. This will be a first element we will compare against
    prev_value = cards[0].value

    # 2. We will iterate for all the cards (but very first one) and compare its
    #    value against previous one
    for curr_idx in range(1, len(cards)):
        curr_value = cards[curr_idx].value
        # 3. If previous value increased by 1 is different than current value
        #    that means the cards are not in an increasing order
        if (prev_value + 1) != curr_value:
            return False
        prev_value = curr_value

    # 4. If we arrived here, that means we didn't discover a point in a list
    #    of cards that break the increase
    return True