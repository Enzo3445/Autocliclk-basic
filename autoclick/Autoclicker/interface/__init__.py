from autoclick import salvar_comandos, carregar_comandos, autoclicker

escolha = int(input("escolha 1- para editar o autocliclker, 2 para ativa"))
match escolha:
    case 1:
        tecla = str(input('click para ativar auto click'))
        letra = len(tecla)
        if letra >= 2:
            print('o autoclick so pode ser uma letra')
        elif letra is None:
            while True:
                print('não deixe vazio')
                escolha_click = str(input('click para ativar auto click'))
                if len(escolha_click) == 1:
                    print('agora prossiga')
                    break
        else:
            print("Edição do autoclicker construida")
            salvar_comandos(tecla)
    case 2:
       tecla = carregar_comandos()
       intervalo = float(input('intervalo para o autoclicker:'))
       autoclicker(tecla, intervalo)