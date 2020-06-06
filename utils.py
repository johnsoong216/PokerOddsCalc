import numpy as np
from itertools import combinations, chain
from scipy.special import comb


num_dict = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
suit_dict = {"d": 0, "c": 1, "s": 2, "h": 3}
rev_num_dict = {v: k for k, v in num_dict.items()}
rev_suit_dict = {v: k for k, v in suit_dict.items()}
hand_type_dict = {0: 'High Card', 1: 'One Pair', 2: 'Two Pairs', 3: 'Three of a Kind', 4: 'Straight', 5: 'Flush', 6: 'Full House', 7: 'Four of a Kind', 8: 'Straight Flush'}




def comb_index(n, k):
    count = comb(n, k, exact=True)
    index = np.fromiter(chain.from_iterable(combinations(range(n), k)),
                        int, count=count*k)
    return index.reshape(-1, k)

def card_str_to_arr(card_str):
    return np.array([[num_dict[card[0]], suit_dict[card[1]]] for card in card_str])


def card_arr_to_str(card_arr):
    return [rev_num_dict[card[0]] + rev_suit_dict[card[1]] for card in card_arr]


def add_card(card, card_arr):
    if type(card) == str:
        if len(card_arr) == 0:
            card_arr = card_str_to_arr([card])
        else:
            card_arr = np.concatenate([
                card_arr,
                card_str_to_arr([card])
            ], axis=0)

    else:
        if len(card_arr) == 0:
            card_arr = card_str_to_arr([card])
        else:
            card_arr = np.concatenate([
                card_arr,
                np.array([card])
            ], axis=0)
    return card_arr

def remove_card(card, card_arr):
    if type(card) == str:
        return card_arr[~np.all(np.isin(card_arr, card_str_to_arr([card])), axis=1)]
    else:
        return card_arr[~np.all(np.isin(card_arr, np.array([card])), axis=1)]

def format_cards(cards):
    if type(cards) == np.ndarray and cards.ndim == 1:
        return [cards]
    elif type(cards) == list and type(cards[0]) == int:
        return [cards]
    elif type(cards) == str:
        return [cards]
    return cards

