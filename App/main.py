
from inspect import Attribute
from sys import path
path.append('..\\secure_data')
# path.append('C:\\Users\\user\\py\\secure_data')

from Views_App.login import Login
from Views_App.loading import Loading
from pack_method.method import time_window, methods, data_encrypt
from tkinter import *
from tkinter import ttk, messagebox
from pack_method.conection_db import Insert_dataDB, Delete_dataDB, Update_dataDB, Search_DB

class Principal:
    # Instanciamos las clases importadas
    validate = methods ()
    encryptCode = data_encrypt ()
    dt = time_window ()

    def __init__(self):
        """
        instaciamos la clase Login()
        """
        self.login = Login ()
        try:
            self.userr = self.login.user_id
        except AttributeError as at:
            return

        # sesion se vuelve True cuando el usuario inicia sesión correctamente
        if self.login.sesion == True:
            #Loading () # revisar esta función
            
            """
            Creamos la pantalla principal de la APP
            """
            self.window = Tk ()
            self.window.title ("Count email")
            self.window.geometry ("1530x784")
            self.window.iconbitmap ("App/media/img/Logo/icon_Logo.ico")
            # self.window.resizable (False, False)
            self.window.config (bg="#3c3c3c")

            # ---------- Menú ----------------
            self.Menu_bar = Menu ()
            self.window.config (menu=self.Menu_bar)

            self.Archive = Menu (self.Menu_bar, tearoff=0)
            self.Archive.add_command (label="New", command=lambda: self.window_two ())
            self.Archive.add_separator ()
            self.Archive.add_command (label="Exit", command=lambda: self.window.destroy ())
            self.Menu_bar.add_cascade (label="Archive", menu=self.Archive)

            self.Edit = Menu (self.Menu_bar, tearoff=0)
            self.Edit.add_command (label="Undo", command=lambda: self.messenger ())
            self.Edit.add_command (label="Redo", command=lambda: self.messenger ())
            self.Menu_bar.add_cascade (label="Edit", menu=self.Edit)

            self.Tool = Menu (self.Menu_bar, tearoff=0)
            self.Tool.add_radiobutton (label="Encrypted", command=lambda: self.validate.update_table (self.userr, self.table, self.encryptCode, 1, self.mail_list, self.account_list, self.url_list))
            self.Tool.add_radiobutton (label="Desencrypted", command=lambda: self.validate.update_table (self.userr, self.table, self.encryptCode, 2, self.mail_list, self.account_list, self.url_list))
            self.Tool.add_separator ()
            self.Tool.add_command (label="Filters")
            self.Menu_bar.add_cascade (label="Tools", menu=self.Tool)

            self.Help = Menu (self.Menu_bar, tearoff=0)
            self.Help.add_command (label="Documentation", command=lambda: self.messenger ())
            self.Help.add_command (label="Release note", command=lambda: self.messenger ())
            self.Help.add_separator ()
            self.Help.add_command (label="See license", command=lambda: self.License ())
            self.Help.add_command (label="Privacy statement", command=lambda: self.messenger ())
            self.Help.add_separator ()
            self.Help.add_command (label="About", command=lambda: self.about ())
            self.Menu_bar.add_cascade (label="Help", menu=self.Help)


            # ----------- Creamos el Frame de contiene perfil y nombre usuario -------------

            self.container_0 = Frame (self.window, relief=RIDGE, bg="#212121") #336666: turquesa oscuro
            self.container_0.grid (row=0, column=0, columnspan=2, rowspan=3)

            self.img_profile = PhotoImage (file="App/media/img/profile_160x160.png")

            Label (self.container_0, image=self.img_profile, bg="white").grid (row=0, column=0, padx=10, pady=3)
            Label (self.container_0, text=f"{self.login.name_user}".title(), bg="#212121", foreground="white", font=("Cambria 11 bold")).grid (row=1, column=0, pady=3)

            """
             Creamos el contendor de los Notebook o pestañas 
            """
            self.Frame_notebook = Frame (self.container_0, borderwidth=5, background="#212121")
            self.Frame_notebook.grid (row=2, column=0, sticky=W+E, ipady=10, padx=10, pady=8)

            # creamos los Notebook o pestañas (2 pestañas)

            tab = ttk.Notebook (self.Frame_notebook, height=508, width=317)#, background="#212121"
            tab.grid (row=3, column=0, columnspan=2, sticky=W+E, ipadx=3)

            # ----------- Creamos el Frame1 contenedor de la primera pestaña ---------
            self.frame1 = Frame (tab, background="#212121") # turquesa mas claro
            self.frame1.grid (row=0, column=0, sticky=W+E)
 
            self.labelFrame_option = LabelFrame (self.frame1, text="Options", font=("Cambria 11 bold"), width=48, background="#212121", foreground="#CCFFFF") # CCFFFF: color celeste claro
            self.labelFrame_option.grid (row=0, column=0, columnspan=2, sticky=W+E, pady=6)
            Button (self.labelFrame_option, text="Add", foreground="blue", font=("Cambria 11 bold"), width=10, command=lambda: self.window_two (), justify=CENTER).grid (row=1, column=0, columnspan=2, sticky=W+E, padx=3, pady=10)

            Label (self.frame1, text="Mail list", font=("Cambria 11 bold"), background="#212121", foreground="#CCFFFF").grid (row=2, column=0, columnspan=2, sticky=W, padx=4, pady=4)
            self.mail_list = Listbox (self.frame1, width=37, height=8, font=("Cambria 11"))
            self.mail_list.grid (row=3, column=0, sticky=W+E)

            scroll_vertical1 = Scrollbar (self.frame1, command=self.mail_list.yview, orient="vertical")
            scroll_vertical1.grid (row=3, column=1, sticky="nsew")

            scroll_horizontal1 = Scrollbar (self.frame1, command=self.mail_list.xview, orient="horizontal")
            scroll_horizontal1.grid (row=4, column=0, sticky="ewns", columnspan=2)

            self.mail_list.config (yscrollcommand=scroll_vertical1.set, xscrollcommand=scroll_horizontal1.set)

            Label (self.frame1, text="Account list", font=("Cambria 11 bold"), background="#212121", foreground="#CCFFFF").grid (row=5, column=0, columnspan=2, sticky=W, padx=4, pady=4)
            self.account_list = Listbox (self.frame1, width=37, height=7, font=("Cambria 11"))
            self.account_list.grid (row=6, column=0, sticky=W+E)

            scroll_vertical2 = Scrollbar (self.frame1, command=self.account_list.yview)
            scroll_vertical2.grid (row=6, column=1, sticky="nsew")

            scroll_horizontal2 = Scrollbar (self.frame1, command=self.account_list.xview, orient="horizontal")
            scroll_horizontal2.grid (row=7, column=0, sticky="ewns", columnspan=2)

            self.account_list.config (yscrollcommand=scroll_vertical2.set, xscrollcommand=scroll_horizontal2.set)


            separador = ttk.Separator (self.frame1, orient="horizontal")
            separador.grid (row=8, column=0, columnspan=2, sticky=W+E, pady=5, padx=20)

            Button (self.frame1, text="Close", font=("Cambria 12 bold"), activeforeground="red", borderwidth=2, justify=CENTER, background="#004D40", foreground="#B2DFDB", width=12, command=lambda: self.window.destroy ()).grid (row=9, column=0, padx=4, pady=3)#00FF00 : color verde fosforocente, #FF00FF: color purpura

            #  --------------- Creamos el Frame2 contenedor de la segunda pestaña -------------
            self.frame2 = Frame (tab, background="#212121")
            self.frame2.grid (row=0, column=0, sticky=W+E)

            self.labelframe_vista = LabelFrame (self.frame2, text="Visualize", font=("Cambria 11 bold"), foreground="#CCFFFF", width=208, bg="#212121")
            self.labelframe_vista.grid (row=0, column=0, pady=5, padx=10, sticky=W+E, columnspan=2)

            var2 = 2
            var1 = 1
            self.var = IntVar ()

            Radiobutton (self.labelframe_vista, text="Encrypted", variable=self.var, value=1, width=12, bg="#212121", activebackground="#212121", font=("Cambria 11"), foreground="#00FF00", command=lambda: self.validate.update_table (self.userr, self.table, self.encryptCode, var1, self.mail_list, self.account_list, self.url_list)).grid (row=0, column=0, pady=3, padx=5, sticky=W, ipadx=10)  #00CC00: color PLOMO

            Radiobutton (self.labelframe_vista, text="Desencrypted", variable=self.var, value=2, width=12, bg="#212121", activebackground="#212121", font=("Cambria 11"), foreground="#00FF00", command=lambda: self.validate.update_table (self.userr, self.table, self.encryptCode, var2, self.mail_list, self.account_list, self.url_list)).grid (row=0, column=1, pady=3, padx=5, sticky=W, ipadx=10)

        
            Label (self.frame2, text="Url list", bg="#212121", font=('Cambria 11 bold'), foreground="#CCFFFF").grid (row=1, column=0, pady=5)
            self.url_list = Listbox (self.frame2, width=37, height=8, font=("Cambria 11")) # esto es solo relleno
            self.url_list.grid (row=2, column=0, sticky=W+E)

            scroll_vertical3 = Scrollbar (self.frame2, command=self.url_list.yview)
            scroll_vertical3.grid (row=2, column=1, sticky="nsew")

            scroll_horizontal3 = Scrollbar (self.frame2, command=self.url_list.xview, orient="horizontal")
            scroll_horizontal3.grid (row=3, column=0, sticky="nsew", columnspan=2)

            self.url_list.config (yscrollcommand=scroll_vertical3.set, xscrollcommand=scroll_horizontal3.set)

            separador = ttk.Separator (self.frame2, orient="horizontal")
            separador.grid (row=4, column=0, pady=10, sticky=W+E, columnspan=2, padx=20)

            # ************** seccion de  información de la APP
            Label (self.frame2, text="Application", justify=CENTER, font=("Cambria 12 bold"), bg="#212121", fg="#FF0000").grid (row=5, column=0, pady=4, columnspan=2) # FF000: color rojo

            Button (self.frame2, text="About us", justify=CENTER, font=("Cambria 11"), bg="#212121", bd=0, activeforeground="blue", foreground="#1DE9B6", activebackground="#212121", command=lambda: self.messenger ()).grid (row=6, column=0, pady=4, columnspan=2)  #222222: color negro
            Button (self.frame2, text="About", justify=CENTER, font=("Cambria 11"), bg="#212121", bd=0, activeforeground="blue", activebackground="#212121", foreground="#1DE9B6", command=lambda: self.about ()).grid (row=7, column=0, pady=4, columnspan=2)
            Button (self.frame2, text="Contact me", justify=CENTER, font=("Cambria 11"), bg="#212121", bd=0, activeforeground="blue", activebackground="#212121", foreground="#1DE9B6", command=lambda: messagebox.showinfo (title="Contact me", message="whoamy0608@gmail.com")).grid (row=8, column=0, pady=4, columnspan=2)
            Button (self.frame2, text="License", justify=CENTER, font=("Cambria 11"), bg="#212121", bd=0, activeforeground="blue", activebackground="#212121", foreground="#1DE9B6", command= lambda: self.License ()).grid (row=9, column=0, pady=4, columnspan=2)

            separador=ttk.Separator (self.frame2, orient="horizontal")
            separador.grid (row=10, column=0, pady=4, sticky=W+E, columnspan=2, padx=20)
            Label (self.frame2, text="V.1.0.2022", font=("Cambria 11 bold"), bg="#212121", bd=0, foreground="purple").grid (row=11, column=0, pady=10, columnspan=2)

            # -------- sección en la que enlazamos el Frame1 y Frame2 en el Notebook -----------
            tab.add (self.frame1, text="Admin".center(44)) 
            tab.add (self.frame2, text="Settings".center(45)) 


            """
            PARTE IZQUIERDA DE LA PANTALLA  VISUALIZACIÓN DE TITULO, IMAGEN, BOTONES Y TABLA
            """
            self.container_1 = Frame (self.window, relief=RIDGE, bg="#3c3c3c", width=250, height=220)
            self.container_1.grid (row=0, column=2, columnspan=2, rowspan=4)

            # #1DE9B6 : TURQUESA CLARO
            Label (self.container_1, text="Data Security", font=("Cambria 34 bold"), fg="#1DE9B6", bg="#3c3c3c").grid (row=0, column=0, columnspan=2, pady=12, ipadx=10, sticky=W+E, ipady=20)

            ttk.Separator (self.container_1, orient=HORIZONTAL).grid (row=1, column=0, sticky=W+E, columnspan=2)
            ttk.Separator (self.container_1, orient=HORIZONTAL).grid (row=2, column=0, sticky=W+E, columnspan=2)

            # ********** Posicionamos la fecha y hora estaticas mediante el "place" ---------

            fech_main = Label (self.container_1, font=("Cambria 12 bold"), foreground="white", background="#3c3c3c")
            fech_main.place (x=1000, y=90)
            fech_main["text"] = self.dt.input_time ()

            hour_main = Label (self.container_1, font=("Cambria 12 bold"), foreground="white", background="#3c3c3c")
            hour_main.place (x=1090, y=90)
            hour_main["text"] = self.dt.input_hour ()

            #  ----------- Creamos el frame_img; contendrá una imagen de portada
            self.frame_img = Frame (self.container_1, bg="#3c3c3c")
            self.frame_img.grid (row=3, column=0, columnspan=2, pady=10,)

            self.img_port_encript = PhotoImage (file="App/media/img/img_portAPP_1080x200.png")
            Label (self.frame_img, image=self.img_port_encript).grid (row=0, column=0, sticky=W+E)

            # ----------- Creamos un Frame "access_button" ección botones de acceso rápido -----------------------
            self.access_button = Frame (self.container_1, width=400, relief=RIDGE, bg="#3c3c3c")
            self.access_button.grid (row=4, column=0, columnspan=2, pady=10, ipady=5)

            self.img_behind = PhotoImage (file="App/media/img/icon/Buttonreturn_25x25.png")
            self.img_add = PhotoImage (file="App/media/img/icon/Buttonsave_25x25.png")
            self.img_update = PhotoImage (file="App/media/img/icon/Buttonupdate_25x25.png")
            self.img_delete = PhotoImage (file="App/media/img/icon/Buttondelete_25x25.png")
            self.img_encrypted = PhotoImage (file="App/media/img/icon/Buttonencrypted_25x25.png")
            self.img_desencrypted = PhotoImage (file="App/media/img/icon/Buttondesencripted_25x25.png")

            Button (self.access_button, image=self.img_behind, bg="white", bd=0, relief=RAISED, command=lambda: self.validate.update_table (self.userr, self.table, self.encryptCode, 2, self.mail_list, self.account_list, self.url_list)).grid (row=0, column=0, padx=5)
            Button (self.access_button, image=self.img_add, text="Save", compound=LEFT, width=76, bg="white", bd=1, relief=RAISED, command=lambda: self.window_two ()).grid (row=0, column=1, padx=5)
            Button (self.access_button, image=self.img_update, text="Update", compound=LEFT, width=76, bg="white", bd=1, relief=RAISED, command=lambda: self.window_tree ()).grid (row=0, column=2, padx=5)
            Button (self.access_button, image=self.img_delete, text="Delete", compound=LEFT, width=76, bg="white", bd=1, relief=RAISED, command= lambda: Delete_dataDB (self.table, self.validate, self.mail_list, self.account_list, self.url_list, self.userr)).grid (row=0, column=3, padx=5)
            Button (self.access_button, image=self.img_encrypted, bg="white", bd=1, relief=RAISED, command=lambda: self.validate.update_table (self.userr, self.table, self.encryptCode, 1, self.mail_list, self.account_list, self.url_list)).grid (row=0, column=4, padx=5)
            Button (self.access_button, image=self.img_desencrypted, bg="white", bd=1, relief=RAISED, command=lambda: self.validate.update_table (self.userr, self.table, self.encryptCode, 2, self.mail_list, self.account_list, self.url_list)).grid (row=0, column=5, padx=5)
            Button (self.access_button, font=("Cambria 11 bold"), fg="red", bg="#3c3c3c", bd=0, relief=RAISED).grid (row=0, column=6, padx=2)

            # ------------- Creamos un contenedor "frame_search" para barra de busqeuda
            self.frame_search = Frame (self.access_button, bg="#3c3c3c")
            self.frame_search.grid (row=0, column=7, sticky=W+E, ipadx=10, ipady=5, padx=5)
            self.search = Entry (self.frame_search, font=("Cambria 12"), width=74, bg="#3c3c3c", relief=RAISED, bd=0, foreground="#64FFDA") # 64ffda: celeste
            self.search.grid (row=0, column=0, sticky=W+E, ipadx=10, ipady=6)
            self.bara = ttk.Separator (self.frame_search,orient=HORIZONTAL).grid (row=1, column=0, sticky=W+E)

            self.img_search = PhotoImage (file="App/media/img/icon/Buttonsearch_25x25.png")
            Button (self.frame_search, image=self.img_search, font=("Cambria 11 bold"), fg="red", bg="white", bd=0, command=lambda: Search_DB (self.search.get (), self.encryptCode, self.table, self.validate)).grid (row=0, column=1, padx=2)

            self.img_x = PhotoImage (file="App/media/img/icon/Buttonx_25x25.png")
            Button (self.frame_search, image=self.img_x, font=("Cambria 11 bold"), bg="white", fg="red", bd=0, command=lambda: self.search.delete (0, END)).place (x=662, y=3)


            # ------------ Creamos un contenedor de para la tabla ------------------
            self.frame_table = Frame (self.container_1, padx=5, width=90, bg="#3c3c3c")
            self.frame_table.grid (row=5, column=0, columnspan=2)

            # # style_table = ttk.Style ()
            # # style_table.theme_use ("default")
            # # style_table.configure ("self.table.TTreeviw", bg="red")

            self.table = ttk.Treeview (self.frame_table, columns=("#1", "#2", "#3", "#4", "#5", "#6"), height=15)
            self.table.grid (row=1, column=0, columnspan=2)

            self.table.heading ("#0", text="ID")
            self.table.heading ("#1", text="GMAIL")
            self.table.heading ("#2", text="SITE")
            self.table.heading ("#3", text="PASSWORD")
            self.table.heading ("#4", text="URL")
            self.table.heading ("#5", text="CREATED")
            self.table.heading ("#6", text="UPDATED")
            self.table.column ("#0", width=70)
            self.table.column ("#1", width=240)
            self.table.column ("#2", width=160)
            self.table.column ("#3", width=160)
            self.table.column ("#4", width=330)
            self.table.column ("#5", width=90)
            self.table.column ("#6", width=90)

            self.scroll_tabley = Scrollbar (self.frame_table, command=self.table.yview, orient="vertical")
            self.scroll_tabley.grid (row=1, column=2, sticky=N+S)                  
            self.table.config (yscrollcommand=self.scroll_tabley.set)

            self.scroll_tablex = Scrollbar (self.frame_table, command=self.table.yview, orient="horizontal")
            self.scroll_tablex.grid (row=2, column=0, columnspan=3, sticky="nsew")                  
            self.table.config (yscrollcommand=self.scroll_tablex.set)

            """
                METODO QUE ACTUALIZA LA TABLA AL MOMENTO DE INICIALIZAR EL PROGRAMA
            """ 
            self.validate.update_table (self.userr, self.table, emaill=self.mail_list, account=self.account_list, link=self.url_list)

            self.window.mainloop ()
    
    # grupo de funciones de messagebox ------------
    def messenger (self):
        messagebox.showinfo (title="Not available", message="Messagebox not available at the moment")

    def License (self):
        messagebox.showinfo (title="See license", message="The available license version is \n\tV-1.0.2022")
    
    def about (self):
        messagebox.showinfo (title="About", message="Secure Data\n\nVersion: 1.0.2002\nCopyright 2021 - 2005 Secure Data. All rights reserved\nContains security software licensed from RSA Data Security Inc.\nThis project is developed by ICQE")
    # ---------------------------------------------------
    
    """
        METODO QUE CONSTRUYE UNA VENTANA QUE PERMITE AGREGAR MAS ELMENTOS A LA BASE DE DATOS Y POR ENDE
        VISUALIZARLO EN LA TABLA
    """
    def window_two (self):
        self.window2 = Toplevel ()
        self.window2.title ("ADD NEW ELEMENT")
        self.window2.geometry ("488x470")
        self.window2.iconbitmap ("App/media/img/Logo/icon_Logo.ico")
        self.window2.resizable (False, False)
        self.window2.config (bg="white")

        self.Frame_AG = Frame (self.window2, background="white")
        self.Frame_AG.pack (ipadx=5, ipady=15, fill="both", expand=True, padx=10)

        Label (self.Frame_AG, text="Data", font= ("Cambria 15 bold"), background="white", width=38).grid (row=0, column=0, columnspan=3, pady=10, ipady=5, sticky=W+E)
        ttk.Separator (self.Frame_AG, orient=HORIZONTAL).grid (row=1, column=0, columnspan=3, sticky=W+E)
        ttk.Separator (self.Frame_AG, orient=HORIZONTAL).grid (row=2, column=0, columnspan=3, sticky=W+E)

        # ************* Creamos el contendor del formulario **************
        self.Frame_dataInput = Frame (self.Frame_AG, bg="white")
        self.Frame_dataInput.grid (row=3, column=0, sticky=W+E, padx=10, pady=30, columnspan=3)

        Label (self.Frame_dataInput, text="Gmail *", font=("Cambria 11 bold"), bd=0, background="white").grid (row=3, column=0, sticky=W+S, pady=10, rowspan=2)
        self.Gmail = ttk.Combobox(self.Frame_dataInput, values=())
        self.Gmail.grid (row=3, column=1, columnspan=3, sticky=W+E, ipady=4, padx=10)


        Label (self.Frame_dataInput, text="Site *", font=("Cambria 11 bold"), bd=0, background="white").grid (row=6, column=0, sticky=W+S, pady=10, rowspan=2)
        self.input_cuenta = Entry (self.Frame_dataInput, bd=0, width=43, font=("Cambria 11"))
        self.input_cuenta.grid (row=6, column=1, columnspan=3, sticky=W+E, ipady=4, padx=10)
        ttk.Separator (self.Frame_dataInput, orient=HORIZONTAL).grid (row=7, column=1, sticky=W+E, columnspan=3, padx=5)

        Label (self.Frame_dataInput, text="Password *", font=("Cambria 11 bold"), bd=0, background="white").grid (row=8, column=0, sticky=W+S, pady=10, rowspan=2)
        self.input_password = Entry (self.Frame_dataInput, bd=0, width=43, show="*", font=("Cambria 11"))
        self.input_password.grid (row=8, column=1, columnspan=3, sticky=W+E, ipady=4, padx=10)
        ttk.Separator (self.Frame_dataInput, orient=HORIZONTAL).grid (row=9, column=1, sticky=W+E, columnspan=3, padx=5)

        Label (self.Frame_dataInput, text="Link *", font=("Cambria 11 bold"), bd=0, background="white").grid (row=10, column=0, sticky=W+S, pady=10, rowspan=2)
        self.input_link = Entry (self.Frame_dataInput, bd=0, width=43, font=("Cambria 11"))
        self.input_link.grid (row=10, column=1, columnspan=3, sticky=W+E, ipady=4, padx=10)
        ttk.Separator (self.Frame_dataInput, orient=HORIZONTAL).grid (row=11, column=1, sticky=W+E, columnspan=3, padx=5)

        Label (self.Frame_dataInput, text="Date *", font=("Cambria 11 bold"), bd=0, background="white").grid (row=12, column=0, sticky=W+S, pady=10, rowspan=2)
        self.input_day = ttk.Combobox (self.Frame_dataInput, values=("01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"),  width=10)
        self.input_day.grid (row=12, column=1, sticky=E, ipady=3, pady=5)
        self.input_month = ttk.Combobox (self.Frame_dataInput, values=("01", "02", "03", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"), width=10)
        self.input_month.grid (row=12, column=2, ipady=3, pady=10)
        self.input_year = ttk.Combobox (self.Frame_dataInput, values=("1970", "1971", "1972", "1973", "1974", "1975", "1976", "1977", "1978", "1979", "1980","1981", "1982", "1983", "1984", "1985", "1986", "1987", "1988", "1989", "1990", "1991", "1992", "1993", "1994", "1995", "1996", "1997", "1998", "1999", "2000", "2001", "2002", "2003", "2004", "2005", "2005", "2006", "2007", "2008", "2009","2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024"),  width=10)
        self.input_year.grid (row=12, column=3, sticky=W, ipady=3, pady=10)

        self.messengerr = Label (self.Frame_AG, background="white", foreground="red", font=("Cambria 12"), justify=CENTER)
        self.messengerr.grid (row=4, column=0, columnspan=4, padx=10)


        Button (self.Frame_AG, text="Send", font=("Cambria 12 bold"), background="Blue", width=7, relief=RAISED, bd=3, activebackground="skyblue", activeforeground="orange", command=lambda: Insert_dataDB (self.__CaptureForm (), self.validate,self.encryptCode, self.Gmail, self.input_password, self.input_link, self.userr, self.table, self.window2)).grid (row=5, column=1, padx=10, ipady=3, ipadx=3, sticky=E)
        

        Button (self.Frame_AG, text="cancel", font=("Cambria 12 bold"), background="Green", width=7, relief=RAISED, bd=3, activebackground="skyblue", activeforeground="orange", command=lambda: self.window2.destroy ()).grid (row=5, column=2, padx=10, ipady=3, ipadx=5)

    # -------------- Método que captura los datos del formulario ------------------
    def __CaptureForm (self):
        capture_data = {
            "Email": self.Gmail.get (), 
            "accounts": self.input_cuenta.get (), 
            "password": self.input_password.get (), 
            "link": self.input_link.get (), 
            "created": "{}/{}/{}".format (self.input_day.get (), self.input_month.get (), self.input_year.get ()),
            "updated": self.dt.input_time ()
        }

        return capture_data
    
    """
         Método que contruye una ventana que permite actualizar los datos ya existentes
    """
    def window_tree (self):
        # ----------- Corroboramos que se seleccione un elemento de la tabla para poder actualizar sus elementos correspondientes de ID
        var = self.table.item (self.table.selection ())
        for k in ["image", "open", "tags"]:
            del var[k]
        if not self.validate.validate_data (var):
            messagebox.askretrycancel (title="Object not selection", message="You did not select an element \n from the table! Do you want to try again?")
            return 

        self.window3 = Toplevel ()
        self.window3.title ("UPDATE ELEMENT")
        self.window3.geometry ("488x470")
        self.window3.iconbitmap ("App/media/img/Logo/icon_Logo.ico")
        self.window3.resizable (False, False)
        self.window3.config (bg="white")

        self.Frame_form = Frame (self.window3, background="white")
        self.Frame_form.pack (ipadx=5, ipady=15, fill="both", expand=True, padx=10)

        Label (self.Frame_form, text="Datos", font= ("Cambria 15 bold"), background="white", width=38).grid (row=0, column=0, columnspan=3, pady=10, ipady=5, sticky=W+E)
        ttk.Separator (self.Frame_form, orient=HORIZONTAL).grid (row=1, column=0, columnspan=3, sticky=W+E)
        ttk.Separator (self.Frame_form, orient=HORIZONTAL).grid (row=2, column=0, columnspan=3, sticky=W+E)

        # contenedor de ingreso de datos
        self.Frame_dataSet = Frame (self.Frame_form, bg="white")
        self.Frame_dataSet.grid (row=3, column=0, sticky=W+E, padx=10, pady=30, columnspan=3)

        self.var_gamil = StringVar ()
        Label (self.Frame_dataSet, text="Gmail *", font=("Cambria 11 bold"), bd=0, background="white").grid (row=3, column=0, sticky=W+S, pady=10, rowspan=2)
        self.Gmail_set = Entry (self.Frame_dataSet, bd=0, width=43, font=("Cambria 11"), textvariable=self.var_gamil, state="readonly")
        self.Gmail_set.grid (row=3, column=1, columnspan=3, sticky=W+E, ipady=4, padx=10)

        ttk.Separator (self.Frame_dataSet, orient=HORIZONTAL).grid (row=4, column=1, sticky=W+E, columnspan=3, padx=5)

        self.var_site = StringVar ()
        Label (self.Frame_dataSet, text="Site *", font=("Cambria 11 bold"), bd=0, background="white").grid (row=6, column=0, sticky=W+S, pady=10, rowspan=2)
        self.site_set = Entry (self.Frame_dataSet, bd=0, width=43, font=("Cambria 11"), textvariable=self.var_site, state="readonly")
        self.site_set.grid (row=6, column=1, columnspan=3, sticky=W+E, ipady=4, padx=10)
        ttk.Separator (self.Frame_dataSet, orient=HORIZONTAL).grid (row=7, column=1, sticky=W+E, columnspan=3, padx=5)

        self.var_password = StringVar ()
        Label (self.Frame_dataSet, text="Password *", font=("Cambria 11 bold"), bd=0, background="white").grid (row=8, column=0, sticky=W+S, pady=10, rowspan=2)
        self.password_set = Entry (self.Frame_dataSet, bd=0, width=43, show="*", font=("Cambria 11"), textvariable=self.var_password)
        self.password_set.grid (row=8, column=1, columnspan=3, sticky=W+E, ipady=4, padx=10)
        ttk.Separator (self.Frame_dataSet, orient=HORIZONTAL).grid (row=9, column=1, sticky=W+E, columnspan=3, padx=5)

        self.var_link = StringVar ()
        Label (self.Frame_dataSet, text="Link *", font=("Cambria 11 bold"), bd=0, background="white").grid (row=10, column=0, sticky=W+S, pady=10, rowspan=2)
        self.link_set = Entry (self.Frame_dataSet, bd=0, width=43, font=("Cambria 11"), textvariable=self.var_link, state="readonly")
        self.link_set.grid (row=10, column=1, columnspan=3, sticky=W+E, ipady=4, padx=10)
        ttk.Separator (self.Frame_dataSet, orient=HORIZONTAL).grid (row=11, column=1, sticky=W+E, columnspan=3, padx=5)

        Label (self.Frame_dataSet, text="Date *", font=("Cambria 11 bold"), bd=0, background="white").grid (row=12, column=0, sticky=W+S, pady=10, rowspan=2)

        self.var_day = StringVar ()
        self.day_set = Entry (self.Frame_dataSet,  width=10, textvariable=self.var_day, state="readonly")
        self.day_set.grid (row=12, column=1, sticky=E, ipady=3, pady=5)
        self.var_month = StringVar ()
        self.month_set = Entry (self.Frame_dataSet, width=10, textvariable=self.var_month, state="readonly")
        self.month_set.grid (row=12, column=2, ipady=3, pady=10)
        self.var_year = StringVar ()
        self.year_set = Entry (self.Frame_dataSet,  width=10, textvariable=self.var_year, state="readonly")
        self.year_set.grid (row=12, column=3, sticky=W, ipady=3, pady=10)

        self.messenger_set = Label (self.Frame_form, background="white", foreground="red", font=("Cambria 12"), justify=CENTER)
        self.messenger_set.grid (row=4, column=0, columnspan=4, padx=10)

        Button (self.Frame_form, text="To update", font=("Cambria 12 bold"), background="Blue", width=7, relief=RAISED, bd=3, activebackground="skyblue", activeforeground="orange", command=lambda: Update_dataDB (self.table, self.window3, self.password_set.get (), self.dt, self.validate, self.encryptCode, emaill=self.mail_list, account=self.account_list, link=self.url_list, userr=self.userr)).grid (row=5, column=1, padx=10, ipady=3, ipadx=3, sticky=E)
        
        Button (self.Frame_form, text="Cancel", font=("Cambria 12 bold"), background="Green", width=7, relief=RAISED, bd=3, activebackground="skyblue", activeforeground="orange", command= lambda: self.window3.destroy ()).grid (row=5, column=2, padx=10, ipady=3, ipadx=5)

        # ---------- Método que permite enviar los datos a la ventana de actualización esto despues de haber selecionado un elemento en la tabla
        self.validate.set_window3 (self.table, self.var_gamil, self.var_site, self.var_password, self.var_link, self.var_day, self.var_month, self.var_year)

    

if __name__ == "__main__":
    App = Principal ()
