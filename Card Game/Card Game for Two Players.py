from card_game_functions import *


def Card_Game():
    # Create Cards for player 1

    a = generating_cards()
    b = generating_cards()
    c = generating_cards()

    # Create Cards for Player 2

    d = generating_cards()
    e = generating_cards()
    f = generating_cards()

    # Cards Should be Different

    c_t = [a[1], b[1], c[1], d[1], e[1], f[1]]
    c_n = [a[0], b[0], c[0], d[0], e[0], f[0]]

    diff_cards = differentiate_cards(a[-1][0], b[-1][0], c[-1][0], d[-1][0], e[-1][0], f[-1][0], c_t, c_n)

    # Print All the cards for player 1 and 2 appropriately

    print(f"Player 1")
    print(f"{diff_cards[0]}\n{diff_cards[1]}\n{diff_cards[2]}\n")
    print(f"Player 2")
    print(f"{diff_cards[3]}\n{diff_cards[4]}\n{diff_cards[5]}\n")

    # Cards Type

    card_t1 = c_t[0]
    card_t2 = c_t[1]
    card_t3 = c_t[2]

    card_t4 = c_t[3]
    card_t5 = c_t[4]
    card_t6 = c_t[5]

    # Cards Number

    card_n1 = c_n[0]
    card_n2 = c_n[1]
    card_n3 = c_n[2]

    card_n4 = c_n[3]
    card_n5 = c_n[4]
    card_n6 = c_n[5]

    """
    If a player have all the cards of same type & another have
    two or three types of cards, then the winner will be:
            PLAYER HAVING ALL CARDS WITH SAME TYPE
    """

    same_type1 = same_type_of_3cards(card_t1, card_t2, card_t3)
    same_type2 = same_type_of_3cards(card_t4, card_t5, card_t6)

    two_type1 = same_type_of_2_cards(card_t1, card_t2, card_t3, card_n1, card_n2, card_n3)
    two_type2 = same_type_of_2_cards(card_t4, card_t5, card_t6, card_n4, card_n5, card_n6)

    if same_type1 is True:
        if two_type2[0] is True:
            return "Player 1: won with All same Cards"
        if diff_type_of_all_cards(card_t4, card_t5, card_t6):
            return "Player 1: won with All same Cards"
    if same_type2 is True:
        if two_type1[0] is True:
            return "Player 2: won with All same Cards"
        if diff_type_of_all_cards(card_t1, card_t2, card_t3):
            return "Player 2: won with All same Cards"

    """
    If both players have three cards of same type (cards type can be different for both players)
    then if one player has cards in sequence, the player will win
    """

    two_cards_seq1 = check_3cards_in_sequence(card_n1, card_n2, card_n3)
    two_cards_seq2 = check_3cards_in_sequence(card_n4, card_n5, card_n6)

    if same_type1 is True and same_type2 is True:
        if two_cards_seq1 is True:
            return "Player1 won with having all cards in a sequence"
        if two_cards_seq2 is True:
            return "Player2 won with having all cards in a sequence"

    """
    If both Players have same type of Cards in a sequence then sum of card number 
    with the highest sum will win, otherwise draw 
    """

    if same_type1 is True and same_type2 is True and two_cards_seq1 is True and two_cards_seq2 is True:
        if highest_sum(card_n1, card_n2, card_n3) > highest_sum(card_n4, card_n5, card_n6) is True:
            return "Player 1: won having all cards of same type in sequence with highest sum"
        if highest_sum(card_n1, card_n2, card_n3) < highest_sum(card_n4, card_n5, card_n6) is True:
            return "Player 2: won having all cards of same type in sequence with highest sum"
        else:
            return "DRAW"

    """
    If any Player have cards with two type - (2 cards of same type and 1 of Different)
    PLAYER WILL WIN only if, other player have all three cards of different type
    """

    if two_type1[0] is True:
        if diff_type_of_all_cards(card_t4, card_t5, card_t6) is True:
            return "Player 1: won the match with 2 same cards and opponent lose with 3 diff cards"
    if two_type2[0] is True:
        if diff_type_of_all_cards(card_t1, card_t2, card_t3) is True:
            return "Player 2: won the match with 2 same cards and opponent lose with 3 diff cards"

    """
    If both players have two cards of same type, then if only one player has 
    two cards in sequence, the player will win
    """

    if two_type1[0] and two_type2[0] is True:
        if two_cards_seq1 is True:
            return "Player 1: won the match with 2 cards of same type and in sequence"
        if two_cards_seq2 is True:
            return "Player 2: won the match with 2 cards of same type and in sequence"

    """
    If both players have two cards of same type and in sequence, 
    then player with higher sequence or sum of two same 
    type cards is higher will win
    """

    if (two_type1[0] is True and two_type2[0] is True)\
            and (two_cards_seq1 is True and two_cards_seq2 is True):
        sum1 = two_type1[1][0] + two_type1[1][1]
        sum2 = two_type2[1][0] + two_type2[1][1]
        if sum1 > sum2:
            return f"Player 1: won by getting 2 cards of same type & sequence & its highest sum = {sum1}"
        else:
            return f"Player 2: won by getting 2 cards of same type & sequence & its highest sum = {sum2}"

    """
    If both players have two cards of same type and of same value, 
    then the player with third higher value card will win 
    otherwise game will be draw
    """

    if two_type1[0] is True and two_type2[0] is True\
            and (same_value(card_n1, card_n2, card_n3) is True
                 and same_value(card_n4, card_n5, card_n6 is True)):
        player_1 = different_value_card(card_n1, card_n2, card_n3)
        player_2 = different_value_card(card_n4, card_n5, card_n6)
        if player_1 > player_2:
            return "Player 1: won having 2 same type and value cards with 3rd highest value"
        elif player_1 < player_2:
            return "Player 2: won having 2 same type and value cards with 3rd highest value"
        else:
            return "DRAW Player 2: won having 2 same type and value cards with 3rd highest value"

    """
    In case three cards are of different type for both players then player 
    with higher sum will win, in case of same value, the player with higher 
    card will win, otherwise the player with second higher card will win, 
    otherwise game will be draw
    """

    diff1 = diff_type_of_all_cards(card_t1, card_t2, card_t3)
    diff2 = diff_type_of_all_cards(card_t4, card_t5, card_t6)

    if diff1 is True and diff2 is True:
        p1 = highest_sum(card_n1, card_n2, card_n3)
        p2 = highest_sum(card_n4, card_n5, card_n6)
        if p1 > p2:
            return "Player 1: won having all different cards with highest sum"
        if p1 < p2:
            return "Player 2: won having all different cards with highest sum"
        if p1 == p2:
            player_1 = max(card_n1, card_n2, card_n3)
            player_2 = max(card_n4, card_n5, card_n6)
            if player_1 > player_2:
                return "Player 1: won having all different cards with 1 higher card"
            if player_1 < player_2:
                return "Player 2: won having all different cards with 1 higher card"
            if player_1 == player_2:
                p_s_1 = second_higher_card(card_n1, card_n2, card_n3)
                p_s_2 = second_higher_card(card_n4, card_n5, card_n6)
                if p_s_1 > p_s_2:
                    return "Player 1: won having all different cards with second higher card"
                if p_s_1 < p_s_2:
                    return "Player 2: won having all different cards with second higher card"
                else:
                    return "Draw"
    return "Game Draw"


def main():
    print(Card_Game())


main()
