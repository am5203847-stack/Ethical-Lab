#!/bin/bash
while true
do
clear
bash ~/banner.sh
echo -n " PHARAOH@choose > "
read choice

# OSINT V2
if [ "$choice" = "1" ]; then
  echo ""
  echo "[+] ADVANCED OSINT"
  echo -n "Enter Username: "
  read user
  echo ""
  echo "[*] Hunting $user in 15 platforms..."
  echo "-----------------------------------"
  for site in instagram.com/$user tiktok.com/@$user github.com/$user facebook.com/$user twitter.com/$user youtube.com/@$user reddit.com/user/$user t.me/$user pinterest.com/$user linkedin.com/in/$user twitch.tv/$user soundcloud.com/$user medium.com/@$user vk.com/$user snapchat.com/add/$user; do
    echo -n "[?] $site -> "
    code=$(curl -s -o /dev/null -w "%{http_code}" https://$site -L --max-time 5)
    if [ "$code" = "200" ]; then
      echo "FOUND ✓"
    else
      echo "Not Found"
    fi
  done
  echo "-----------------------------------"
  read -p "Press Enter..."

# SCAN V2
elif [ "$choice" = "2" ]; then
  echo ""
  echo -n "Enter IP/Domain: "
  read ip
  echo ""
  echo "[*] Fast Nmap Scan..."
  nmap -F $ip
  echo ""
  echo "[*] Ping & DNS..."
  ping -c 2 $ip
  read -p "Press Enter..."

# TOOLS V2
elif [ "$choice" = "3" ]; then
  echo ""
  echo "TOOLS V2:"
  echo "[a] My IP & Location"
  echo "[b] Update System"
  echo "[c] Install All Tools (nmap, curl, whois)"
  echo -n "Choose: "
  read t
  if [ "$t" = "a" ]; then curl ipinfo.io; echo ""; fi
  if [ "$t" = "b" ]; then pkg update -y && pkg upgrade -y; fi
  if [ "$t" = "c" ]; then pkg install nmap curl whois -y; fi
  read -p "Press Enter..."

elif [ "$choice" = "4" ]; then
  exit
fi
done
