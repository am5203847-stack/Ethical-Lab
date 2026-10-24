import socket, ssl
print("=== ADEL Header Checker V2 (HTTPS) ===")
host = input("الموقع: ")

try:
    context = ssl.create_default_context()
    sock = socket.socket()
    s = context.wrap_socket(sock, server_hostname=host)
    s.settimeout(4)
    s.connect((host, 443))
    s.send(f"HEAD / HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n".encode())
    data = s.recv(4096).decode(errors='ignore')
    print("\n--- HTTPS Header ---\n")
    print(data)
    print(f"\n[✓] الشهادة شغالة ومشفرة")
    s.close()
except Exception as e:
    print(f"Error: {e}")
