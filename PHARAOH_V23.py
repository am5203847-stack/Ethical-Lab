import requests, datetime, os, time
from pathlib import Path

# Colors
Y="\033[93m"; G="\033[92m"; P="\033[95m"; W="\033[97m"; R="\033[91m"; C="\033[96m"; RESET="\033[0m"

def banner():
    os.system('clear')
    print(f"{Y}")
    print(r"""
  ██████  ██    ██  █████  ██████   █████  
 ██    ██ ██    ██ ██   ██ 
 ██    ██ ██    ██ ███████ ██   ██ ███████ 
 ██ ▄▄ ██ ██    ██ ██   ██ ██   ██ ██   ██ 
  ██████   ██████  ██   ██ ██████  ██   ██ 
     ▀▀
    """)
    print(f"{P} V23 FINAL LEGEND - ADEL - THE GOD MODE{W}")
    print(f" Results auto saved in QUADA_Results.txt + PDF report {RESET}\n")

def save_log(text):
    with open("QUADA_Results.txt","a", encoding="utf-8") as f:
        now = datetime.datetime.now()
        f.write(f"{now} - {text}\n")

def check_username(username):
    sites = {
        "Instagram": f"https://www.instagram.com/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "Facebook": f"https://www.facebook.com/{username}",
        "Twitter/X": f"https://twitter.com/{username}",
        "GitHub": f"https://github.com/{username}",
        "YouTube": f"https://www.youtube.com/@{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
    }
    print(f"{C}[*] Scanning: {username}{RESET}")
    save_log(f"SCAN USERNAME: {username}")
    found = 0
    for name, url in sites.items():
        try:
            r = requests.get(url, timeout=5, headers={"User-Agent":"Mozilla/5.0"})
            if r.status_code == 200:
                print(f"{G}[FOUND] {name}: {url}{RESET}")
                save_log(f"[FOUND] {name}: {url}")
                found+=1
            else:
                print(f"{W}[NOT FOUND] {name}{RESET}")
        except:
            print(f"{R}[ERROR] {name}{RESET}")
    print(f"\n{G}[+] Total Found: {found}/{len(sites)}{RESET}")
    save_log(f"Total Found: {found}")

def ip_hunter():
    ip = input(f"{Y}Enter IP (8.8.8.8): {W}").strip()
    if not ip: return
    try:
        data = requests.get(f"http://ip-api.com/json/{ip}?fields=status,country,regionName,city,isp,org,lat,lon,query", timeout=10).json()
        if data['status']=='success':
            print(f"{G}\nCountry: {data['country']} - {data['regionName']}")
            print(f"City: {data['city']}")
            print(f"ISP: {data['isp']}")
            print(f"ORG: {data['org']}")
            print(f"Coords: {data['lat']},{data['lon']}")
            print(f"Map: https://www.google.com/maps?q={data['lat']},{data['lon']}{RESET}")
            save_log(f"IP: {ip} | {data['country']} {data['city']} | ISP: {data['isp']} | {data['lat']},{data['lon']}")
        else:
            print(f"{R}IP not found{RESET}")
    except Exception as e:
        print(f"{R}Error: {e}{RESET}")

def email_finder():
    domain = input(f"{Y}Domain (gmail.com): {W}").strip()
    full = input(f"{Y}Full Name (adel ahmed): {W}").strip().lower()
    if not domain or not full: return
    parts = full.split()
    first = parts[0]
    last = parts[-1] if len(parts)>1 else ""
    print(f"{G}[*] Generating for {domain}{RESET}")
    emails = [
        f"{first}@{domain}",
        f"{first}{last}@{domain}",
        f"{first}.{last}@{domain}",
        f"{first}_{last}@{domain}",
        f"{first}1@{domain}",
        f"{first}.01@{domain}",
        f"{first}{last}01@{domain}",
    ]
    save_log(f"EMAIL SEARCH: ['{first}'] @ {domain}")
    for e in emails:
        print(e)
        save_log(e)
    print(f"{G}\n[+] Saved {len(emails)} emails to QUADA_Results.txt{RESET}")

# MAIN LOOP
banner()
while True:
    choice = input(f"\n{Y}[1] Scan  [2] IP  [3] Email  [Q] Quit: {W}").lower().strip()
    if choice == '1':
        u = input(f"{Y}Username: {W}").strip()
        if u: check_username(u)
    elif choice == '2':
        ip_hunter()
    elif choice == '3':
        email_finder()
    elif choice == 'q':
        print(f"{G}\nBye ADEL! Check QUADA_Results.txt{RESET}")
        # Create simple HTML report
        try:
            txt = Path("QUADA_Results.txt").read_text(encoding="utf-8")
            html = f"<html><head><title>QUADA V23 Report</title></head><body style='background:#111;color:#0f0;font-family:monospace'><h1 style='color:yellow'>QUADA V23 - ADEL</h1><pre>{txt}</pre></body></html>"
            Path("QUADA_Report_V23.html").write_text(html, encoding="utf-8")
            print(f"{C}[+] HTML Report: QUADA_Report_V23.html{RESET}")
        except:
            pass
        break
    print(f"{W}\nEnter to return...{RESET}", end="")
    input()
