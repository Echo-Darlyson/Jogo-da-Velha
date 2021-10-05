import tkinter as tk
from functools import partial
from tkinter import messagebox
import random, os, sys

#Diretório atual
dir_name = os.path.dirname(__file__)

#Janela
janela = tk.Tk()
janela.title("Jogo da Velha")
janela.geometry("300x300")
janela.configure(background = "#29f705")

#Imagens
img_x = tk.PhotoImage(file = f"{os.path.join(dir_name, './X.png')}") # X
img_o = tk.PhotoImage(file = f"{os.path.join(dir_name, './O.png')}") # O
img_sword = tk.PhotoImage(file = f"{os.path.join(dir_name, './swords.png')}") # Espadas

win = 0 # Contagem de partida vencida | 0 = Empate | > 0 = Alguém venceu

count = 0 # Contagem das vezes jogadas pelo jogador


def Clique(id):
	global win, count, winner, jog, pc
	
	jog = imagem

	if jog == img_x:
		pc = img_o
		
	elif jog == img_o:
		pc = img_x

	id.botão["image"] = jog
	
	try:
		lista.remove(id)
	except:
		pass
	else:
		count += 1

		# Computador escolhe quadrados aleatórios para jogar
		if len(lista) != 0:
			esc = random.choice(lista)
			
			lista.remove(esc)
			
			esc.botão["image"] = pc
				
			esc.botão["command"] = ""

		# Verifica os quadrados semelhantes -----------------------------------------------------------------
		if b1.botão["image"] != "":
				
			if b1.botão["image"] == b2.botão["image"] == b3.botão["image"]:
				winner = b1.botão["image"]
				win += 1
			
			elif b1.botão["image"] == b4.botão["image"] == b7.botão["image"]:
				winner = b1.botão["image"]
				win += 1
					
			elif b1.botão["image"] == b5.botão["image"] == b9.botão["image"]:
				winner = b1.botão["image"]
				win += 1
			
		if b2.botão["image"] != "":
				
			if b2.botão["image"] == b5.botão["image"] == b8.botão["image"]:
				winner = b2.botão["image"]
				win += 1
			
		if b3.botão["image"] != "":
				
			if b3.botão["image"] == b6.botão["image"] == b9.botão["image"]:
				winner = b3.botão["image"]
				win += 1
				
			elif b3.botão["image"] == b5.botão["image"] == b7.botão["image"]:
				winner = b3.botão["image"]
				win += 1
			
		if b4.botão["image"] != "":
				
			if b4.botão["image"] == b5.botão["image"] == b6.botão["image"]:
				winner = b4.botão["image"]
				win += 1
			
		if b7.botão["image"] != "":
				
			if b7.botão["image"] == b8.botão["image"] == b9.botão["image"]:
				win += 1
				winner = b7.botão["image"]
		# -----------------------------------------------------------------------------------------

		w = ""
		# Verifica quem ganhou
		if win > 0:
			if winner == f"{jog}" or winner == f"{pc}" and win > 1:
				w = "Você"
			elif winner == f"{pc}" and win == 1:
				w = "Computador"
			messagebox.showinfo("Good Game", f"{w} Venceu!")
			sys.exit()
		
		#Verifica se empatou
		if count == 5 and win == 0:
			messagebox.showinfo("Good Game", "Empate!")
			sys.exit()


#Classe para os botões
class Botão:
	def __init__(self, x, y):
		self.botão = tk.Button(janela, background = "#29f705", border = 0, width = 98, height = 98, highlightthickness = 0)
		self.botão.place(x = x, y = y)
		self.botão["command"] = partial (Clique, self)
		self.botão.configure(activebackground = self.botão.cget("background"))


def Choose(img):
	global imagem, b1, b2, b3, b4, b5, b6, b7, b8, b9, x, o, lista
	imagem = img

	#Botões 1
	b1 = Botão(0, 0)
	b2 = Botão(100, 0)
	b3 = Botão(200, 0)
	b4 = Botão(0, 100)
	b5 = Botão(100, 100)
	b6 = Botão(200, 100)
	b7 = Botão(0, 200)
	b8 = Botão(100, 200)
	b9 = Botão(200, 200)

	#Separadores
	s1 = tk.Frame(janela, bg = "black", height = 300, width = 3, bd = 0)
	s1.place(x = 100, y = 0)

	s2 = tk.Frame(janela, bg = "black", height = 300, width = 3, bd = 0)
	s2.place(x = 200, y = 0)

	s3 = tk.Frame(janela, bg = "black", height = 3, width = 300, bd = 0)
	s3.place(x = 0, y = 100)

	s3 = tk.Frame(janela, bg = "black", height = 3, width = 300, bd = 0)
	s3.place(x = 0, y = 200)

	lista = [b1, b2, b3, b4, b5, b6, b7, b8, b9] # Lista com botões


#Frames
f1 = tk.Frame(janela, bg = "#29f705", height = 230, width = 300, bd = 0)
f1.place(x = 0, y = 70)

f6 = tk.Frame(janela, bg = "white", height = 70, width = 300, bd = 0)
f6.place(x = 0, y = 0)

f2 = tk.Frame(janela, bg = "Black", height = 230, width = 3, bd = 0)
f2.place(x = 150, y = 70)

f3 = tk.Frame(janela, bg = "Black", height = 4, width = 300, bd = 0)
f3.place(x = 0, y = 70)

f4 = tk.Frame(janela, bg = "Black", height = 70, width = 4, bd = 0)
f4.place(x = 0, y = 0)

f5 = tk.Frame(janela, bg = "Black", height = 70, width = 4, bd = 0)
f5.place(x = 296, y = 0)

f6 = tk.Frame(janela, bg = "Black", height = 4, width = 300, bd = 0)
f6.place(x = 0, y = 0)

f7 = tk.Frame(janela, bg = "Black", height = 4, width = 300, bd = 0)
f7.place(x = 0, y = 296)

f8 = tk.Frame(janela, bg = "Black", height = 230, width = 4, bd = 0)
f8.place(x = 0, y = 70)

f9 = tk.Frame(janela, bg = "Black", height = 230, width = 4, bd = 0)
f9.place(x = 296, y = 70)

#Botões 2
x = tk.Button(janela, image = img_x, command = partial(Choose, img_x), highlightthickness = 0, borderwidth = 0, background = "#29f705", activebackground = "#29f705")
x.place(x = 30, y = 140)
o = tk.Button(janela, image = img_o, command = partial(Choose, img_o), highlightthickness = 0, borderwidth = 0, background = "#29f705", activebackground = "#29f705")
o.place(x = 180, y = 140)

#Label
texto = tk.Label(janela, text = "Choose One", font = ("Helvetica", 27), fg = "Black", bg = "White")
texto.place(x = 47, y = 20)

#Swords
icon1 = tk.Label(janela, image = img_sword, border = 0, background = "White")
icon1.place(x = 8, y = 20)

icon2 = tk.Label(janela, image = img_sword, border = 0, background = "White")
icon2.place(x = 258, y = 20)

janela.mainloop()