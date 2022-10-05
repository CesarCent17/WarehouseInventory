import mysql.connector


class Connection:
    def connect(self):
        dic = {
            "host": "localhost",
            "user": "root",
            "passwd": "Artn0w21",
            "database": "warehouseinventory",
        }

        connect_db = None
        try:
            connect_db = mysql.connector.connect(**dic)

        except(mysql.connector.DatabaseError, mysql.connector.OperationalError, mysql.connector.IntegrityError) as e:
            print("Error de conexion" + str(e))
        return connect_db



