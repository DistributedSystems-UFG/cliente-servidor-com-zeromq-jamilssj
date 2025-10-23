import zmq
import time

HOST = "0.0.0.0"
PORT = 1234

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind(f"tcp://{HOST}:{PORT}")

lista = []

print(f"[DEBUG] Servidor ZeroMQ iniciado em {HOST}:{PORT}")
print("[DEBUG] Aguardando conexões e mensagens...\n")

while True:
    try:
        # Recebe mensagem do cliente
        print("[DEBUG] Esperando mensagem do cliente...")
        msg = socket.recv_string()
        print(f"[DEBUG] Mensagem recebida: {msg}")

        partes = msg.split()
        comando = partes[0]
        resposta = ""

        # Processamento dos comandos
        if comando == "mostrar":
            resposta = str(lista)
        elif comando == "append":
            val = partes[1]
            lista.append(val)
            resposta = f"Elemento '{val}' adicionado."
        elif comando == "insert":
            pos = int(partes[1])
            val = partes[2]
            if pos < 0 or pos > len(lista):
                resposta = f"Posição inválida: {pos}"
            else:
                lista.insert(pos, val)
                resposta = f"Elemento '{val}' inserido na posição {pos}."
        elif comando == "remover":
            val = partes[1]
            if val in lista:
                lista.remove(val)
                resposta = f"Elemento '{val}' removido."
            else:
                resposta = f"Elemento '{val}' não encontrado."
        elif comando == "pesquisar":
            val = partes[1]
            resposta = "Encontrado" if val in lista else "Não encontrado"
        elif comando == "ordenar_cresc":
            lista.sort()
            resposta = "Lista ordenada crescentemente."
        elif comando == "ordenar_desc":
            lista.sort(reverse=True)
            resposta = "Lista ordenada decrescentemente."
        elif comando == "limpar":
            lista.clear()
            resposta = "Lista limpa."
        else:
            resposta = "Comando inválido."

        print(f"[DEBUG] Enviando resposta ao cliente: {resposta}")
        socket.send_string(resposta)
        print("[DEBUG] Resposta enviada com sucesso.\n")

    except Exception as e:
        print(f"[DEBUG][ERRO] Exceção no servidor: {e}")
        time.sleep(1)
