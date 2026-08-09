import socket
import sys
from datetime import datetime


if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Uso: python3 scanner.py <IP_ALVO>")
    sys.exit()

print("-" * 50)
print(f"Iniciando varredura no alvo: {target}")
print(f"Horário de início: {str(datetime.now())}")
print("-" * 50)

try:
   
    ports = [21, 22, 80, 443, 8080]
    
    for port in ports:
        # Criação do socket IPv4 (AF_INET) e TCP (SOCK_STREAM)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1) # Timeout de 1 segundo para não travar
        
        
        result = s.connect_ex((target, port))
        
        if result == 0:
            print(f"Porta {port}: ABERTA")
        
        s.close()

except KeyboardInterrupt:
    print("\nVarredura interrompida pelo usuário.")
    sys.exit()
except socket.error:
    print("\nErro de rede: O host não respondeu.")
    sys.exit()