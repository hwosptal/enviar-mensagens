import pyautogui
import time
import os

def enviar(texto,duracao):
	pyautogui.click(648,701,duration=duracao) #input
	pyautogui.write(texto)
	pyautogui.press('enter')
	time.sleep(duracao)


os.system("cls")

print("Enviar Mensagens")
print("[ 1 ] - Iniciar")
print("[ 2 ] - Fechar")
opt = int(input(">>>> "))
 
if opt == 1:
	texto = input("Digite o texto: ")
	duracao = float(input("Velocidade: (Recomendado: 0.5 a 2): "))
	loop = input("LOOP ? Y/N: ")

	if loop != "Y" or loop != "y":
		n = int(input("Digite a quantidade de vezes: "))

		for i in range(n):
			enviar(texto, duracao)
	else:
		enviar(texto, duracao)
else:
	exit()