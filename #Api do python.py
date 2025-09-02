#Api do python 
#Aprender Djanjo para fazer API 
import sqlite3
from flask import Flask, request, jsonify
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

#Criação do database

conn = sqlite3.connect('app_ruido_teste.db')


def create_table():
    conn = sqlite3.connect('app_ruido_teste.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dados_ruido (
            id_ruido INTEGER PRIMARY KEY AUTOINCREMENT,
            nivel_ruido REAL NOT NULL,
            data_hora TEXT NOT NULL
        );
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dados_maquina (
            id_maquina INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_maquina TEXT NOT NULL,
            modelo_maquina TEXT NOT NULL
        );
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dados_usuario(
            id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_usuario TEXT NOT NULL,
            email_usuario TEXT NOT NULL,
            senha_usuario TEXT NOT NULL,
            cargo_usuario TEXT NOT NULL
        );
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dados_relato(
            id_relato INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao_relato TEXT NOT NULL,
            data_hora_relato TEXT NOT NULL,
            id_usuario INTEGER,
            FOREIGN KEY (id_usuario) REFERENCES dados_usuario(id_usuario)
        );
    ''')
    print("Tabelas criadas com sucesso!")
    conn.commit()
    conn.close()
    

    
def inserir_ruido(nivel_ruido):
    if not nivel_ruido:
        messagebox.showwarning("Aviso", "Informe o nível de ruído!")
        return
    conn = sqlite3.connect('app_ruido_teste.db')
    cursor = conn.cursor()
    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO dados_ruido (nivel_ruido, data_hora) VALUES (?, ?)", (nivel_ruido, data_hora))
    conn.commit()
    conn.close()
    messagebox.showinfo("Sucesso", f"Nível de ruído {nivel_ruido} dB inserido com sucesso!")

def inserir_maquina(nome, modelo):
    if not nome or not modelo:
        messagebox.showwarning("Aviso", "Preencha todos os campos da máquina!")
        return
    conn = sqlite3.connect('app_ruido_teste.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO dados_maquina (nome_maquina, modelo_maquina) VALUES (?, ?)", (nome, modelo))
    conn.commit()
    conn.close()
    messagebox.showinfo("Sucesso", f"Máquina '{nome}' cadastrada com sucesso!")

def inserir_usuario(nome, email, senha, cargo):
    if not nome or not email or not senha or not cargo:
        messagebox.showwarning("Aviso", "Preencha todos os campos do usuário!")
        return
    conn = sqlite3.connect('app_ruido_teste.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO dados_usuario (nome_usuario, email_usuario, senha_usuario, cargo_usuario) VALUES (?, ?, ?, ?)",
                   (nome, email, senha, cargo))
    conn.commit()
    conn.close()
    messagebox.showinfo("Sucesso", f"Usuário '{nome}' cadastrado com sucesso!")

def inserir_relato(descricao, id_usuario):
    if not descricao or not id_usuario:
        messagebox.showwarning("Aviso", "Preencha todos os campos do relato!")
        return
    conn = sqlite3.connect('app_ruido_teste.db')
    cursor = conn.cursor()
    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO dados_relato (descricao_relato, data_hora_relato, id_usuario) VALUES (?, ?, ?)",
                   (descricao, data_hora, id_usuario))
    conn.commit()
    conn.close()
    messagebox.showinfo("Sucesso", f"Relato registrado com sucesso!")


def abrir_database():
    conn = sqlite3.connect('app_ruido_teste.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    info = "Tabelas no banco de dados:\n" + "\n".join([table[0] for table in tables])
    messagebox.showinfo("Database Info", info)
    conn.close()
    
#interface grafica 
root = tk.Tk()
root.configure(bg="gray")
root.title("Cadastro de Dados de Ruído")
root.geometry("1400x1200")

#Titulo 
tk.Label(root, text="Cadastro de Dados de Ruído", font=("Arial", 24)).pack(pady=20, anchor="center")
#Ruido
frame_ruido = tk.LabelFrame(root, text="Cadastrar Ruído", padx=10, pady=10)
frame_ruido.pack(padx=10, pady=10, fill="x")
tk.Label(frame_ruido, text="Nível de Ruído (dB):").pack()
entry_ruido = tk.Entry(frame_ruido)
entry_ruido.pack()
tk.Button(frame_ruido, text="Inserir Ruído", command=lambda: inserir_ruido(entry_ruido.get())).pack(pady=5)
#Maquina
frame_maquina = tk.LabelFrame(root, text="Cadastrar Máquina", padx=10, pady=10)
frame_maquina.pack(padx=10, pady=10, fill="x")
tk.Label(frame_maquina, text="Nome da Máquina:").pack()
entry_nome_maquina = tk.Entry(frame_maquina)
entry_nome_maquina.pack()
tk.Label(frame_maquina, text="Modelo da Máquina:").pack()
entry_modelo_maquina = tk.Entry(frame_maquina)
entry_modelo_maquina.pack()
tk.Button(frame_maquina, text="Inserir Máquina", command=lambda: inserir_maquina(entry_nome_maquina.get(), entry_modelo_maquina.get())).pack(pady=5)

#usuario
frame_usuario = tk.LabelFrame(root, text="Cadastrar Usuário", padx=10, pady=10)
frame_usuario.pack(padx=10, pady=10, fill="x")
tk.Label(frame_usuario, text="Nome:").pack()
entry_nome_usuario = tk.Entry(frame_usuario)
entry_nome_usuario.pack()
tk.Label(frame_usuario, text="Email:").pack()
entry_email_usuario = tk.Entry(frame_usuario)
entry_email_usuario.pack()
tk.Label(frame_usuario, text="Senha:").pack()
entry_senha_usuario = tk.Entry(frame_usuario, show="*")
entry_senha_usuario.pack()
tk.Label(frame_usuario, text="Cargo:").pack()
entry_cargo_usuario = tk.Entry(frame_usuario)
entry_cargo_usuario.pack()
tk.Button(frame_usuario, text="Inserir Usuário", command=lambda: inserir_usuario(entry_nome_usuario.get(), entry_email_usuario.get(), entry_senha_usuario.get(), entry_cargo_usuario.get())).pack(pady=5)
#Relato
frame_relato = tk.LabelFrame(root, text="Cadastrar Relato", padx=10, pady=10)
frame_relato.pack(padx=10, pady=10, fill="x")
tk.Label(frame_relato, text="Descrição:").pack()
entry_descricao_relato = tk.Entry(frame_relato)
entry_descricao_relato.pack()
tk.Label(frame_relato, text="ID Usuário:").pack()
entry_id_usuario = tk.Entry(frame_relato)
entry_id_usuario.pack()
tk.Button(frame_relato, text="Inserir Relato", command=lambda: inserir_relato(entry_descricao_relato.get(), entry_id_usuario.get())).pack(pady=5)

def abrir_database():
    conn = sqlite3.connect('app_ruido_teste.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    info = "Tabelas no banco de dados:\n" + "\n".join([table[0] for table in tables])
    messagebox.showinfo("Database Info", info)
    conn.close()
    
btn_abrir_db = tk.Button(root, text="Abrir Database", command=abrir_database)
btn_abrir_db.pack(pady=10, anchor="center", side="bottom")

def exibir_info():
    conn = sqlite3.connect('app_ruido_teste.db')
    cursor = conn.cursor()
    # Exibe os 5 últimos registros de cada tabela principal
    info = ""
    # Ruído
    cursor.execute("SELECT * FROM dados_ruido ORDER BY id_ruido DESC LIMIT 5")
    rows_ruido = cursor.fetchall()
    info += "Últimos níveis de ruído:\n"
    for row in rows_ruido:
        info += f"ID: {row[0]}, Nível: {row[1]} dB, Data/Hora: {row[2]}\n"
    info += "\n"
    # Máquina
    cursor.execute("SELECT * FROM dados_maquina ORDER BY id_maquina DESC LIMIT 5")
    rows_maquina = cursor.fetchall()
    info += "Últimas máquinas cadastradas:\n"
    for row in rows_maquina:
        info += f"ID: {row[0]}, Nome: {row[1]}, Modelo: {row[2]}\n"
    info += "\n"
    # Usuário
    cursor.execute("SELECT * FROM dados_usuario ORDER BY id_usuario DESC LIMIT 5")
    rows_usuario = cursor.fetchall()
    info += "Últimos usuários cadastrados:\n"
    for row in rows_usuario:
        info += f"ID: {row[0]}, Nome: {row[1]}, Email: {row[2]}, Cargo: {row[4]}\n"
    info += "\n"
    # Relato
    cursor.execute("SELECT * FROM dados_relato ORDER BY id_relato DESC LIMIT 5")
    rows_relato = cursor.fetchall()
    info += "Últimos relatos:\n"
    for row in rows_relato:
        info += f"ID: {row[0]}, Descrição: {row[1]}, Data/Hora: {row[2]}, ID Usuário: {row[3]}\n"
    conn.close()
    messagebox.showinfo("Informações sobre Ruído", info)


btn_exibir_info = tk.Button(root, text="Exibir Informações", command=exibir_info)
btn_exibir_info.pack(pady=10, anchor="center", side="bottom")




create_table()
root.mainloop()
conn.close()