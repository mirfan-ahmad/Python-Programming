from random import randint
from random_card_generator import random_card_generated


def generating_cards():
    card_number = randint(1, 13)
    card_type = randint(0, 3)
    color = randint(0, 1)
    String = random_card_generated(card_number, card_type)
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

    if abs(a[0] - b[0]) == 1 or abs(a[0] - c[0]) == 2 or abs(b[0] - c[0]) == 1:
        print("All Cards are in sequence")

    # Check: All cards in a sequence and of same type?

    if a[1] == b[1] == c[1]:
        if abs(a[0] - b[0]) == 1 and abs(b[0] - c[0]) == 1:
            print("All Cards are in sequence and of same type")
        elif abs(a[0] - c[0]) == 1 and abs(c[0] - b[0]) == 1:
            print("All Cards are in sequence and of same type")
        elif abs(b[0] - c[0]) == 1 and abs(c[0] - a[0]) == 1:
            print("All Cards are in sequence and of same type")
    else:

        # Print Card with the highest value (Number)

        if a[0] > b[0] and a[0] > c[0]:
            print(f"Highest value of card = {a[3][-1]}")
        elif b[0] > c[0]:
            print(f"Highest value of card = {b[3][-1]}")
        else:
            print(f"Highest value of card = {c[3][-1]}")


main()
