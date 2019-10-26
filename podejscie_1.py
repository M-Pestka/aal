import sys


def read_graph():
    edges = []
    for l in sys.stdin:
        src, tgt, w = [x.strip() for x in l.split(',')]
        edges.append((src, tgt, int(w)))

    return edges

def sort_graph(edges):
    return sorted(edges, key = lambda x: x[2], reverse = True)


if(__name__ == '__main__'):

    edges = read_graph()
    edges = sort_graph(edges)

    subtrees = []
    final_edges = []
    for e in edges:
        new_subtree = True
        set_number_v1 = -1
        set_number_v2 = -1
        for i, st in enumerate(subtrees):
            v1 = e[0] in st
            v2 = e[1] in st
            if(v1 and v2):
                # byłby cykl w grafie
                new_subtree = False
                break
            
            if(v1):
                # dołączmy tę krawędź do istniejącego drzewa
                st.add(e[1])
                set_number_v1 = i
                new_subtree = False
                final_edges.append(e)
                

            if(v2):
                # dołączmy tę krawędź do istniejącego drzewa
                st.add(e[0])
                set_number_v2 = i
                new_subtree = False
                final_edges.append(e)
                
            
            # lecimy w pętli

        # tworzymy nowe poddrzewo
        if(new_subtree):
            final_edges.append(e)
            subtrees.append(set(e[:2]))

        else:
            # sprawdzamy czy należy połączyć 2 zbiory wierzchołków
            if(set_number_v1 != -1 and set_number_v2 != -1):
                subtrees[set_number_v1] = subtrees[set_number_v1].union(subtrees[set_number_v2])
                subtrees.remove(subtrees[set_number_v2])

    print(min([x[2] for x in final_edges]))
