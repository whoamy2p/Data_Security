#! /usr/bin/env python3

from tkinter import messagebox
import sqlite3


"""
    Función que reliza las consultas a la base da datos y devulve un objeto
"""

def request_db (query, parameter=()):
    with sqlite3.connect ("Data_App.db") as conection:
        cursor = conection.cursor ()
        try:
            result = cursor.execute (query, parameter)
        except sqlite3.DatabaseError as dbt:
            messagebox.showerror (title="Database error", message="""Failed to connect to database. 
            Error of %s"""%dbt)
            print ("fallo al conectar a la abse de datos", dbt)
        
        conection.commit ()

        return result


"""
    Método que permite ingresar datos encriptados a la base da datos tabla cuentas
"""

def Insert_dataDB (parameter, validator, encryptCode, emaill, account, link, userr, table=0, window2=0):
    if validator.validate_data  (parameter):
        try:
            query = "INSERT INTO Accounts VALUES (NULL, ?,?,?,?,?,?,?)"
            
            if messagebox.askokcancel (title="Insert element", message="Are you sure you want to save the account? \n %s"%emaill):
                list_data = encryptCode.Encrypt (parameter)
                list_data.append (userr)
                request_db (query, list_data)

                validator.update_table (userr, table, encryptCode, emaill=emaill, account=account, link=link)
                window2.destroy ()
        except sqlite3.OperationalError as ots:
            print ("Error de: ", ots)
    
    else:
        messagebox.showerror (title="Failed operation", message="Por favor rellene todos los campos\n o cancela la operación")
    

"""
    Método que elimina datos de la base de datos
"""

def Delete_dataDB (table, validator, email, account, link, userr):
    try:
        # se alamcena los datos seleccionados en la tabla
        data_select = table.item (table.selection ())

        if data_select['text'] == "":
            messagebox.showerror (title="Object error", message="You have not selected an element \n from the table ! Please select an element \n from the table")
            return
    except IndexError as it:
        print ("selecciona una items", it)
    
    query = "DELETE FROM Accounts WHERE ID=?"
    
    if messagebox.askokcancel (title="Continue operation", message="Are you sure you want to delete the account? '%s'"%data_select['values'][1]):
        request_db (query, (data_select['text'],))

        validator.update_table (userr, table, emaill=email, account=account, link=link)


"""
    Metodo que actuliza elementos de la base de datos
"""

def Update_dataDB (table, window, password, date, validate, encryptCode, emaill, account, link, userr):
    
    data_selections = table.item (table.selection ())
    data_update = {
        "password": password,
        "date": date.input_time ()
        }

    data_updateEncripted = encryptCode.Encrypt (data_update)
    query = "UPDATE Accounts SET PASSSWORD=?, UPDATED=? WHERE ID=?"
    try:
        if messagebox.askokcancel (title="Continue operation", message="Are you sure you want to update\nthe password field of the account? '%s'"%data_selections['values'][0]):
            request_db (query, (data_updateEncripted[0], data_updateEncripted[1], data_selections['text']))
    except IndexError as it:
        print ("selecciona un campo", it)
    

    validate.update_table (userr, table, encryptCode, emaill=emaill, account=account, link=link)
    
    window.destroy ()

"""
    Metodo que encargado de realizar busquedas en la base de datos , son datos que el usuario quiere visualizar en la tabla "funciona como un filtro"
"""

def Search_DB (search, encryptCode, table, validate):
    if search.isspace () or search == "":
        if  not validate.validate_email (search, search):
            messagebox.showerror (title="Objet Error", message="Please write the email correctly\n !%s¡"%search)
            return

    diccsearch = {"searchP": search}
    search_ = encryptCode.Encrypt (diccsearch)
    
    try:
        query = "SELECT * FROM Accounts WHERE EMAIL LIKE '%{}%'".format (search_[0])
        resultpp = request_db (query)
    except IndexError as it:
        print ("Error de: ", it)

    # ------------ limpiamos tabla -----------------
    data_table = table.get_children ()
    for element in data_table:
        table.delete (element)
    
    # ------------ Insertamos los valores de busqueda -----------------
    for data_tuple in resultpp:
        data_list = [data_tuple[i] for i in range (1,7)]
        row = encryptCode.Desencrypt (data_list)
        table.insert ("", 0, text=data_tuple[0], values=(row[0], row[1], row[2], row[3], row[4], row[5]))


#  ****** METODO ENCARGADO DE INGRESAR LOS USUARIOS REGISTRADOS A LA DDBB *******

def Insert_dataDB_users (parameter, validator, encryptCode, emaill, window):
    if validator.validate_data  (parameter):
        try:
            query = "INSERT INTO Auth_Users VALUES (NULL, ?,?,?,?,?,?,?,?)"
            
            if messagebox.askokcancel (title="Insert element", message="Are you sure you want to save the account? \n %s"%emaill):

                request_db (query, encryptCode.Encrypt (parameter))

                window.destroy ()
        except sqlite3.OperationalError as ots:
            print ("Error de: ", ots)
    
    else:
        messagebox.showerror (title="Field error", message="Please fill in all the fields or \ncancel the operation")

def Read_dataDB_Users (email):
    query = "SELECT ID FROM Auth_Users WHERE USERNAME=?"
    result = request_db (query, (email,))
    for k in result:
        return k

# ----------- INSERTANDO LOS CODIGOS DE VERIFICACIÓN A LA BASE DE DATOS ------------------


def Insert_codeDB (code, dt, id_user):
    query = "INSERT INTO Code_Verfication values(NULL, ?,?,?)"
    parameter_inf = [code, id_user, f"{dt.day}/{dt.month}/{dt.year}"]
    request_db (query, parameter_inf)



    
