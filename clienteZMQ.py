import zmq
from constZMQ import *
import time

context = zmq.Context()
socket = context.socket(zmq.REQ)

print(f"[DEBUG] Cliente tentando conectar ao servidor tcp://{HOST}:{PORT}")
try:
    socket.connect(f"tcp://{HOST}:{PORT}")
    print("[DEBUG] Conexão estabelecida com sucesso.\n")
except Exception as e:
    print(f"[DEBUG][ERRO] Falha ao conectar: {e}")

def show_menu():
    print("=" * 50)
    print("Cliente ZeroMQ - Lista Remota")
    print("1 - Mostrar lista atual")
    print("2 - Adicionar elemento (append)")
    print("3 - Inserir elemento em posição específica")
    print("4 - Remover elemento")
    print("5 - Pesquisar elemento")
    print("6 - Ordenar lista (crescente)")
    print("7 - Ordenar lista (decrescente)")
    print("8 - Limpar lista")
    print("9 - Sair")
    print("=" * 50)

while True:
    show_menu()
    opcao = input("Escolha uma opção: ")
    print(f"[DEBUG] Opção escolhida: {opcao}")

    try:
        # Construção do comando
        if opcao == "1":
            cmd = "mostrar"
        elif opcao == "2":
            dado = input("Digite o elemento a adicionar: ")
            cmd = f"append {dado}"
        elif opcao == "3":
            index = input("Posição onde inserir: ")
            dado = input("Elemento a inserir: ")
            cmd = f"insert {index} {dado}"
        elif opcao == "4":
            dado = input("Elemento a remover: ")
            cmd = f"remover {dado}"
        elif opcao == "5":
            dado = input("Elemento a pesquisar: ")
            cmd = f"pesquisar {dado}"
        elif opcao == "6":
            cmd = "ordenar_cresc"
        elif opcao == "7":
            cmd = "ordenar_desc"
        elif opcao == "8":
            cmd = "limpar"
        elif opcao == "9":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")
            continue

        print(f"[DEBUG] Enviando comando ao servidor: {cmd}")
        socket.send_string(cmd)

        print("[DEBUG] Aguardando resposta do servidor...")
        resposta = socket.recv_string()
        print(f"[DEBUG] Resposta recebida do servidor: {resposta}\n")

    except Exception as e:
        print(f"[DEBUG][ERRO] Exceção no cliente: {e}")
        time.sleep(1)
