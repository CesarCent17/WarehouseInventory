from tkinter import *
from tkinter import messagebox
from controllers.inventory_controller import InventoryController
from util.util import validate_positive_number


class AddStockView:
    def __init__(self, producto, inventory_view):
        self.window = None
        self.inventory_view = inventory_view
        self.inventory_controller = InventoryController()
        self.producto = producto
        self.get_window()

    def get_labels(self):
        # Labels
        self.lbl_id = Label(self.window, text="Id", font=("Arial", 14))
        self.lbl_id.configure(padx=10, pady=10)
        self.lbl_id.grid(row=0, column=0)

        self.lbl_descripcion = Label(self.window, text="Descripcion", font=("Arial", 14))
        self.lbl_descripcion.configure(padx=10, pady=10)
        self.lbl_descripcion.grid(row=1, column=0)

        self.lbl_stock = Label(self.window, text="Stock", font=("Arial", 14))
        self.lbl_stock.configure(padx=10, pady=10)
        self.lbl_stock.grid(row=2, column=0)

        self.lbl_ingreso = Label(self.window, text="Ingreso", font=("Arial", 14))
        self.lbl_ingreso.configure(padx=10, pady=10)
        self.lbl_ingreso.grid(row=3, column=0)

    def get_entrys(self):
        # Entrys
        self.entry_id = Entry(self.window, font=("Arial", 18))
        self.entry_id.insert("end", self.producto.id)
        self.entry_id.configure(state='disabled')
        self.entry_id.grid(row=0, column=1)

        self.entry_descripcion = Entry(self.window, font=("Arial", 18))
        self.entry_descripcion.insert("end", self.producto.descripcion)
        self.entry_descripcion.configure(state='disabled')
        self.entry_descripcion.grid(row=1, column=1)

        self.entry_stock = Entry(self.window, font=("Arial", 18))
        self.entry_stock.insert("end", self.producto.stock)
        self.entry_stock.configure(state='disabled')
        self.entry_stock.grid(row=2, column=1)

        self.entry_ingreso = Entry(self.window, font=("Arial", 18))
        self.entry_ingreso.grid(row=3, column=1)

    def get_buttons(self):
        # Buttons
        self.btn_aceptar = Button(self.window, text="Aceptar",
                                     font=("Arial", 14), borderwidth=False, bg="#5D5DF1",
                                     highlightthickness=False, relief="flat", fg="white", command=self.click_aceptar)
        self.btn_aceptar.grid(row=4, column=0)

        self.btn_cancelar = Button(self.window, text="Cancelar",
                                  font=("Arial", 14), borderwidth=False,
                                  highlightthickness=False, relief="flat", bg="#F15D5D",fg="white",command=self.window.destroy)
        self.btn_cancelar.grid(row=4, column=1)

    def click_aceptar(self):
        try:
            add_stock = int(self.entry_ingreso.get())
            response = validate_positive_number(add_stock)

            #Si el numero es positivo
            if response[1]:
                stock = int(self.producto.stock)
                stock_actualizado = add_stock + stock
                id = self.producto.id
                response = self.inventory_controller.update_stock(id, stock_actualizado)

                if response[1]:
                    msg = f"Se ha ingresado correctamente, " \
                          f"la nueva cantidad en stock disponible es de: {stock_actualizado}"
                    messagebox.showinfo("Ingreso exitoso", msg)
                    self.inventory_view.update_product_list()
                    self.window.destroy()

                elif response[1] == False:
                    msg = "Error al registrar el ingreso por favor intentelo nuevamente"
                    messagebox.showwarning("Error", msg)

            elif response[1] == False:
                messagebox.showwarning("Error", response[0])
        except ValueError:
            messagebox.showwarning("Error", "Carácter inválido")

    def get_window(self):
        self.window = Tk()
        self.window.geometry("430x300")
        self.window.title("Ingreso")
        self.window.resizable(False, False)
        self.get_labels()
        self.get_entrys()
        self.get_buttons()
        self.window.mainloop()





