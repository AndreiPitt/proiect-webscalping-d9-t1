import tkinter.ttk
from tkinter import *
from tkinter import messagebox
from customtkinter import *

from user import user
from web import web

pagina1 = web("https://www.drmax.ro/medicamente-fara-reteta/vitamine-si-minerale")
pagina1.creazaPagina(flag=1)
# pagina1.afiseazaProduse(flag=1)
# print()
pagina2 = web("https://www.farmaciilenapofarm.ro/minerale-vitamine")
pagina2.creazaPagina(flag=2)
# pagina2.afiseazaProduse(flag=2)
# print()
pagina3 = web("https://www.helpnet.ro/uz-general")
pagina3.creazaPagina(flag=3)
# pagina3.afiseazaProduse(flag = 3)

# Main app
principal = Tk()
principal.geometry("520x520")
principal.title("Aplicatie")
principal.configure(bg="#008080")
icon = PhotoImage(file="icon.png")
principal.iconphoto(True, icon)

# Treeview
treeview = tkinter.ttk.Treeview(principal)

# Coloane Treeview
treeview["columns"] = ("Nume", "Pret")
treeview.column("#0", width=20,minwidth=20,stretch=NO)
treeview.column("Nume", width=370, anchor=W, minwidth=370)
treeview.column("Pret", anchor=W, width=60, minwidth=60)

# Handing Treeview
treeview.heading("#0", text="ID", anchor=W)
treeview.heading("Nume", text="Nume medicament", anchor=W)
treeview.heading("Pret", text="Pret", anchor=W)

# Add Date
id = 0
drmax = pagina1.listadrmax
# for produs in drmax:
#     treeview.insert(parent="", text=str(id), index="end", values=produs)
#     id += 1

napofarm = pagina2.listanapofarm
# for produs in napofarm:
#     treeview.insert(parent="", text=str(id), index="end", values=produs)
#     id += 1

helpnet = pagina3.listahelpnet
for produs in helpnet:
    treeview.insert(parent="", text=str(id), index="end", values=produs)
    id += 1
# Login TopLevel
login = Toplevel(principal)
login.withdraw()
login.geometry("320x320")
login.title("Login")
login.configure(bg="#008080")

# Register TopLevel
register = Toplevel(principal)
register.withdraw()
register.geometry("320x320")
register.title("Register")
register.configure(bg="#008080")

mainframe = CTkFrame(principal, fg_color="#008080")
loginframe = CTkFrame(login, fg_color="#008080")
registerframe = CTkFrame(register, fg_color="#008080")

# Functii:
def logheazaPersoana():
    user.loadPersons()
    utilizator = user.readFormFile()
    if user.checkPersonByName(username_entry.get()):
        if [username_entry.get(), password_entry.get()] in utilizator:
            login.withdraw()
            messagebox.showinfo(message="Te-ai logat cu succes")
            mainframe.destroy()
            treeview.pack()
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
        mainframe.destroy()


# Mainframe (login/register)
mesaj = CTkLabel(mainframe, text="Welcome!", font=("arial", 40))
login_buttonmain = CTkButton(mainframe, text="Login", fg_color="#B22222", command=login.deiconify)
register_buttonmain = CTkButton(mainframe, text="Register", fg_color="#B22222", command=register.deiconify)
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

mainframe.pack()
loginframe.pack()
registerframe.pack()
principal.mainloop()
