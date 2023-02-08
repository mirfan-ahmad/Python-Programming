from random import randint
from random_card_generator import random_card_generated


def generating_cards():
    card_number = randint(1, 13)
    card_type = randint(0, 3)
    String = random_card_generated(card_number, card_type)
    return card_number, card_type, String


def differentiate_cards(a, b, c, d, e, f, c_t, c_n):
    list1 = [a, b, c, d, e, f]
    for i in range(len(list1)):
        for j in range(1, len(list1)):
            while True:
                if list1[i] == list1[j] and i != j:
                    x = generating_cards()
                    c_t[i] = x[1]
                    c_n[i] = x[0]
                    list1[i] = x[-1][0]
                break
    return list1[0], list1[1], list1[2], list1[3], list1[4], list1[5], c_t, c_n


def same_type_of_2_cards(a1, b1, c1, a, b, c):
    Type = [0, 0]
    if a1 == b1 and a1 != c1:
        Type = [a, b]
        list1 = [True, Type]
        return list1
    if a1 == c1 and a1 != b1:
        Type = [a, c]
        list1 = [True, Type]
        return list1
    if b1 == a1 and b1 != c1:
        Type = [b, a]
        list1 = [True, Type]
        return list1
    if b1 == c1 and b1 != a1:
        Type = [b, c]
        list1 = [True, Type]
        return list1
    if c1 == a1 and c1 != b1:
        Type = [c, a]
        list1 = [True, Type]
        return list1
    if c1 == b1 and c1 != a1:
        Type = [c, b]
        list1 = [True, Type]
        return list1
    return False, Type


def same_type_of_3cards(a, b, c):
    if a == b and a == c and b == c:
        return True
    return False


def diff_type_of_all_cards(a, b, c):
    if a != b and a != c and b != c:
        return True
    return False


def check_3cards_in_sequence(a, b, c):
    """
    Check the 3 cards of both players either they have cards
    in sequence or not?
    How to Check whether the cards are in sequence or not?
    By using, Absolut(abs()) function
    """
    list1 = [a, b, c]
    sort = sorted(list1)
    if abs(sort[0] - sort[1]) == 1 and abs(sort[1] - sort[2]) == 1:
        return True
    return False


def check_2cards_in_sequence(a, b, c):
    """
    Check the 2 cards of both players either they have cards
    in sequence or not?
    How to Check whether the cards are in sequence or not?
    By using, Absolut(abs()) function
    """
    list1 = [a, b, c]
    sort = sorted(list1)
    if abs(sort[0] - sort[1]) == 1 or abs(sort[1] - sort[2]) == 1:
        return True
    return False


def highest_sum(a, b, c):
    return a + b + c


def same_value(a, b, c):
    if (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
        return True
    return False


def different_value_card(a, b, c):
    if a == b and a != c:
        value = [a, b]
    elif a == c and a != b:
        value = [a, c]
    elif b == c and b != a:
        value = [b, c]
    elif b == a and b != c:
        value = [b, a]
    elif c == a and c != b:
        value = [c, a]
    elif c == b and c != a:
        value = [c, b]
    if a not in value and b not in value:
        return c
    elif a not in value and c not in value:
        return b
    elif b not in value and c not in value:
        return a
    elif b not in value and a not in value:
        return c
    elif c not in value and a not in value:
        return b
    elif c not in value and b not in value:
        return a


def second_higher_card(a, b, c):
    list1 = [a, b, c]
    sort = sorted(list1)
    return sort[1]
