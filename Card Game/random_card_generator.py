from random import randint


"""
Symbol - Type - Color       Symbol      Representation
----------------------   |  --------------------------
  D -   Diamond - Red        (A)1           Ace
  H -    Heart  - Red       2....10       Card Value (2, 3, 4, 5, 6, 7, 8, 9, 10)
  S -    Spade  - Black      (J)11          Jack
  C -    Club   - Black      (Q)12          Queen
                             (K)13          King 
"""


def random_card_generated(card_number, card_type):

    if card_number == 1:
        english = "Ace"
    elif card_number == 2:
        english = "Two"
    elif card_number == 3:
        english = "Three"
    elif card_number == 4:
        english = "Four"
    elif card_number == 5:
        english = "Five"
    elif card_number == 6:
        english = "Six"
    elif card_number == 7:
        english = "Seven"
    elif card_number == 8:
        english = "Eight"
    elif card_number == 9:
        english = "Nine"
    elif card_number == 10:
        english = "Ten"
    elif card_number == 11:
        english = "Jack"
    elif card_number == 12:
        english = "Queen"
    elif card_number == 13:
        english = "King"

    if card_type == 0:
        Type = "Diamond"
        color = "Red"
    elif card_type == 1:
        Type = "Heart"
        color = "Red"
    elif card_type == 2:
        Type = "Spade"
        color = "Black"
    elif card_type == 3:
        Type = "Club"
        color = "Black"

    String = f"{english} of {Type}"

    return String, card_type, card_number
