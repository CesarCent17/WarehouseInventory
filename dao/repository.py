from dao.connection import Connection
from models.producto import Producto
from models.usuario import Usuario

class Repository:
    def __init__(self):
        self.connect_db = Connection()

    def get_productos(self):
        """ Retorna una lista con todos los productos. """
        cnn = self.connect_db.connect()
        cur = cnn.cursor()
        query = "SELECT id, descripcion, stock FROM producto;"
        cur.execute(query)
        data = cur.fetchall()
        list_productos = []

        for i in range(len(data)):
            producto = Producto(data[i][0], data[i][1], data[i][2])
            list_productos.append(producto)
        cur.close()
        return list_productos

    def update_stock(self, id, stock):
        response = ["", 0]
        try:
            cnn = self.connect_db.connect()
            cur = cnn.cursor()
            data = (stock,id)
            cur.execute("UPDATE producto SET stock = %s WHERE id = %s", data)
            cnn.commit()
            cur.close()
            msg = str(cur.rowcount) + " registro (s) afectados."
            response = [msg, 1]
        except Exception as e:
            msg = str(e)
            response = [msg, 0]
        return response

    def insert_product(self, descripcion, stock):
        response = ["", 0]
        try:
            cnn = self.connect_db.connect()
            cur = cnn.cursor()
            data = (descripcion, stock)
            cur.execute("INSERT INTO producto(id, descripcion, stock) VALUES (null, %s, %s);", data)
            cnn.commit()
            cur.close()
            msg = str(cur.rowcount) + " registro (s) afectados."
            response = [msg, 1]
        except Exception as e:
            msg = str(e)
            response = [msg, 0]
        return response

    def delete_product(self, id):
        response = ["", 0]
        try:
            cnn = self.connect_db.connect()
            cur = cnn.cursor()
            data = [id]
            cur.execute("DELETE FROM producto WHERE id=%s;", data)
            cnn.commit()
            cur.close()
            msg = str(cur.rowcount) + " registro (s) afectados."
            response = [msg, 1]
        except Exception as e:
            msg = str(e)
            response = [msg, 0]
        return response

    def insert_user(self, user):
        response = ["", 0]
        try:
            cnn = self.connect_db.connect()
            cur = cnn.cursor()
            data = [user.usuario, user.email, user.passw]
            cur.execute("INSERT INTO usuario(id, usuario, email, passw) VALUES (null, %s, %s, %s);", data)
            cnn.commit()
            cur.close()
            msg = str(cur.rowcount) + " registro (s) afectados."
            response = [msg, 1]
        except Exception as e:
            msg = str(e)
            response = [msg, 0]
        return response










