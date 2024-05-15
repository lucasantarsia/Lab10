from model.model import Model

myModel = Model()

myModel.creaGrafo(2000)

# print(len(myModel._grafo.nodes))
# print(len(myModel._grafo.edges))

for v in myModel._grafo.nodes:
    print(f"{v} -- {len(list(myModel._grafo.neighbors(v)))}")

# for u, v in myModel._grafo.edges:
#     print(f"{u} --- {v}")
