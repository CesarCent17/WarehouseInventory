from tkinter import *
from controllers.register_form_controller import RegisterFormController
from models.usuario import Usuario
from tkinter import messagebox

class RegisterFormView:
    def __init__(self, login_view):
        self.login_view = login_view
        self.register_form_controller = RegisterFormController()
        self.get_window()


    def get_window(self):
        self.window = Tk()
        self.window.geometry("430x300")
        self.window.title("Formulario de registro")
        self.window.resizable(False, False)
        self.get_labels()
        self.get_entrys()
        self.get_buttons()
        self.window.mainloop()

    def get_labels(self):
        # Labels
        self.lbl_usuario = Label(self.window, text="Usuario", font=("Arial", 14))
        self.lbl_usuario.configure(padx=10, pady=10)
        self.lbl_usuario.grid(row=0, column=0)

        self.lbl_email = Label(self.window, text="Email", font=("Arial", 14))
        self.lbl_email.configure(padx=10, pady=10)
        self.lbl_email.grid(row=1, column=0)

        self.lbl_contrasena = Label(self.window, text="Contraseña", font=("Arial", 14))
        self.lbl_contrasena.configure(padx=10, pady=10)
        self.lbl_contrasena.grid(row=2, column=0)

    def get_entrys(self):
        # Entrys
        self.entry_usuario = Entry(self.window, font=("Arial", 18))
        self.entry_usuario.grid(row=0, column=1)

        self.entry_email = Entry(self.window, font=("Arial", 18))
        self.entry_email.grid(row=1, column=1)

        self.entry_contrasena = Entry(self.window, font=("Arial", 18))
        self.entry_contrasena.grid(row=2, column=1)

    def get_buttons(self):
        # Buttons
        self.btn_aceptar = Button(self.window, text="Aceptar",
                                     font=("Arial", 14), borderwidth=False, bg="#5D5DF1",
                                     highlightthickness=False, relief="flat", fg="white", command=self.click_aceptar)
        self.btn_aceptar.grid(row=4, column=0)

        self.btn_cancelar = Button(self.window, text="Cancelar",
                                  font=("Arial", 14), borderwidth=False,
                                  highlightthickness=False, relief="flat", bg="#F15D5D",fg="white",command=self.click_cancelar)
        self.btn_cancelar.grid(row=4, column=1)

    def click_aceptar(self):
        user = self.entry_usuario.get()
        email =self.entry_email.get()
        passw = self.entry_contrasena.get()
        if user == "" or email == "" or passw == "":
            messagebox.showwarning("Registro", "Por favor llene los campos")
            return
        usuario = Usuario(user, email, passw)
        response = self.register_form_controller.insert_user(usuario)
        if response[1]:
            messagebox.showinfo("Registro", "Usuario registrado correctamente")
            self.window.destroy()
            self.login_view.window.deiconify()
        else:
            messagebox.showerror("Registro", "Ha ocurrido un error, intentelo nuevamente")

    def click_cancelar(self):
        self.window.destroy()
        self.login_view.window.deiconify()



