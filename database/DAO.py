from connessione import Connessione
from database.DB_connect import DBConnect
from model.country import Country


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllCountries():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                from country c
                order by c.StateAbb"""
        cursor.execute(query, ())

        for row in cursor:
            result.append(Country(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllConnessioni(idMap, anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select c.state1no as s1, c.state2no as s2
                from contiguity c 
                where c.conttype = 1 
                and c.`year` <= %s 
                and c.state1no < c.state2no"""
        cursor.execute(query, (anno,))

        for row in cursor:
            result.append(Connessione(idMap[row["s1"]], idMap[row["s2"]]))

        cursor.close()
        conn.close()
        return result
