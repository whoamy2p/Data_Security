#! /usr/bin/env python3

from tkinter import *
import sqlite3
from pack_method.conection_db import request_db

class Register ():
    def __init__(self):
        pass

    def regis (self):
        self.window_register = Tk ()
        self.window_register.title ("Register")
        self.window_register.geometry ("800x760")
        self.window_register.resizable (False, False)

        Label (self.window_register, text="DARK APPLICATIONS", height=2, font=("Algerian 20 bold")).grid (row=0, column=0, columnspan=3, sticky=E+W)

        self.imge = PhotoImage (file="App/media/img/linux.png")
        Label (self.window_register, image=self.imge ,width=380, height=600).grid (row=1, column=0, padx=5)

        # Form python
        self.container_login = Frame (self.window_register, bd=7, cursor="hand2")

        Label (self.container_login, text="Name *", font=("Cambria 12 bold")).grid (row=1, column=0, pady=8, sticky=W)
        self.name = Entry (self.container_login, font=("Cambria 12"), justify=CENTER)
        self.name.grid (row=2, column=0, sticky=W+E, pady=3, padx=2)

        Label (self.container_login, text="Last Name *", font=("Cambria 12 bold")).grid (row=1, column=1, pady=8, sticky=W)
        self.last_name = Entry (self.container_login, font=("Cambria 12"), justify=CENTER)
        self.last_name.grid (row=2, column=1, sticky=W+E, pady=3, padx=2)

        Label (self.container_login, text="Username *", font=("Cambria 12 bold")).grid (row=3, column=0, columnspan=2, pady=8, sticky=W)
        self.username = Entry (self.container_login, font=("Cambria 12"), justify=CENTER)
        self.username.grid (row=4, column=0, columnspan=2, sticky=W+E, pady=3, padx=2)

        Label (self.container_login, text="Passwword *", font=("Cambria 12 bold")).grid (row=5, column=0, columnspan=2, pady=8, sticky=W)
        self.password = Entry (self.container_login, font=("Cambria 12"), justify=CENTER, show="*")
        self.password.grid (row=6, column=0, columnspan=2, sticky=W+E, pady=3, padx=2)

        Label (self.container_login, text="Password confirmation *", font=("Cambria 12 bold")).grid (row=7, column=0, columnspan=2, pady=8, sticky=W)
        self.Password_confirmation= Entry (self.container_login, font=("Cambria 12"), justify=CENTER, show="*")
        self.Password_confirmation.grid (row=8, column=0, columnspan=2, sticky=W+E, pady=3, padx=2)

        Label (self.container_login, text="Date of birth *", font=("Cambria 12 bold")).grid (row=9, column=0, columnspan=2, pady=8, sticky=W)

        self.frame1 = Frame (self.container_login)
        self.day = Entry (self.frame1, width=10, font=("Cambria 12"))
        self.day.grid (row=0, column=0, padx=5, pady=3)

        self.month = Spinbox (self.frame1, values=("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"), width=15)
        self.month.grid (row=0, column=1, padx=5, pady=3)

        self.year = Entry (self.frame1, width=15, font=("Cambria 12"))
        self.year.grid (row=0, column=3, padx=5, pady=3)

        self.frame1.grid (row=10, column=0, columnspan=2, sticky=W+E)

        Label (self.container_login, text="Sex *", font=("Cambria 12 bold")).grid (row=11, column=0, columnspan=2, pady=3, sticky=W)

        self.option = IntVar ()
        self.women = Radiobutton (self.container_login, text="Woman", variable=self.option, value=1, font=("Cambria 12"))
        self.women.grid (row=12, column=0, padx=2)

        self.man = Radiobutton (self.container_login, text="Man", variable=self.option, value=2, font=("Cambria 12"))
        self.man.grid (row=12, column=1, padx=2)

        Label (self.container_login, text="Mobile phone *", font=("Cambria 12 bold")).grid (row=13, column=0, columnspan=2, pady=8, sticky=W)
        self.mobile_phone = Entry (self.container_login, font=("Cambria 12"))
        self.mobile_phone.grid (row=14, column=0, sticky=W+E, padx=2, pady=3)

        Label (self.container_login, text="Your current e-mail *", font=("Cambria 12 bold")).grid (row=15, column=0, columnspan=2, pady=8, sticky=W)
        self.email_current = Entry (self.container_login, font=("Cambria 12"))
        self.email_current.grid (row=16, column=0, columnspan=2, sticky=W+E, padx=2, pady=3)

        robot = IntVar ()
        self.check = Checkbutton (self.container_login, text="I am not a robot", variable=robot, onvalue=1, offvalue=0, font=("Cambria 12 bold"))
        self.check.grid (row=17, column=0, sticky=W+E, padx=2, pady=3)

        Button (self.container_login, text="Submit", font=("Cambria 12 bold"), activebackground="black", activeforeground="white", bg=None, relief="raise", bd=4, command=lambda: self.__send_data ()).grid (row=18, column=0, columnspan=2, sticky=W+E, pady=15)

        Button (self.container_login, text="¿Ya tienes una cuenta? Inicia Sesión", relief=GROOVE, foreground="blue", command=lambda: self.window_register.destroy ()).grid (row=19, column=0, sticky=W+E)

        self.container_login.grid (row=1, column=1, padx=5, sticky=N+S+W+E)

        self.window_register.mainloop ()

        # ****************************************
    def captureForm (self):
        self.genero = ""
        if self.option == 1:
            self.genero = "Woman"
        else:
            self.genero = "Man"

        self.date = ("{}/{}/{}").format (self.day.get (), self.month.get (), self.year.get ())
        # *****************************************

        self.data_gui = {
            "name":self.name.get (), 
            "last_name":self.last_name.get (), 
            "username":self.username.get (), 
            "password":self.password.get (), 
            "pass_confirmation":self.Password_confirmation.get (), 
            "date":self.date, 
            "genero":self.genero, 
            "phone":self.mobile_phone.get ()
        }
        return self.data_gui

    # aqui estamo falta aanalizar ese error de cargar los datos a la db
    def __send_data (self):
        data_Form = self.captureForm ()
        if self.validator.validate_data (self, data_Form):
            try:
                query = "INSERT INTO REGISTER VALUES (NULL, ?,?,?,?,?,?,?,?)"
                request_db (query, [form for form in data_Form.values ()])
            except sqlite3.DatabaseError as sdt:
                print ("la variable result se asgino antes de llamrla")
            else:
                self.window_register.destroy ()
        
        else:
            print ("no se guardaron los datos")




# if __name__ == "__register__":
#     obj= Register ()   