from random import randint
from random_card_generator import random_card_generated


def generating_cards():
    card_number = randint(1, 13)
    card_type = randint(0, 3)
    color = randint(0, 1)
    String = random_card_generated(card_number, card_type)[0]
    return card_number, card_type, color, String


def main():
    a = generating_cards()
    b = generating_cards()
    c = generating_cards()

    # Check: Card numbers are same or not?

    if a[0] == b[0] == c[0]:
        print("All cards have same number")

    # Check: Card Type is same or not?

    if a[1] == b[1] == c[1]:
        print("All cards have same type")

    # Check: Card color is same or not?

    if a[2] == b[2] == c[2]:
        print("All cards have same color")

    # Check: Cards are in a sequence or not?

    if abs(a[0] - b[0]) == 1 and abs(b[0] - c[0]) == 1:
        print("All Cards are in sequence")
    elif abs(a[0] - c[0]) == 1 and abs(c[0] - b[0]) == 1:
        print("All Cards are in sequence")
    elif abs(b[0] - c[0]) == 1 and abs(c[0] - a[0]) == 1:
        print("All Cards are in sequence")

    # Check: All cards in a sequence and of same type?

    if a[1] == b[1] == c[1]:
        if abs(a[0] - b[0]) == 1 and abs(b[0] - c[0]) == 1:
            print("All Cards are in sequence and of same type")
        elif abs(a[0] - c[0]) == 1 and abs(c[0] - b[0]) == 1:
            print("All Cards are in sequence and of same type")
        elif abs(b[0] - c[0]) == 1 and abs(c[0] - a[0]) == 1:
            print("All Cards are in sequence and of same type")

    # Check: Two cards have Same Type

    if a[1] == b[1]:
        print(f"{a[3]} & {b[3]} Have SAME TYPE")
    elif a[1] == c[1]:
        print(f"{a[3]} & {c[3]} Have SAME TYPE")
    elif b[1] == c[1]:
        print(f"{b[3]} & {c[3]} Have SAME TYPE")

    # Check: Two cards are in a sequence

    if abs(a[0]-b[0]) == 1:
        print(f"{a[3]} & {b[3]} are in sequence")
    elif abs(a[0]-c[0]) == 1:
        print(f"{a[3]} & {c[3]} are in sequence")
    elif abs(a[0]-c[0]) == 1:
        print(f"{b[3]} & {c[3]} are in sequence")
    else:

        # Print Card with the highest value (Number)

        if a[0] > b[0] and a[0] > c[0]:
            print(f"Highest value of card = {a[0]}")
        elif b[0] > c[0]:
            print(f"Highest value of card = {b[0]}")
        else:
            print(f"Highest value of card = {c[0]}")


main()
