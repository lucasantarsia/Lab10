import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self._countryList = DAO.getAllCountries()
        self._grafo = nx.Graph()
        self._grafo.add_nodes_from(self._countryList)

        self._idMap = {}
        for c in self._countryList:
            self._idMap[c.CCode] = c

    def creaGrafo(self, intAnno):
        self.addEdges(intAnno)

    def addEdges(self, intAnno):
        self._grafo.clear_edges()

        allEdges = DAO.getAllConnessioni(self._idMap, intAnno)
        for e in allEdges:
            self._grafo.add_edge(e.v1, e.v2)

    def getSatiConfinanti(self):
        statiConfinanti = []
        count = 0
        for n in self._grafo.nodes:
            for u, v in self._grafo.edges:
                if u == n:
                    count += 1
            statiConfinanti.append((n, count))
        return statiConfinanti


    def checkExistence(self, anno):
        if 1826 <= anno <= 2016:
            return True
        else:
            return False
