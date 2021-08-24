import tkinter as tk
from functools import partial
import random

#Janela
janela2 = tk.Tk()
janela = tk.Tk()

def Clique(id):
	
	if e.get().upper() == "X" or e.get().upper() == "O":
		jog = e.get().upper()
		
	if jog == "X":
		pc = "O"
		
	elif jog == "O":
		pc = "X"
	
	id.botão["text"] = jog
	
	lista.remove(id)
	
	for c in range (2):
	
		if b1.botão["text"] != "":
			
			if b1.botão["text"] == b2.botão["text"] == b3.botão["text"]:
				l1["text"] = f"{b1.botão['text']} Wins!"
				return
		
			elif b1.botão["text"] == b4.botão["text"] == b7.botão["text"]:
				l1["text"] = f"{b1.botão['text']} Wins!"
				return
				
			elif b1.botão["text"] == b5.botão["text"] == b9.botão["text"]:
				l1["text"] = f"{b1.botão['text']} Wins!"
				return
		
		if b2.botão["text"] != "":
			
			if b2.botão["text"] == b5.botão["text"] == b8.botão["text"]:
				l1["text"] = f"{b2.botão['text']} Wins!"
				return
		
		if b3.botão["text"] != "":
			
			if b3.botão["text"] == b6.botão["text"] == b9.botão["text"]:
				l1["text"] = f"{b3.botão['text']} Wins!"
				return
			
			elif b3.botão["text"] == b5.botão["text"] == b7.botão["text"]:
				l1["text"] = f"{b3.botão['text']} Wins!"
				return
		
		if b4.botão["text"] != "":
			
			if b4.botão["text"] == b5.botão["text"] == b6.botão["text"]:
				l1["text"] = f"{b4.botão['text']} Wins!"
				return
		
		if b7.botão["text"] != "":
			
			if b7.botão["text"] == b8.botão["text"] == b9.botão["text"]:
				l1["text"] = f"{b7.botão['text']} Wins!"
				return
		
		if c == 0:
					
			if len(lista) != 0:
				esc = random.choice(lista)
		
				lista.remove(esc)
		
				esc.botão["text"] = pc
			
				esc.botão["command"] = ""

#Classe para os botões
class Botão:
	def __init__(self, col, lin):
		self.botão = tk.Button(janela, width = 2, height = 2, bg = "green", fg = "white", activebackground = "green", activeforeground = "white")
		self.botão.grid(column = col, row = lin)
		self.botão["command"] = partial (Clique, self)

#Caixa de Texto				
l = tk.Label(janela2, text = "X ou O")
l.grid(column =  0, row = 0)

l1 = tk.Label(janela2)
l1.grid(column = 0, row = 1)

#Input
e = tk.Entry(janela2, width = 5)
e.grid(column = 1, row = 0)

#Botões
b1 = Botão(0, 0)
b2 = Botão(1, 0)
b3 = Botão(2, 0)
b4 = Botão(0, 1)
b5 = Botão(1, 1)
b6 = Botão(2, 1)
b7 = Botão(0, 2)
b8 = Botão(1, 2)
b9 = Botão(2, 2)

lista = [b1, b2, b3, b4, b5, b6, b7, b8, b9]

janela.mainloop()