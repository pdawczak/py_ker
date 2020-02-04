import pytest

from ..poker.game import PokerHand

THREE_OF_A_KIND = "5S 7C KC KH KD"
FULL_HOUSE = "7C 7S KC KH KD"
ROYAL_FLUSH = "TH JH QH KH AH"


def test_it_allows_comparing_poker_hands():
    hand_with_royal_flush = PokerHand(ROYAL_FLUSH)
    hand_with_three_of_a_kind = PokerHand(THREE_OF_A_KIND)
    hand_with_full_house = PokerHand(FULL_HOUSE)

    assert hand_with_three_of_a_kind < hand_with_full_house < hand_with_royal_flush

    unsorted_hands = [hand_with_royal_flush,
                      hand_with_three_of_a_kind,
                      hand_with_full_house]

    sorted_hands = [hand_with_three_of_a_kind,
                    hand_with_full_house,
                    hand_with_royal_flush]

    assert list(sorted(unsorted_hands)) == sorted_hands
