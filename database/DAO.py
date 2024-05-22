from model.connessione import Connessione
from database.DB_connect import DBConnect
from model.country import Country


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllCountries(year):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select c.StateAbb , c.CCode , c.StateNme 
                from country c , contiguity co
                where c.CCode = co.state1no 
                and co.`year` <= %s 
                group by c.CCode 
                order by c.StateAbb"""
        cursor.execute(query, (year,))

        for row in cursor:
            result.append(Country(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getConnessioni(idMap, year):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select co.state1no , co.state2no 
                from contiguity co 
                where co.`year` <= %s
                and co.conttype = 1
                and co.state1no < co.state2no"""
        cursor.execute(query, (year,))

        for row in cursor:
            result.append(Connessione(idMap[row["state1no"]], idMap[row["state2no"]]))

        cursor.close()
        conn.close()
        return result
