import socket
import time 
from concurrent.futures import ThreadPoolExecutor

ip = "scanme.nmap.org"
inicio = time.perf_counter()
def scan_porta(porta):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    resultado = s.connect_ex((ip, porta))
    if resultado == 0:
        print(f"[OPEN] {porta}")
    s.close()
with ThreadPoolExecutor(max_workers= 100) as executor:
    executor.map(scan_porta, range(1, 1025))
fim = time.perf_counter()
tempo = fim - inicio 
print(f"tempo de operação: {tempo:.2f} segundos")
