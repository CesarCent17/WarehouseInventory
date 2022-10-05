from tkinter import *
from controllers.inventory_controller import InventoryController
from tkinter import messagebox


class DeleteProductView:
    def __init__(self, id, inventory_view):
        self.id_producto = id
        self.inventory_view = inventory_view
        self.inventory_controller = InventoryController()
        self.get_window()

    def get_window(self):
        self.window = Tk()
        self.window.geometry("430x100")
        self.window.title("Confirmacion")
        self.window.resizable(False, False)
        self.get_labels()
        self.get_buttons()
        self.window.mainloop()

    def get_labels(self):
        # Labels
        self.lbl_pregunta = Label(self.window, text="¿Estás seguro de querer eliminar?", font=("Arial", 14))
        self.lbl_pregunta.configure(padx=10, pady=10)
        self.lbl_pregunta.grid(row=0, column=0)

    def get_buttons(self):
        # Buttons
        self.btn_aceptar = Button(self.window, text="Aceptar",
                                  font=("Arial", 14), borderwidth=False, bg="#5D5DF1",
                                  highlightthickness=False, relief="flat", fg="white", command=self.click_aceptar)
        self.btn_aceptar.grid(row=1, column=0)

        self.btn_cancelar = Button(self.window, text="Cancelar",
                                   font=("Arial", 14), borderwidth=False,
                                   highlightthickness=False, relief="flat", bg="#F15D5D", fg="white",
                                   command=self.window.destroy)
        self.btn_cancelar.grid(row=1, column=1)

    def click_aceptar(self):
        response = self.inventory_controller.delete_product(self.id_producto)
        if response[1]:
            messagebox.showinfo("Eliminar", "El producto se ha eliminado correctamente")
            self.inventory_view.update_product_list()
            self.window.destroy()
        elif response[1] == False:
            messagebox.showwarning("Eliminar", response[0])








