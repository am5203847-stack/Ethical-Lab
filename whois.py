import socket
print("=== ADEL Domain Checker V1 ===")
domain = input("اكتب الدومين (مثال google.com): ").strip()

def whois_query(server, query):
    s = socket.socket()
    s.settimeout(5)
    s.connect((server, 43))
    s.send((query + "\r\n").encode())
    data = b""
    while True:
        chunk = s.recv(4096)
        if not chunk:
            break
        data += chunk
    s.close()
    return data.decode(errors='ignore')

try:
    print(f"\n[*] بفحص {domain} ...\n")
    # اول خطوة نعرف سيرفر الـ whois من iana
    result = whois_query("whois.iana.org", domain)
    print(result[:1500]) # اول جزء
    
    # لو .com نحاول نجيب تفاصيل اكتر
    if ".com" in domain:
        print("\n--- تفاصيل اضافية من Verisign ---\n")
        result2 = whois_query("whois.verisign-grs.com", domain)
        # نعرض بس السطور المهمة
        for line in result2.splitlines():
            if any(x in line for x in ["Creation Date", "Registrar", "Name Server", "Domain Name"]):
                print(line)
except Exception as e:
    print(f"[!] Error: {e}")
