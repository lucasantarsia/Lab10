from time import time

import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):

        self._grafo = nx.Graph()
        self._countries = []  # lista di countries che popolo in creaGrafo
        self._idMap = {}

    def creaGrafo(self, year):
        self._countries = DAO.getAllCountries(year)
        for c in self._countries:
            self._idMap[c.CCode] = c

        self._grafo.clear()
        self._grafo.add_nodes_from(self._countries)
        self.addEdges(year)

    def addEdges(self, year):
        self._grafo.clear_edges()

        allEdges = DAO.getConnessioni(self._idMap, year)
        for e in allEdges:
            self._grafo.add_edge(e.c1, e.c2)

    def getNodes(self):
        return self._grafo.nodes

    def getNumConfinanti(self, v):
        return len(list(self._grafo.neighbors(v)))

    def getNumComponentiConnesse(self):
        # return len(list(nx.connected_components(self._grafo)))
        return nx.number_connected_components(self._grafo)

    def checkExistence(self, anno):
        if 1826 <= anno <= 2016:
            return True
        else:
            return False

    def getRaggiungibili(self, source):
        start = time()
        raggiungibiliDFS = self.getRaggiungibiliDFS(source)
        end = time()
        print(f"DFS: {end - start} - {len(raggiungibiliDFS)}")

        start = time()
        raggiungibiliBFS = self.getRaggiungibiliBFS(source)
        end = time()
        print(f"BFS: {end - start} - {len(raggiungibiliBFS)}")

        start = time()
        raggiungibiliRec = self.getRaggiungibiliRec(source)
        end = time()
        print(f"REC: {end - start} - {len(raggiungibiliRec)}")

        start = time()
        raggiungibiliIte = self.getRaggiungibiliIte(source)
        end = time()
        print(f"ITE: {end - start} - {len(raggiungibiliIte)}")

        return raggiungibiliDFS

    def getRaggiungibiliDFS(self, source):
        tree = nx.dfs_tree(self._grafo, source)
        raggiungibili = list(tree.nodes)
        raggiungibili.remove(source)
        return raggiungibili

    def getRaggiungibiliBFS(self, source):
        tree = nx.bfs_tree(self._grafo, source)
        raggiungibili = list(tree.nodes)
        raggiungibili.remove(source)
        return raggiungibili

    def getRaggiungibiliRec(self, source):
        visited = []
        self.recursion(visited, source)
        visited.remove(source)
        return visited

    def recursion(self, visited, source):
        visited.append(source)
        for country in self._grafo.neighbors(source):
            if country not in visited:
                self.recursion(visited, country)

    def getRaggiungibiliIte(self, source):
        # visited = []
        # to_visit = []
        # visited.append(source)
        # vicini = self._grafo.neighbors(source)
        # to_visit.extend(vicini)
        # while len(to_visit) > 0:
        #     for v in to_visit:
        #         vicini = self._grafo.neighbors(v)
        #         to_visit.extend(vicini)
        #         if v not in visited:
        #             visited.append(v)
        # return visited
        return []
