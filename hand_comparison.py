def hand_score(hand):
    return max([assign_rank(h) for h in hand[comb_index(len(hand), 5)]])


# @jit(nopython=True)
def suit_check(hand_suits):
    return np.all(hand_suits[0] == hand_suits)


# @jit(nopython=True)
def straight_check(hand_values):
    return np.all(hand_values == np.arange(hand_values[0], hand_values[0] - 5, -1)) | \
           np.all(hand_values == np.array([14, 5, 4, 3, 2], dtype=np.int32))


# @jit(nopython=True)
def assign_rank(hand):
    hand_values = np.sort(hand[:, 0])[::-1]
    hand_suits = hand[:, 1]

    val = hand_values

    is_suited = suit_check(hand_suits)
    is_straight = straight_check(hand_values)

    if np.all(hand_values == np.array([14, 5, 4, 3, 2])):
        hand_values = np.array([5, 4, 3, 2, 1], dtype=np.int32)

    if is_suited and is_straight and hand_values[0] == 14:
        rank = 10 * np.power(16, 5)  # + hand_values * np.power(16, np.arange(4,-1, -1))
    elif is_suited and is_straight:
        rank = 9 * np.power(16, 5)  # + hand_values * np.power(16, np.arange(4,-1, -1))
    elif is_suited:
        rank = 6 * np.power(16, 5)  # + hand_values * np.power(16, np.arange(4,-1, -1))
    elif is_straight:
        rank = 5 * np.power(16, 5)  # + hand_values * np.power(16, np.arange(4,-1, -1))
    else:
        #         val_counter = np.array(Counter(np.array([2,2,3,4,5])).most_common())
        #         val, count = val_counter[:, 0], val_counter[:, 1]
        val = list(hand_values)
        val.sort(key=Counter(val).get, reverse=False)
        val = val[::-1]
        count = np.array(Counter(val).most_common())[:, 1]
        rank = rank_dict((max(count), min(count), len(count))) * np.power(16, 5)
        # val * np.power(16, np.arange(4, -1, -1))
    rank += np.sum(val * np.power(16, np.arange(4, -1, -1)))
    return rank


# @jit(nopython=True)
def rank_dict(max_min_len):
    return rank_params_dict[max_min_len]