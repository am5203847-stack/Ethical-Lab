import socket
print("=== ADEL Header Checker V1 ===")
host = input("اكتب الموقع (مثال: google.com) : ")

try:
    s = socket.socket()
    s.settimeout(3)
    s.connect((host, 80))
    # نبعت طلب HEAD بس عشان نجيب الهيدر
    s.send(f"HEAD / HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n".encode())
    data = s.recv(4096).decode(errors='ignore')
    print("\n--- النتيجة ---\n")
    print(data)
    s.close()
except Exception as e:
    print(f"\n[!] مش عارف أوصله: {e}")
    print("جرب تكتب google.com من غير https")
