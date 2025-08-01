import socket
import time

target = input("Enter target domain or IP: ")
ip = socket.gethostbyname(target)
print(f"\nScanning {target} [{ip}]...\n")

for port in range(1, 101):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((ip, port))
    if result == 0:
        print(f"Port {port:3} is OPEN")
    s.close()
    time.sleep(0.1)
