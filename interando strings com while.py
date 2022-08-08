print("*-" * 50 + "*")
frase = input("Escreva uma frase: ")
action = ""


while not action.isdigit():
    print("*-" * 50 + "*")
    action = input("Oque você deseja fazer com a frase:\n\n"
                   "    [0] Construir a frase caractere por caractere\n"
                   "    [1] Apagar as vogais da frase\n"
                   "    [2] Inverter a frase\n"
                   "    [3] Apagar os espaços da frase\n"
                   "    [4] Mostrar o índice de cada caractere\n"
                   "    [5] Sair\n\n"
                   "Res.: ")

    
    if not action.isdigit():
        print("\nVALOR INCORRETO MEU QUERIDO, TENTE NOVAMENTE.")
        continue

else:
    print("*-" * 50 + "*")


action = int(action)
frase = frase.upper()
frase = frase.strip()
cont = 0
quantiaCaracteres = len(frase)


if action == 0:
    novaString = ""
    while cont < quantiaCaracteres:
        novaString = novaString + frase[cont]
        print(novaString)
        cont = cont + 1
    else:
        msg = "FRASE CONSTRUÍDA COM SUCESSO."
        print("\n" + msg.center(61))


elif action == 1:
    while cont < quantiaCaracteres:
        if frase[cont] == "A" or frase[cont] == "E" or frase[cont] == "I" or frase[cont] == "O" or frase[cont] == "U":
            cont = cont + 1
            continue
        print(frase[cont])
        cont = cont + 1
    else:
        msg = "VOGAIS EXCLUÍDAS COM SUCESSO"
        print("\n" + msg.center(61))


elif action == 2:
    cont = quantiaCaracteres - 1
    while cont >= 0:
        print(frase[cont])
        cont = cont - 1
    else:
        msg = "FRASE INVERTIDA COM SUCESSO."
        print("\n" + msg.center(61))


elif action == 3:
    while cont < quantiaCaracteres:
        if frase[cont] == " ":
            cont = cont + 1
            continue
        print(frase[cont])
        cont = cont + 1
    else:
        msg = "ESPAÇOS DA FRASE EXCLUÍDOS COM SUCESSO."
        print("\n" + msg.center(61))


elif action == 4:
    while cont < quantiaCaracteres:
        print(f"{frase[cont]}  -->  {cont:0>3d}")
        cont = cont + 1
    else:
        msg = "ÍNDICES INDICADOS COM SUCESSO"
        print("\n" + msg.center(61))


elif action == 5:
    msg = "EXECUÇÃO DO PROGRAMA FINALIZADA."
    print(msg.center(61))

elif action > 5:
    msg = "NÃO ENCONTREI ESTE VALOR, TENTE NOVAMENTE."
    print(msg.center(61))


else:
    msg = "ERROR, CONSULTE O SUPORTE\nCÓDIGO INSTABILIDADE: CRITICAL_PROCESS_DIED"
    print("\n" + msg.center(61))

print("*-" * 50 + "*")