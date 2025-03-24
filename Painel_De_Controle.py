# Painel de Controle

import os
import time
import speedtest

while True:
    print ("――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
    print ("█▀█  █▀█ ▄▄  ▀ ▄▄▄ ▄▄  █  ▄▄█ ▄▄   █▀▀ ▄▄▄ ▄▄▄ █▄ ▄▄ ▄▄▄ █ ▄▄ ")
    print ("█▄▄  █▀▀ ▀▄█ █ █ █ ██▄ █  █▄█ ██▄  █▄▄ █▄█ █ █ █▄ █  █▄█ █ ██▄")
    print ("―――――――――――――――――――――――――By. Sleepp―――――――――――――――――――――――――――")

    print ("")
    print ("Lista de Opções")
    print ("")

    print ("1. Speed Test")
    print ("0. Exit")

    print ("")

    escolha = int(input("Digite a opção desejada: "))
    
    if escolha == 1:
        sim_nao = input("Essa opção faz um teste completo de internet. Deseja executala? (S/N): ")

        if sim_nao == "S" or sim_nao == "s":
            os.system("cls")

        print ("")
        print ("――――――――――――――――――――――――――――――――――――――――")
        print ("█▀█  █▀▀ ▄▄▄ ▄▄  ▄▄  ▄▄█  ▀█▀ ▄▄   ▄▄ █▄")
        print ("█▄▄  ▄▄█ █▄█ ██▄ ██▄ █▄█   █  ██▄ ▄█  █▄")
        print ("         █                              ")
        print ("――――――――――――――――――――――――――――――――――――――――")

        st = speedtest.Speedtest()
        st.get_best_server()

        print ("Testando download...")
        download_speed = st.download() / 1_000_000
        print (f"Velocidade de Download: {download_speed:.2f} Mbps")
        print ("")

        print ("Testando upload...")
        upload_speed = st.upload() / 1_000_000
        print (f"Velocidade de Upload: {upload_speed:.2f} Mbps")
        print ("")

        ping = st.results.ping
        print (f"Ping: {ping:.2f} ms")
        print ("")

        print ("――――――――――――――――――――――――――――――――――――――――")

        enter = input("Aperte enter para continuar...")
        os.system("cls")

    elif escolha == 0:
        print ("Okk... Fechando programa.")
        break
    else:
        print ("Opção indisponivel no momento.")
        time.sleep(2)
        os.system("cls")