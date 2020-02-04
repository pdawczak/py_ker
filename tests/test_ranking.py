import pytest

from ..poker.ranking import Ranking
from ..poker.ranking import Highcard, Pair, TwoPairs, ThreeOfAKind, Straight, Flush, FullHouse, FourOfAKind, StraightFlush, RoyalFlush

from ..poker.cards import Card

# Reminder to self:
#
#   S - spade
#   H - heart
#   C - clubs
#   D - diamonds

NON_RANKED_CARDS = [Card("2S"), Card("4H"), Card("7D"), Card("KC"), Card("AC")]
CARDS_WITH_A_PAIR = [Card("2S"), Card("4H"), Card("4D"), Card("KC"), Card("AC")]
CARDS_WITH_TWO_PAIRS = [Card("2S"), Card("4H"), Card("4D"), Card("KC"), Card("KH")]
CARDS_WITH_THREE_OF_A_KIND = [Card("5S"), Card("7C"), Card("KC"), Card("KH"), Card("KD")]
CARDS_WITH_STRAIGHT = [Card("3C"), Card("4H"), Card("5D"), Card("6C"), Card("7S")]
CARDS_WITH_FLUSH = [Card("2C"), Card("8C"), Card("9C"), Card("QC"), Card("KC")]
CARDS_WITH_FULL_HOUSE = [Card("7C"), Card("7S"), Card("KC"), Card("KH"), Card("KD")]
CARDS_WITH_FOUR_OF_A_KIND = [Card("5S"), Card("KC"), Card("KH"), Card("KD"), Card("KS")]
CARDS_WITH_STRAIGHT_FLUSH = [Card("3C"), Card("4C"), Card("5C"), Card("6C"), Card("7C")]
CARDS_WITH_ROYAL_FLUSH = [Card("TH"), Card("JH"), Card("QH"), Card("KH"), Card("AH")]


def test_it_ranks_list_of_cards():
    assert Highcard.valid_for_cards(NON_RANKED_CARDS)

    assert Pair.valid_for_cards(CARDS_WITH_A_PAIR)
    assert not Pair.valid_for_cards(NON_RANKED_CARDS)

    assert TwoPairs.valid_for_cards(CARDS_WITH_TWO_PAIRS)
    assert not TwoPairs.valid_for_cards(CARDS_WITH_A_PAIR)

    assert ThreeOfAKind.valid_for_cards(CARDS_WITH_THREE_OF_A_KIND)
    assert not ThreeOfAKind.valid_for_cards(CARDS_WITH_A_PAIR)

    assert Straight.valid_for_cards(CARDS_WITH_STRAIGHT)
    assert not Straight.valid_for_cards(CARDS_WITH_A_PAIR)

    assert Flush.valid_for_cards(CARDS_WITH_FLUSH)
    assert not Flush.valid_for_cards(CARDS_WITH_A_PAIR)

    assert FullHouse.valid_for_cards(CARDS_WITH_FULL_HOUSE)
    assert not FullHouse.valid_for_cards(CARDS_WITH_A_PAIR)

    assert FourOfAKind.valid_for_cards(CARDS_WITH_FOUR_OF_A_KIND)
    assert not FourOfAKind.valid_for_cards(CARDS_WITH_A_PAIR)

    assert StraightFlush.valid_for_cards(CARDS_WITH_STRAIGHT_FLUSH)
    assert not StraightFlush.valid_for_cards(CARDS_WITH_A_PAIR)

    assert RoyalFlush.valid_for_cards(CARDS_WITH_ROYAL_FLUSH)
    assert not RoyalFlush.valid_for_cards(CARDS_WITH_STRAIGHT_FLUSH)


def test_ranks_preserve_order():
    assert Highcard() < Pair() < TwoPairs() < ThreeOfAKind() < Straight() < \
             Flush() < FullHouse() < FourOfAKind() < StraightFlush() < \
             RoyalFlush()


def test_ranking_returns_proper_strategy_for_list_of_cards():
    assert type(Ranking.rank(NON_RANKED_CARDS)) == Highcard
    assert type(Ranking.rank(CARDS_WITH_A_PAIR)) == Pair
    assert type(Ranking.rank(CARDS_WITH_TWO_PAIRS)) == TwoPairs
    assert type(Ranking.rank(CARDS_WITH_THREE_OF_A_KIND)) == ThreeOfAKind
    assert type(Ranking.rank(CARDS_WITH_STRAIGHT)) == Straight
    assert type(Ranking.rank(CARDS_WITH_FULL_HOUSE)) == FullHouse
    assert type(Ranking.rank(CARDS_WITH_FLUSH)) == Flush
    assert type(Ranking.rank(CARDS_WITH_FOUR_OF_A_KIND)) == FourOfAKind
    assert type(Ranking.rank(CARDS_WITH_STRAIGHT_FLUSH)) == StraightFlush
    assert type(Ranking.rank(CARDS_WITH_ROYAL_FLUSH)) == RoyalFlush
