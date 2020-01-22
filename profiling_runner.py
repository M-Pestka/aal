#! /usr/bin/env python3
from tqdm import tqdm

import pandas as pd
import numpy as np
from generator_grafu import generate_graph
from generator_grafu import turbo_random
import podejscie_1
from podejscie_1 import Solver

def get_ex(parents):
    return parents, int((2*parents-1)**2*np.random.random())

test_cases = []
for p in [10, 40, 80, 120, 160, 200, 250, 300, 310, 320, 330]:
    for i in range(20):
        test_cases.append(get_ex(p))


if(__name__ == '__main__'):
    outcomes = []
    for i, (num_p, num_random) in enumerate(tqdm(test_cases)):    
        edges = turbo_random(num_p, num_random)
        s = Solver()
        s.edges = edges
        time = s.solve(timeit = True)

        outcomes.append((num_p, num_random, len(edges), time))
        if(i%30 == 0):
            pd.DataFrame(outcomes, columns = ['parents', 'random', 'edges', 'time']).to_csv('_logi_big.csv', index = False)

    pd.DataFrame(outcomes, columns = ['parents', 'random', 'edges', 'time']).to_csv('_logi_biger.csv', index = False)  
