from tkinter import *
from tkinter import messagebox, ttk, Tk, Label, PhotoImage

def abrir_pratos_entrada():
    pratos_entrada = Toplevel()
    pratos_entrada.title("Pratos de Entrada")
    pratos_entrada.state("zoomed")
    pratos_entrada.configure(bg='lightgray')

def abrir_pratos_principais():
    pratos_principais = Toplevel()
    pratos_principais.title("Pratos Principais")
    pratos_principais.state("zoomed")
    pratos_principais.configure(bg='lightgray')

def abrir_bebidas_alcolicas():
    bebidas_alcolicas = Toplevel()
    bebidas_alcolicas.title("Bebidas Alcólicas")
    bebidas_alcolicas.state("zoomed")
    bebidas_alcolicas.configure(bg='lightgray')

def abrir_bebidas():
    bebidas = Toplevel()
    bebidas.title("Bebidas")
    bebidas.state("zoomed")
    bebidas.configure(bg='lightgray')

def abrir_sobremesas():
    sobremesas = Toplevel()
    sobremesas.title("Sobremesas")
    sobremesas.state("zoomed")
    sobremesas.configure(bg='lightgray')

def abrir_menu_do_chef():
    menu_do_chef = Toplevel()
    menu_do_chef.title("Menu do Chef")
    menu_do_chef.state("zoomed")
    menu_do_chef.configure(bg='lightgray')

def abrir_carrinho():
    carrinho = Toplevel()
    carrinho.title("Carrinho")
    carrinho.state("zoomed")
    carrinho.configure(bg='lightgray')

def confirmar_sair():
    resposta = messagebox.askyesno("Confirmar Saída", "Você tem certeza que deseja sair?")
    if resposta:
        root.destroy()

def inicial_tela(usuario):
    global root
    root = Tk()
    root.title("Tela Inicial")
    root.state("zoomed")
    root.configure(bg='lightgray')

    img = PhotoImage(file="Imagens_Restaurante\\Logo_Restaurante.png")
    Label(root, image=img).place(relx=0.5, rely=0.25, anchor="center")

    Label(root, text=("Bem Vindo ao Restaurante do seu Ederson!"), font=("Arial", 20, "bold"), bg='lightgray').place(relx=0.5, rely=0.45, anchor="center")
    Label(root, text=(f"Olá {usuario}"), font=("Arial", 20, "bold"), bg='lightgray').place(relx=0.5, rely=0.5, anchor="center")

    style = ttk.Style()
    style.configure('custom.TButton', font=('Arial', 10), padding=15, width=20)

    btn_pratos_entrada = ttk.Button(root, text="Pratos de Entrada", style='custom.TButton', command=abrir_pratos_entrada)
    btn_pratos_entrada.place(relx=0.4, rely=0.6, anchor="center")

    btn_pratos_principais = ttk.Button(root, text="Pratos Principais", style='custom.TButton', command=abrir_pratos_principais)
    btn_pratos_principais.place(relx=0.5, rely=0.6, anchor="center")

    btn_bebidas_alcolicas = ttk.Button(root, text="Bebidas Alcólicas", style='custom.TButton', command=abrir_bebidas_alcolicas)
    btn_bebidas_alcolicas.place(relx=0.6, rely=0.6, anchor="center")

    btn_bebidas = ttk.Button(root, text="Bebidas", style='custom.TButton', command=abrir_bebidas)
    btn_bebidas.place(relx=0.4, rely=0.7, anchor="center")

    btn_sobremesas = ttk.Button(root, text="Sobremesas", style='custom.TButton', command=abrir_sobremesas)
    btn_sobremesas.place(relx=0.5, rely=0.7, anchor="center")

    btn_menu_do_chef = ttk.Button(root, text="Menu do Chef", style='custom.TButton', command=abrir_menu_do_chef)
    btn_menu_do_chef.place(relx=0.6, rely=0.7, anchor="center")

    bnt_carrinho = ttk.Button(root, text="Carrinho", style='custom.TButton', command=abrir_carrinho)
    bnt_carrinho.place(relx=0.45, rely=0.8, anchor="center")

    bnt_sair = ttk.Button(root, text="Sair", style='custom.TButton', command=confirmar_sair)
    bnt_sair.place(relx=0.55, rely=0.8, anchor="center")

    root.mainloop()