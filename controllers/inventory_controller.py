from dao.repository import Repository

class InventoryController:
    def __init__(self):
        self.repository = Repository()

    def get_productos(self):
        return self.repository.get_productos()

    def update_stock(self, id, stock):
        return self.repository.update_stock(id, stock)

    def insert_product(self, descripcion, stock):
        return self.repository.insert_product(descripcion, stock)

    def delete_product(self, id):
        return self.repository.delete_product(id)

