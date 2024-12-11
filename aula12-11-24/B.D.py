#coding: utf-8

import sqlite3 as sq
import time as t

def CriarBD(): 
	conexao = sq.connect("Funcionarios.db")
	cursor= conexao.cursor()
	return conexao, cursor

def CriarTabela(): 
	tabela = ("""
	create table if not exists Funcionarios(
		id integer primary key, 
		nome text not null, 
		cargo text not null, 
		dataContratacao text not null);""")
		
	return tabela

def InserirDados(conexao, cursor, i): 
	nome = input('Digite um nome:')
	cargo = input('Digite um cargo:')
	data = input('Digite uma data no formato aaaa-mm-dd:')
	cursor.execute("INSERT INTO Funcionarios VALUES (?, ?, ?, ?)",(i, nome, cargo, data))
	conexao.commit()

def Parte1():
	conexao, cursor  = CriarConexãoBD()
	tabela = CriarTabela()
	cursor.execute(tabela) 
	conexao.commit()
	for i in range(3): 
		InserirDados(conexao, cursor, i)
		
def VerDados(conexao):
    cursor = conexao.curso()
    cursor.execute("SELECT * FROM Funciorarios")
    return cursor.fetchall()
def DeletarDado(conexao, cursor, id):
	cursor.execute("DELETE FROM Funcionarios WHERE id = ?", (id,) )
	conexao.commit()
def AlterarDado(conexao, cargo, id):
	cursor= conexao.cursor()
	cursor.execute("UPDATE Funcionarios Set cargo = ? WHERE id = ?",  (cargo, id))
	conexao.commit
def Parte2():
	conexao, cursor  = CriarConexãoBD()
	Dados = VerDados(conexao)
	print(Dados)
	t.sleep(2)
	InserirDados(conexao, cursor, 1)
	print(VerDados(conexao))
	t.sleep(2)
	#DeletarDado(conexao, cursor, 1)
	#print(VerDados(conexao))
	AlterarDado(conexao, 1, "CEO")
	print(VerDados(conexao))
	
if __name__=="__main__": 
    #Parte1()
    Parte2()  #Alterações no banco de dados.

