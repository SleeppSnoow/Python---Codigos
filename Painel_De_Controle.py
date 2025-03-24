# Painel de Controle

import os
import time
import speedtest


while True:
    # Interfacie Inicial
    print ("―――――――――――――――――――――――――――――――――――――――")
    print ("█▀█  █▀█ ▄▄  ▀ ▄▄▄ ▄▄  █  ▄▄█ ▄▄   █▀▀ ▄▄▄ ▄▄▄ █▄ ▄▄ ▄▄▄ █ ▄▄ ")
    print ("█▄▄  █▀▀ ▀▄█ █ █ █ ██▄ █  █▄█ ██▄  █▄▄ █▄█ █ █ █▄ █  █▄█ █ ██▄")
    print ("―――――――――――――――By. Sleepp――――――――――――――――――")

    # Lista de Opções
    print ("")
    print ("Lista de Opções")
    print ("")

    print ("1. Speed Test")
    print ("0. Exit")
    print ("")

    escolha = int(input("Digite a opção desejada: "))

    if escolha == 1: # Opção Speed Test | Teste de Velocidade de internet
        sim_nao = str(input("Essa opção faz um teste de velocidade na sua internet. \nDeseja executala? (S/N): "))

        if sim_nao == "S" or sim_nao == "s":
            os.system("cls")
            print ("")
            print ("―――――――――――――――――――――――――――――――――――――――")
            print ("█▀█  █▀▀ ▄▄▄ ▄▄  ▄▄  ▄▄█  ▀█▀ ▄▄   ▄▄ █▄")
            print ("█▄▄  ▄▄█ █▄█ ██▄ ██▄ █▄█   █  ██▄ ▄█  █▄")
            print ("         █                              ")
            print ("―――――――――――――――――――――――――――――――――――――――")

            st = speedtest.Speedtest()
            st.get_best_server()

            print ("Testando download...")
            download_speed = st.download() / 1_000_000
            print ("Velocidade de Download: {:.2f} Mbps" .format(download_speed))
            print ("")

            print ("Testando upload...")
            upload_speed = st.upload() / 1_000_000
            print ("Velocidade de Upload: {:.2f} Mbps" .format(upload_speed))
            print ("")

            ping = st.results.ping
            print ("Ping: {:.2f} ms" .format(ping))
            print ("")

            print ("―――――――――――――――――――――――――――――――――――――――")
            print ("")

            enter = input("Aperte enter para voltar ao menu...")
            os.system("cls")

        elif sim_nao == "N" or sim_nao == "n":
            input("Okk... voltando para o menu inicial. \nAperte enter para voltar ao menu...")
            os.system("cls")

    elif escolha == 0: # Opção Exit | Fechar programa
        sim_nao = str(input("Deseja realmente fechar o programa? (S/N): "))

        if sim_nao == "S" or sim_nao == "s":
            print ("Okk... Fechando programa.")
            break

        elif sim_nao == "N" or sim_nao == "n":
            input("Okk... Aperte enter para voltar ao menu...")
            os.system("cls")

    else:
        input("Opção indisponivel no momento. \nAperte enter para voltar ao menu...")
