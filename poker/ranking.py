from functools import total_ordering

from abc import ABC, abstractmethod

from collections import Counter


class Ranking:
    """It allows ranking of a set of the cards."""

    def rank(cards):
        """It perform the ranking.

        It is a factory that will accept list of Card objects and will perform
        ranking, which effect will be an instance one of specific Rank instances.

        Parameters
        ----------
        cards : list(Card)
            List of cards which will be ranked

        Returns
        -------
        Based on the set of the cards, it will return one of Rank strategies

        Example
        -------

            Given a set of cards, it will return one of Rank instances, like:

            >>> rank = Ranking.rank(example_cards_with_royal_flush)
            >>> type(rank)
            RoyalFlush

            >>> rank = Ranking.rank(example_cards_with_three_of_a_kind)
            >>> type(rank)
            ThreeOfAKind

        """
        all_rankings = [RoyalFlush,
                        StraightFlush,
                        FourOfAKind,
                        FullHouse,
                        Flush,
                        Straight,
                        ThreeOfAKind,
                        TwoPairs,
                        Pair,
                        Highcard]

        # Search from the highest Rank (that is the most restrictive) to the
        # lowest one. We know Highcard is kind of match-all-cases, so we can
        # rely on this fact, so method will always return "some" instance of
        # a Rank.
        # Alternatively, we could consider raising exception in case no Rank
        # has been matched.
        for rank_class in all_rankings:
            if rank_class.valid_for_cards(cards):
                return rank_class()


@total_ordering
class Rank(ABC):
    """Represents an instance of a Rank. It will allow comparing Ranks.

    There are a few strategies of ranking cards, each of which has it's own
    implementation of Rank base class.

    Once the instances of Ranks are initialised it is possible to compare them.

    Examples
    --------

        >>> Straight() < FullHouse()
        True

        >>> TwoPairs() > Pair()
        True

        >>> sorted([FullHouse(), TwoPairs(), ThreeOfAKind()])
        [<Rank: TwoPairs>, <Rank: ThreeOfAKind>, <Rank: FullHouse>]

    """

    @abstractmethod
    def valid_for_cards(cards):
        """It checks if provided set of cards fulfill criteria of a particular rank.

        Parameters
        ----------
        cards : list(Card)
            List of cards which will be ranked

        Returns
        -------
        Boolean value that will indicate if the cards match criteria of a rank.
        """
        pass

    @abstractmethod
    def rank_value(self):
        """Returns an integer.

        It's sole purpose is only for comparing purposes and the value doesn't
        have any meaning outside this context.

        Returns
        -------
        An integer that will be used for comparison between Rank instances
        """
        pass

    def __eq__(self, other_rank):
        return self.rank_value() == other_rank.rank_value()

    def __neq__(self, other_rank):
        return not (self.rank_value() == other_rank.rank_value())

    def __lt__(self, other_rank):
        return self.rank_value() < other_rank.rank_value()

    def __repr__(self):
        return "<Rank: {}>".format(self.__class__.__name__)


class Highcard(Rank):
    def valid_for_cards(cards):
        return True

    def rank_value(self):
        return 1


class Pair(Rank):
    def valid_for_cards(cards):
        return count_occurrences_of_a_value(cards, look_for_counts_of=2) == 1

    def rank_value(self):
        return 2


class TwoPairs(Rank):
    def valid_for_cards(cards):
        return count_occurrences_of_a_value(cards, look_for_counts_of=2) == 2

    def rank_value(self):
        return 3


class ThreeOfAKind(Rank):
    def valid_for_cards(cards):
        return count_occurrences_of_a_value(cards, look_for_counts_of=3) == 1

    def rank_value(self):
        return 4


class Straight(Rank):
    def valid_for_cards(cards):
        return all_cards_in_increasing_value(cards)

    def rank_value(self):
        return 5


class Flush(Rank):
    def valid_for_cards(cards):
        return all_cards_of_a_single_suit(cards)

    def rank_value(self):
        return 6


class FullHouse(Rank):
    def valid_for_cards(cards):
        found_pairs = count_occurrences_of_a_value(cards, look_for_counts_of=2)
        found_tripples = count_occurrences_of_a_value(cards, look_for_counts_of=3)

        return (found_pairs == 1) and (found_tripples == 1)

    def rank_value(self):
        return 7


class FourOfAKind(Rank):
    def valid_for_cards(cards):
        return count_occurrences_of_a_value(cards, look_for_counts_of=4) == 1

    def rank_value(self):
        return 8


class StraightFlush(Rank):
    def valid_for_cards(cards):
        # 1. Check if it is Straight
        if not all_cards_in_increasing_value(cards):
            return False

        # 2. Check if it is Flush
        return all_cards_of_a_single_suit(cards)

    def rank_value(self):
        return 9


class RoyalFlush(Rank):
    def valid_for_cards(cards):
        # 1. Check if it is Straight
        if not all_cards_in_increasing_value(cards):
            return False

        # 2. Check if it is Flush
        if not all_cards_of_a_single_suit(cards):
            return False

        # 3. Check if the first card is a 10 (as only then Ace will be last one)
        return cards[0].value == 10

    def rank_value(self):
        return 10


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


def all_cards_of_a_single_suit(cards):
    suits_found = set([card.suit for card in cards])
    return len(suits_found) == 1
