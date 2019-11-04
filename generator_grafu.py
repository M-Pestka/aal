#! /bin/python3

import random

def get_v_name(number):
    name = ''
    while(number > 25):
        name += chr((number%25)+97)
        number = number // 25
    
    name += chr(97+number)
    return name

def get_weight():
    return 10 + int(random.random()*20)

def generate_graph(num_parents, num_random):
    
    edges = []
    for v in range(1, num_parents + 1):
        w = get_weight()
        edges.append((v-1, v*2-1, w))
        w = get_weight()
        edges.append((v-1, v*2, w))

    min_weight = min([x[2] for x in edges])
    if(min_weight != 10):
        edges[-1] = (*edges[-1][:2], 10)

    d = {k: [] for k in range(num_parents*2+1)}

    for e in edges:
        d[e[0]].append(e[1])
        d[e[1]].append(e[0])

    for i in range(num_random):
        idx1 = -1
        indeces = []

        for k, v in d.items():
            if(len(v) < num_parents*2+1):
                indeces.append(k)

        idx1 = random.choice(indeces) 
        
        if(len(list(set(range(num_parents*2+1)) - set([idx1]) -set(d[idx1]))) == 0):
            break

        idx2 = random.choice(list(set(range(num_parents*2+1)) - set([idx1]) -set(d[idx1])))
        

        d[idx1].append(idx2)
        d[idx2].append(idx1)

        edges.append((idx1, idx2, int(random.random() * 8 + 1)))

    edges = random.permutation(edges)
    return edges

import numpy as np
def turbo_random(num_parents, aprox_num_random):
    tab = np.random.random((2*num_parents+1, 2*num_parents+1))
    for i in range(num_parents*2):
        tab[i, i+1] = 1

    tab *= 10
    tab = np.where(tab > 10*(1 - (aprox_num_random / (4.*num_parents**2))), tab, 0)
    indeces = np.nonzero(tab)
    edges = np.concatenate([np.transpose(indeces), tab[indeces][:, None]], axis = 1)
    return np.random.permutation(edges)


if(__name__ == '__main__'):
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--num_parents', default = 5, type = int, help = 'number of parents in tree, the resulting graph will have num_parents*2+1 verteces')
    parser.add_argument('--num_random', default = 10, type = int, help = ' number of additional, random, edges')
    parser.add_argument('--output_file_name', default = '', type = str, help = 'name of the output text file')
    args = parser.parse_args()

    if((args.num_parents*2+1)**2 - (args.num_parents*2 + 1 - 1) < args.num_random):
        raise Exception('za dużo randomowych krawędzi. Nie zmieści się tyle. :(')
    edges = generate_graph(args.num_parents, args.num_random)

    if(args.output_file_name == ''):
        for e in edges:
            print('{}, {}, {}'.format(get_v_name(e[0]), get_v_name(e[1]), e[2]))
        import sys
        sys.stdout.flush()

    else:
        with open(args.output_file_name, 'w') as file:
            for e in edges:
                print('{}, {}, {}'.format(get_v_name(e[0]), get_v_name(e[1]), e[2]))













