import socket, ssl
from datetime import datetime

def header_check(host):
    try:
        # HTTP
        s = socket.socket()
        s.settimeout(3)
        s.connect((host, 80))
        s.send(f"HEAD / HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n".encode())
        data = s.recv(2048).decode(errors='ignore')
        s.close()
        print("--- [1] HTTP Header ---")
        print(data)
    except:
        print("--- [1] HTTP Header ---\n[!] مقفول او مش شغال على 80")

    try:
        # HTTPS
        context = ssl.create_default_context()
        sock = socket.socket()
        sec = context.wrap_socket(sock, server_hostname=host)
        sec.settimeout(4)
        sec.connect((host, 443))
        sec.send(f"HEAD / HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n".encode())
        data = sec.recv(2048).decode(errors='ignore')
        print("\n--- [2] HTTPS Header ---")
        print(data)
        sec.close()
    except:
        print("\n--- [2] HTTPS Header ---\n[!] مقفول او مش شغال على 443")

def port_check():
    print("\n--- [3] فحص جهازك انت ---")
    for port in [21, 22, 80, 443, 8080]:
        s = socket.socket()
        s.settimeout(0.5)
        result = s.connect_ex(('127.0.0.1', port))
        state = "مفتوح" if result == 0 else "مقفول"
        print(f"Port {port}: {state}")
        s.close()

def whois_check(domain):
    try:
        print(f"\n--- [4] WHOIS لـ {domain} ---")
        s = socket.socket()
        s.settimeout(5)
        s.connect(("whois.verisign-grs.com", 43))
        s.send((domain + "\r\n").encode())
        data = b""
        while True:
            c = s.recv(4096)
            if not c: break
            data += c
        s.close()
        txt = data.decode(errors='ignore')
        for line in txt.splitlines():
            if any(k in line for k in ["Domain Name", "Creation Date", "Registrar:", "Name Server"]):
                print(line.strip())
    except Exception as e:
        print(f"[!] WHOIS Error: {e}")

# --- Main ---
print("==============================")
print("  ADEL RECON TOOL V1 - FINAL")
print(f"  {datetime.now()}")
print("==============================")
target = input("\nاكتب الموقع (مثال google.com): ").strip()
header_check(target)
port_check()
whois_check(target)
print("\n[✓] التقرير خلص - انت كده عملت Recon كامل!")
