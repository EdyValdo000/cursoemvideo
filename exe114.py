import socket

def is_server_available(host, port, Timeout=5):
    try:
        with socket.create_connection((host, port), timeout=Timeout):
            return True
    except (socket.timeout, ConnectionRefusedError):
        return False
    except Exception:
        return False

# Testando com um servidor (exemplo: Google na porta 80)
host = "google.com"
port = 80

if is_server_available(host, port):
    print(f"\033[1;32mServidor {host}:{port} está disponível!\033[m")
else:
    print(f"\033[1;31mServidor {host}:{port} não está acessível.\033[m")
