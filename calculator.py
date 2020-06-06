import numpy as np

class Calculator:


    def __init__(self):
        return


    @staticmethod
    def rank_all_hands(hand_combos):
        return np.max(np.array(Parallel(n_jobs=multiprocessing.cpu_count(), backend="threading") \
                                   (delayed(parallel_rank_hand)(sce, hand_combos) for sce in
                                    range(len(hand_combos.shape[1])))),
                      axis=1)



