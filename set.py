

class subsets:
    def __init__(self, num_vertexes):
        assert isinstance(num_vertexes, int)

        self.subsets = num_vertexes

        # każdy wierzchołek jest swoim własnym parentem
        self.parents = list(range(num_vertexes+1))
        # jak głębokie jest drzewo pod wierzchołkiem
        self.rank = [0]*(num_vertexes + 1)


    def find(self, vertex):
        if(self.parents[vertex] == vertex):
            return vertex

        return self.find(self.parents[vertex])

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        x_root_rank = self.rank[x_root]
        y_root_rank = self.rank[y_root]

        if(x_root_rank > y_root_rank):
            # jeśli drzewo pod wierzchołkiem x_root jest głębsze
            self.parents[y_root] = x_root
        elif(y_root_rank > x_root_rank):
            # jeśli jest na odwrót
            self.parents[x_root] = y_root
        else:
            # jeśli miały takie same głębokości
            self.parents[x_root] = y_root
            self.rank[x_root] += 1

        self.subsets -= 1