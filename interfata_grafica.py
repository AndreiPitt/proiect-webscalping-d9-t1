import tkinter.ttk
from tkinter import *
from tkinter import messagebox
from customtkinter import *

from app import pagina1, pagina2, pagina3
from user import user
from web import web


def start():
    # Start app
    principal = Tk()
    principal.geometry("650x440")
    principal.title("Aplicatie")
    principal.configure(bg="#008080")
    icon = PhotoImage(file="icon.png")
    principal.iconphoto(True, icon)
    principal.resizable(height=False, width=False)

    # Login TopLevel
    login = Toplevel(principal)
    login.withdraw()
    login.geometry("320x320")
    login.title("Login")
    login.configure(bg="#008080")
    login.resizable(height=False, width=False)

    # Register TopLevel
    register = Toplevel(principal)
    register.withdraw()
    register.geometry("320x320")
    register.title("Register")
    register.configure(bg="#008080")
    register.resizable(height=False, width=False)

    # Frame uri
    startframe = CTkFrame(principal, fg_color="#008B8B")
    loginframe = CTkFrame(login, fg_color="#008080")
    registerframe = CTkFrame(register, fg_color="#008080")
    buttonframe = CTkFrame(principal, fg_color="#008080")
    searchframe = CTkFrame(principal, fg_color="#008080")
    # Treeview
    treeview = tkinter.ttk.Treeview(principal, height=15)
    # Coloane Treeview
    treeview["columns"] = ("Nume", "Pret")
    treeview.column("#0", width=20, minwidth=20, stretch=NO)
    treeview.column("Nume", width=370, anchor=W, minwidth=370)
    treeview.column("Pret", anchor=W, width=60, minwidth=60)

    # Handing Treeview
    treeview.heading("#0", text="ID", anchor=W)
    treeview.heading("Nume", text="Nume medicament", anchor=W)
    treeview.heading("Pret", text="Pret", anchor=W)

    # Functii:

    def comanda_pagina(pagina: object):
        """" Functia comanda_pagina primeste ca parametru un obiect de tip Web.Flagul paginii poate fi 1,
        2 sau 3. Se verifica daca cheia apartine dictionarului cu optiuni iar daca aceasta apartine se creaza o
        variabila "tip" care tine loc de metodele obiectului de tip Web (.drmax sau .napofarm sau .helpnet)
        """
        optiuni = {1: "listadrmax", 2: "listanapofarm", 3: "listahelpnet"}
        tip = optiuni.get(pagina.flag)
        if pagina.flag in optiuni:
            count = 0
            elemente = getattr(pagina, tip)
            for produs in elemente:
                treeview.insert(parent="", text=str(count), index="end", values=produs)
                count += 1

    def comanda_clear():
        """
        Functia goleste continutul treeview-ului.
        """
        treeview.delete(*treeview.get_children())

    def verificaLink():
        """
        Functia verifica daca linkurile sunt valide.
        a este parametru temporar care stocheaza caracterele introduse in entry pentru a fi procesate.
        t este un tuplu care contine url ul site ului respectiv si flag-ul: t[0] = url ; t[1] = flag
        In caz ca url ul este invalid se returneaza None
        """
        a = link.get()
        if a.startswith("https://www.drmax.ro/"):
            flag = 1
            t = (a, flag)
            link.delete(0, END)
            return t
        elif a.startswith("https://www.farmaciilenapofarm.ro/"):
            flag = 2
            t = (a, flag)
            link.delete(0, END)
            return t
        elif a.startswith("https://www.helpnet.ro/"):
            flag = 3
            t = (a, flag)
            link.delete(0, END)
            return t
        else:
            print("Nu ai introdus un link valid")
            link.delete(0, END)
            messagebox.showwarning(message="ERROR: Link invalid!")
            error = (a, -1)
            return error

    def creazaLink():
        """"
        Apeleaza functia verificaLink() si salveaza in variabila a tuplul returnat de functie.
        Se face verificarea elementului secundar din tuplu care indica ce tip de pagina este apoi se creaza pagina.
        Dupa verificare se returneaza obiectul creat.
        Functia creazaLink returneaza obiecte de tip Web sau None daca flagul nu corespunde.

        """
        a = verificaLink()
        if a[1] == 1:
            pagina = web(a[0])
            pagina.creazaPagina(a[1])
            return pagina
        elif a[1] == 2:
            pagina = web(a[0])
            pagina.creazaPagina(a[1])
            return pagina
        elif a[1] == 3:
            pagina = web(a[0])
            pagina.creazaPagina(a[1])
            return pagina
        else:
            return None

    def afiseazaLink():
        """"
        Se apeleaza functia creazaLink pentru a crea un obiect de tip Web
        """
        pagina = creazaLink()
        if pagina is not None:
            comanda_pagina(pagina)
        return pagina

    def salveazaPagina():
        with open("produse.csv", "a", encoding="UTF-8") as f:
            elemente = treeview.get_children()
            for element in elemente:
                produs = treeview.item(element, "values")
                f.write(f"{produs}\n")
            print("Produsele au fost adaugate in fisier.")

    def logheazaPersoana():
        user.loadPersons()
        utilizator = user.readFormFile()
        if user.checkPersonByName(username_entry.get()):
            if [username_entry.get(), password_entry.get()] in utilizator:
                login.withdraw()
                messagebox.showinfo(message="Te-ai logat cu succes")
                startframe.destroy()
                treeview.grid(row=0, column=1, padx=20, pady=20)
                buttonframe.grid(row=0, column=0)
                searchframe.grid(row=1, column=0, columnspan=5, sticky="ew")

            else:
                messagebox.showwarning(message="Datele pe care le-ai introdus sunt incorecte!")
                login.deiconify()
                username_entry.delete(0, END)
                password_entry.delete(0, END)

        else:
            messagebox.showwarning(message="Nu exista acest cont!Te rugam sa te inregistrezi.")
            login_buttonmain.destroy()
            login.destroy()

    def inregistreazaPersoana():
        user.loadPersons()
        if user.checkPersonByName(username2_entry.get()):
            username2_entry.delete(0, END)
            password2_entry.delete(0, END)
            messagebox.showwarning(message="Exista deja cont cu acest username!")
        else:
            cont_nou = user(username2_entry.get(), password2_entry.get())
            user.save(cont_nou)
            register.withdraw()
            messagebox.showinfo(message=f"Te-ai inregistrat cu succes! Bine ai venit {username2_entry.get()}")
            startframe.destroy()

    # Startframe (login/register)
    mesaj = CTkLabel(startframe, text="Welcome!", font=("arial", 40))
    login_buttonmain = CTkButton(startframe, text="Login", fg_color="#B22222", command=login.deiconify)
    register_buttonmain = CTkButton(startframe, text="Register", fg_color="#B22222", command=register.deiconify)
    mesaj.grid(row=1, column=0, pady=50)
    login_buttonmain.grid(row=2, column=0, pady=20)
    register_buttonmain.grid(row=3, column=0, pady=20)

    # Loginframe:
    label1 = CTkLabel(loginframe, text="Login", font=("arial", 40))
    username_label = CTkLabel(loginframe, text="Username", font=("arial", 18))
    username_entry = CTkEntry(loginframe, fg_color="#B22222")
    password_label = CTkLabel(loginframe, text="Password", font=("arial", 18))
    password_entry = CTkEntry(loginframe, show="*", fg_color="#B22222")
    login_button = CTkButton(loginframe, text="Login", fg_color="#B22222", command=logheazaPersoana)

    label1.grid(row="0", column="0", columnspan="2", pady="40")
    username_label.grid(row="1", column="0")
    username_entry.grid(row="1", column="1")
    password_label.grid(row="2", column="0")
    password_entry.grid(row="2", column="1")
    login_button.grid(row="3", column="0", columnspan="2", pady="30")

    # Registerframe:
    label2 = CTkLabel(registerframe, text="Register", font=("arial", 40))
    username2_label = CTkLabel(registerframe, text="Username", font=("arial", 18))
    username2_entry = CTkEntry(registerframe, fg_color="#B22222")
    password2_label = CTkLabel(registerframe, text="Password", font=("arial", 18))
    password2_entry = CTkEntry(registerframe, show="*", fg_color="#B22222")
    login_button2 = CTkButton(registerframe, text="Register", fg_color="#B22222", command=inregistreazaPersoana)

    label2.grid(row="0", column="0", columnspan="2", pady="40")
    username2_label.grid(row="1", column="0")
    username2_entry.grid(row="1", column="1")
    password2_label.grid(row="2", column="0")
    password2_entry.grid(row="2", column="1")
    login_button2.grid(row="3", column="0", columnspan="2", pady="30")

    # Butoaneframe

    clear_button = CTkButton(buttonframe, text="Clear", command=comanda_clear, fg_color="red")
    clear_button.grid(row=0, column=0, padx=10, pady=10)

    button1 = CTkButton(buttonframe, text="DrMax", command=lambda: comanda_pagina(pagina1), fg_color="red")
    button1.grid(row=1, column=0, padx=10, pady=10)

    button2 = CTkButton(buttonframe, text="Helpnet", command=lambda: comanda_pagina(pagina3), fg_color="red")
    button2.grid(row=2, column=0, padx=10, pady=10)

    button3 = CTkButton(buttonframe, text="Napofarm", command=lambda: comanda_pagina(pagina2), fg_color="red")
    button3.grid(row=3, column=0, padx=10, pady=10)

    button4 = CTkButton(buttonframe, text="Save", fg_color="red", command=salveazaPagina)
    button4.grid(row=4, column=0, padx=10, pady=10)

    # entryframe
    introducere = CTkLabel(searchframe, text="Introduceti link ul farmaciei: ")
    introducere.grid(row=0, column=0, padx=12, sticky="w")
    link = CTkEntry(searchframe, fg_color="#B22222")
    link.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="ew")
    searchframe.columnconfigure(0, weight=6)
    buttonsearch = CTkButton(searchframe, text="OK", fg_color="black", command=afiseazaLink)
    buttonsearch.grid(row=1, column=1, padx=(0, 10), pady=(0, 10), sticky="e")
    searchframe.columnconfigure(1, weight=1)

    startframe.pack(anchor="center", pady=50)
    loginframe.pack()
    registerframe.pack()
    principal.mainloop()
