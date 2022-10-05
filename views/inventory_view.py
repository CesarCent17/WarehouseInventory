import sys
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from .add_stock_view import AddStockView
from controllers.inventory_controller import InventoryController
from models.producto import Producto
from .add_product_view import AddProductView
from .delete_product_view import DeleteProductView


class InventoryView:
    def __init__(self, user):
        # class attributes
        self.label_inventario = None
        self.label_user = None
        self.treeview = None
        self.window = None
        self.list_productos = []
        self.inventory_controller = InventoryController()
        self.get_window(user)

    def show_table(self):
        self.treeview = ttk.Treeview(self.window, columns=(1, 2, 3), show="headings", height=10)

        scrollbar = ttk.Scrollbar(self.window, orient="vertical", command=self.treeview.yview)
        scrollbar.place(x=810, y=130, height=250)
        self.treeview.configure(yscrollcommand=scrollbar.set)

        self.treeview.heading(1, text="Id")
        self.treeview.heading(2, text="Descripcion")
        self.treeview.heading(3, text="Stock")
        self.get_data_table()
        self.treeview.column(1, anchor=CENTER, width=80)
        self.treeview.column(2, anchor=CENTER, width=250)
        self.treeview.column(3, anchor=CENTER, width=120)
        self.treeview.grid(row=4, column=1)
        self.treeview.configure(padding=(50, 0))
        self.treeview.bind("<Double-1>", self.click_select)


    def click_select(self, event):
        try:
            item = self.treeview.identify('item', event.x, event.y)
            id = self.treeview.item(item, "values")[0]
            descripcion = self.treeview.item(item, "values")[1]
            stock = self.treeview.item(item, "values")[2]
            producto = Producto(id, descripcion, stock)
            AddStockView(producto, self)
        except:
            messagebox.showwarning("Ingreso", "No ha seleccionado ningun producto")

    def get_labels(self, user):
        self.label_inventario = Label(self.window, text="Inventario de productos", font=("Arial", 18, 'bold'))
        self.label_inventario.configure(pady=20)
        self.label_inventario.grid(row=1, column=1)

        text = f"Bienvenido {user.usuario}"
        self.label_user = Label(self.window, text=text, font=("Arial", 12,))
        #self.label_user.place(x=20, y=20)
        self.label_user.configure(pady=20, padx=10)
        self.label_user.grid(row=0, column=0)

    def get_window(self, user):
        self.window = Tk()
        self.window.geometry("900x600")
        self.window.title("Inventario Bodega")
        self.window.resizable(False, False)
        self.get_labels(user)
        self.get_buttons()
        self.show_table()
        self.window.mainloop()

    def get_data_table(self):
        self.list_productos = self.inventory_controller.get_productos()
        for i in range(len(self.list_productos)):
            self.treeview.insert("", "end", values=(self.list_productos[i].id, self.list_productos[i].descripcion,
                                                    self.list_productos[i].stock))

    def get_buttons(self):
        self.btn_nuevo_producto = Button(self.window, text="Nuevo Producto",
                                         font=("Arial", 14), borderwidth=False, bg="#5D5DF1",
                                         highlightthickness=False, relief="flat", fg="white",
                                         command=self.click_nuevo_producto)
        self.btn_nuevo_producto.place(x=100, y=380, width=200, height=50)

        self.btn_eliminar_producto = Button(self.window, text="Eliminar Producto",
                                            font=("Arial", 14), borderwidth=False,
                                            highlightthickness=False, relief="flat", bg="#F15D5D", fg="white",
                                            command=self.click_eliminar_producto,
                                            )
        self.btn_eliminar_producto.place(x=350, y=380, width=200, height=50)

        self.btn_salir_aplicacion = Button(self.window, text="Cerrar Aplicacion",
                                            font=("Arial", 14), borderwidth=False,
                                            highlightthickness=False, relief="flat", bg="#2A3E85", fg="white",
                                            command=self.click_salir_aplicacion,
                                            )
        self.btn_salir_aplicacion.place(x=600, y=20, width=180, height=40)

    def update_product_list(self):
        self.show_table()

    def click_nuevo_producto(self):
        AddProductView(self)

    def click_eliminar_producto(self):
        try:
            id = self.treeview.item(self.treeview.selection())['values'][0]
            DeleteProductView(id, self)
        except:
            messagebox.showwarning("Eliminar", "No ha seleccionado ningun producto")

    def click_salir_aplicacion(self):
        value = messagebox.askquestion("Salir", "¿Estás seguro de querer salir de la App?")
        if value == "yes":
            self.window.destroy()
            sys.exit()

