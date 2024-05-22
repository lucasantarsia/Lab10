import networkx as nx

from model.model import Model

myModel = Model()

myModel.creaGrafo(1980)

raggiungibili = myModel.getRaggiungibili(myModel._countries[0])

print(raggiungibili)
