from random import randint
from random_card_generator import random_card_generated


def main():
    card_number = randint(1, 13)
    card_type = randint(0, 3)
    print(random_card_generated(card_number, card_type)[0])


main()
