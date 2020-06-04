# from math import factorial
import numpy as np

num_dict = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
suit_dict = {"d": 0, "c": 1, "s": 2, "h": 3}
rev_num_dict = {v: k for k, v in num_dict.items()}
rev_suit_dict = {v: k for k, v in suit_dict.items()}

# def num_combinations(total, selected):
#     return int(factorial(total)/(factorial(selected)*factorial(total-selected)))
#
#

def card_str_to_arr(card_str):
    return np.array([[num_dict[card[0]], suit_dict[card[1]]] for card in card_str])


def card_arr_to_str(card_arr):
    return [rev_num_dict[card[0]] + rev_suit_dict[card[1]] for card in card_arr]


def add_to_hand():
    pass

def remove_from_hand():
    pass