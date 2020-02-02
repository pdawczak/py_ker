import pytest

from ..poker.ranking import Highcard, Pair, TwoPairs, ThreeOfAKind, Straight, Flush, FullHouse, FourOfAKind, StraightFlush, RoyalFlush

from ..poker.cards import Card

# Reminder to self:
#
#   S - spade
#   H - heart
#   C - clubs
#   D - diamonds

def test_it_ranks_list_of_cards():
    non_ranked_cards = [Card("2S"), Card("4H"), Card("7D"), Card("KC"), Card("AC")]
    assert Highcard.valid_for_cards(non_ranked_cards)

    cards_with_a_pair = [Card("2S"), Card("4H"), Card("4D"), Card("KC"), Card("AC")]
    assert Pair.valid_for_cards(cards_with_a_pair)
    assert not Pair.valid_for_cards(non_ranked_cards)

    cards_with_two_pairs = [Card("2S"), Card("4H"), Card("4D"), Card("KC"), Card("KH")]
    assert TwoPairs.valid_for_cards(cards_with_two_pairs)
    assert not TwoPairs.valid_for_cards(cards_with_a_pair)

    cards_with_three_of_a_kind = [Card("5S"), Card("7C"), Card("KC"), Card("KH"), Card("KD")]
    assert ThreeOfAKind.valid_for_cards(cards_with_three_of_a_kind)
    assert not ThreeOfAKind.valid_for_cards(cards_with_a_pair)

    cards_with_straight = [Card("3C"), Card("4H"), Card("5D"), Card("6C"), Card("7S")]
    assert Straight.valid_for_cards(cards_with_straight)
    assert not Straight.valid_for_cards(cards_with_a_pair)

    cards_with_flush = [Card("2C"), Card("8C"), Card("9C"), Card("QC"), Card("KC")]
    assert Flush.valid_for_cards(cards_with_flush)
    assert not Flush.valid_for_cards(cards_with_a_pair)

    cards_with_full_house = [Card("7C"), Card("7S"), Card("KC"), Card("KH"), Card("KD")]
    assert FullHouse.valid_for_cards(cards_with_full_house)
    assert not FullHouse.valid_for_cards(cards_with_a_pair)

    cards_with_four_of_a_kind = [Card("5S"), Card("KC"), Card("KH"), Card("KD"), Card("KS")]
    assert FourOfAKind.valid_for_cards(cards_with_four_of_a_kind)
    assert not FourOfAKind.valid_for_cards(cards_with_a_pair)

    cards_with_straight_flush = [Card("3C"), Card("4C"), Card("5C"), Card("6C"), Card("7C")]
    assert StraightFlush.valid_for_cards(cards_with_straight_flush)
    assert not StraightFlush.valid_for_cards(cards_with_a_pair)

    cards_with_royal_flush = [Card("TH"), Card("JH"), Card("QH"), Card("KH"), Card("AH")]
    assert RoyalFlush.valid_for_cards(cards_with_royal_flush)
    assert not RoyalFlush.valid_for_cards(cards_with_straight_flush)


def test_ranks_preserve_order():
    assert Highcard() < Pair() < TwoPairs() < ThreeOfAKind() < Straight() < \
             Flush() < FullHouse() < FourOfAKind() < StraightFlush() < \
             RoyalFlush()
