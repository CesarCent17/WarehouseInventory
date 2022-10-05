from dao.connection import Connection
from models.usuario import Usuario

class Auth:
    def __init__(self):
        self.connect_db = Connection()

    def getUserAuth(self, email, passw):
        user = None
        cnn = self.connect_db.connect()
        cur = cnn.cursor()
        query = f"SELECT * FROM usuario WHERE email = '{email}' and passw = '{passw}'"
        cur.execute(query)
        data = cur.fetchall()
        if len(data) == 1:
            user = Usuario(data[0][1], data[0][2], data[0][3])
        cnn.commit()
        cur.close()
        return user


