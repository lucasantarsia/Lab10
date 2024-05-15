from database.DAO import DAO
from model.model import Model

model = Model()

res = DAO.getAllCountries()

print(len(res))

conn = DAO.getAllConnessioni(model._idMap, 2000)

print(len(conn))
