import sys

from poker.game import PokerHand


if __name__ == "__main__":
    if len(sys.argv) == 2:
        cards_tokens_string = sys.argv[1]

        cards_tokens = list(map(lambda x: x.strip(), cards_tokens_string.split(",")))
        poker_hands = list(map(lambda x: PokerHand(x), cards_tokens))

        if len(poker_hands) < 2:
            print("Not enough card sets provided, please provide at least two!")
        else:
            print("unsorted hands", poker_hands)
            print("  sorted hands", list(sorted(poker_hands)))
    else:
        THREE_OF_A_KIND = "5S 7C KC KH KD"
        FULL_HOUSE = "7C 7S KC KH KD"
        ROYAL_FLUSH = "TH JH QH KH AH"


        hand_with_royal_flush = PokerHand(ROYAL_FLUSH)
        hand_with_three_of_a_kind = PokerHand(THREE_OF_A_KIND)
        hand_with_full_house = PokerHand(FULL_HOUSE)

        print(
            "hand_with_three_of_a_kind < hand_with_full_house < hand_with_royal_flush",
            hand_with_three_of_a_kind < hand_with_full_house < hand_with_royal_flush
        )

        unsorted_hands = [hand_with_royal_flush,
                            hand_with_three_of_a_kind,
                            hand_with_full_house]

        print("unsorted hands", unsorted_hands)
        print("  sorted hands", sorted(unsorted_hands))
