from random import randint
from random_card_generator import random_card_generated

"""
Symbol   Type    Color      Symbol      Representation
-------|-------|-------  |  ---------|----------------
  D     Diamond   Red    |   (A)1           Ace
  H      Heart    Red    |  2....10       Card Value (2, 3, 4, 5, 6, 7, 8, 9, 10)
  S      Spade    Black  |    (J)11          Jack
  C      Club     Black  |    (Q)12          Queen
                         |    (K)13          King 
"""


def card_generator():
    card_number = randint(1, 13)
    card_type = randint(0, 3)
    color = randint(0, 1)
    return random_card_generated(card_number, card_type)


def main():
    a = card_generator()
    b = card_generator()
    c = card_generator()
    if a == b or a == c:
        while True:
            a = card_generator()
            if a != b and a != c:
                break
    if b == c:
        while True:
            a = card_generator()
            if b != c:
                break
    print(a)
    print(b)
    print(c)


main()
