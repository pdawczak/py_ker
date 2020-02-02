import pytest

from ..poker.cards import InvalidCardTokenError, Card


def test_it_allows_initialising_a_card():
    assert Card("2H")

    with pytest.raises(InvalidCardTokenError) as excinfo:
        Card("ZXC")
    assert "should consist of 2 characters" in str(excinfo.value)

    # Continue with assertion around validation of invalid argument strings,
    # like unexpected value or suit...


def test_cards_are_sortable():
    cards = [Card("9H"),
             Card("6H"),
             Card("TH"),
             Card("AH"),
             Card("2H")]

    sorted_cards = sorted(cards)

    assert sorted_cards == [Card("2H"),
                            Card("6H"),
                            Card("9H"),
                            Card("TH"),
                            Card("AH")]
