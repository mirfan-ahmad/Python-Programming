from random import randint
from random_card_generator import random_card_generated


def generating_cards():
    card_number = randint(1, 13)
    card_type = randint(0, 3)
    color = randint(0, 1)
    card = random_card_generated(card_number, card_type)[0]
    return card_number, card_type, color, card


def main():
    a = generating_cards()
    b = generating_cards()

    # Check: Card number is same or not?

    if a[0] == b[0]:
        print(f"{a[-1]} & {b[-1]} have same number")

    # Check: Card type is same or not?

    if a[1] == b[1]:
        print(f"{a[-1]} & {b[-1]} have same type")

    # Check: Card color is same or not?

    if a[2] == b[2]:
        print(f"{a[-1]} & {b[-1]} have same color")

    # Check: Card is in a sequence or not?

    if abs(a[0]-b[0]) == 1:
        print(f"{a[-1]} & {b[-1]} are in sequence")


main()
