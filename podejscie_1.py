import sys
import time
from set import subsets


class Solver:

    def __init__(self):
        self.edges = []
        self.subsets = None

    def read_graph(self):
        """
        fukncja wczytująca graf ze standardowego wejścia
        """
        edges = []
        for l in sys.stdin:
            src, tgt, w = [x.strip() for x in l.split(',')]
            edges.append((src, tgt, int(w)))

        self.edges = edges

    def _sort_graph(self):
        """
        sortowanie grafu

        :param edges: list(tuple()) lista zawierająca krotki opisujące poszczególne połącznia w grafie.
        """
        self.edges = sorted(self.edges, key=lambda x: x[2], reverse=True)

    def _decode_graph(self):
        self.max_index = 0
        self.map = {}
        self.edges = list(map(lambda x: (int(x[0]), int(x[1]), x[2]), self.edges))
        for i, e in enumerate(self.edges):
            if (e[0] not in self.map):
                self.max_index += 1
                self.map[e[0]] = self.max_index
            if (e[1] not in self.map):
                self.max_index += 1
                self.map[e[1]] = self.max_index

            self.edges[i] = (self.map[e[0]], self.map[e[1]], e[2])

        self.num_vertexes = int(max(map(lambda x: max(x[0], x[1]), self.edges)))

    # ! /bin/python3

    def solve(self, timeit):
        final_edges = []
        self._decode_graph()
        t = time.time()
        self._sort_graph()

        self.subsets = subsets(self.num_vertexes)
        for e in self.edges:
            subset_root1 = self.subsets.find(e[0])
            subset_root2 = self.subsets.find(e[1])

            if (subset_root1 != subset_root2):
                # nie są połączone:
                self.subsets.union(subset_root2, subset_root1)
                final_edges.append(e)

        if (self.subsets.subsets != 1):
            print(self.subsets.subsets)
            raise Exception('Nie da się znaleźć wartości maksymalnej')
        if (timeit):
            # pomiar czasu
            return time.time() - t
        else:
            return min([x[2] for x in final_edges])


if (__name__ == '__main__'):
    s = Solver()
    s.read_graph()
    if (len(sys.argv) > 1 and sys.argv[1] == 'timeit'):
        rval = s.solve(timeit=True)
    else:
        rval = s.solve(timeit=False)
    print(rval)
