from tkinter import *
from controllers.login_controller import LoginController
from tkinter import messagebox
from views.inventory_view import InventoryView
from .register_form_view import RegisterFormView


class LoginView:
    def __init__(self):
        # class attributes
        self.window = None
        self.registrarse = None
        self.iniciar_sesion = None
        self.lbl_password = None
        self.lbl_email = None
        self.entry_passw = None
        self.entry_email = None
        self.login_controller = LoginController()
        self.get_window()

    def get_labels(self):
        # Labels
        self.lbl_email = Label(self.window, text="Email", font=("Arial", 18)).place(x=185, y=220)
        self.lbl_password = Label(self.window, text="Password", font=("Arial", 18)).place(x=175, y=300)

    def get_entrys(self):
        # Entrys
        self.entry_email = Entry(self.window, font=("Arial", 18))
        self.entry_email.place(x=300, y=220)
        self.entry_passw = Entry(self.window, font=("Arial", 18))
        self.entry_passw.place(x=300, y=300)

    def get_buttons(self):
        # Buttons
        self.iniciar_sesion = Button(self.window, text="Iniciar Sesion",
                                     font=("Arial", 18), borderwidth=False, bg="#5D5DF1",
                                     highlightthickness=False, relief="flat", fg="white",
                                     command=self.click_iniciar_sesion) \
            .place(x=250, y=380, width=200, height=50)

        self.registrarse = Button(self.window, text="Registrarse",
                                  font=("Arial", 18), borderwidth=False,
                                  highlightthickness=False, relief="flat", fg="#5D5DF1", command=self.click_registrarse) \
            .place(x=450, y=380, width=180, height=50)

    def get_window(self):
        # Main Window
        self.window = Tk()
        self.window.geometry("900x600")
        self.window.title("Inventario Bodega")
        self.window.resizable(False, False)

        self.get_labels()
        self.get_entrys()
        self.get_buttons()
        self.window.mainloop()

    def click_iniciar_sesion(self):
        txt_email = self.entry_email.get()
        txt_passw = self.entry_passw.get()
        user = self.login_controller.getUserAuth(txt_email, txt_passw)

        if user:
            messagebox.showinfo("Login exitoso", "Bienvenido " + txt_email)
            self.window.withdraw()
            InventoryView(user)
        else:
            messagebox.showwarning("Error", "Credenciales incorrectas por favor intentelo nuevamente")

    def click_registrarse(self):
        self.window.withdraw()
        RegisterFormView(self)


