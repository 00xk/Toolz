#!/bin/bash

clear

echo -e '\033[1;31m
    .:::::::::.
  .:'''''''''':.
 .'  .      .  '.
:   .        .   :
:  :  -    -  :  :
:  :    ..    :  :
:  '.        .'  :
'.   '......'   .'
  '.          .'
    '........'
\033[1;33m
╔════════════════════════════════════╗
║     \033[1;36mWelcome to My Tool\033[1;33m         ║
║     \033[1;32mVersion 1.0\033[1;33m                 ║
╚════════════════════════════════════╝
\033[0m'

echo -e '\033[1;36m┌─────────────────────────────────┐'
echo -e '│         MAIN MENU              │'
echo -e '└─────────────────────────────────┘\033[0m'
echo ""
echo -e '\033[1;32m[1]\033[1;37m System Information\033[0m'
echo -e '\033[1;33m[2]\033[1;37m Network Tools\033[0m'
echo -e '\033[1;35m[3]\033[1;37m Exit\033[0m'
echo ""
echo -ne '\033[1;36mSelect an option [1-3]: \033[0m'
read choice

case $choice in
    1)
        echo -e '\033[1;32m\n[*] Gathering system information...\033[0m'
        uname -a
        ;;
    2)
        echo -e '\033[1;33m\n[*] Network tools menu...\033[0m'
        ifconfig
        ;;
    3)
        echo -e '\033[1;35m\n[*] Goodbye!\033[0m'
        exit 0
        ;;
    *)
        echo -e '\033[1;31m\n[!] Invalid option\033[0m'
        ;;
esac
