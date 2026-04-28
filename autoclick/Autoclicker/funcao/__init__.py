import pyautogui
import time
import keyboard
import json

def salvar_comandos(tecla):
    try:
        with open('usuarios.json', 'w') as arquivo:
            json.dump(tecla, arquivo)
    except FileNotFoundError:
        print('erro ao criar arquivo')

def carregar_comandos():
    try:
        with open('usuarios.json', 'r') as arquivo:
            return json.load(arquivo)
    except:
        return None



def autoclicker(tecla, intervalo):
    print(f"Aperte '{tecla}' para começar/parar o autoclicker")

    while True:
        if keyboard.is_pressed(tecla):
            print("Parando...")
            break

        pyautogui.click()
        time.sleep(intervalo)