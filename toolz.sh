#!/bin/bash

# Colors
RED='\033[1;31m'
GREEN='\033[1;32m'
YELLOW='\033[1;33m'
BLUE='\033[1;34m'
PURPLE='\033[1;35m'
CYAN='\033[1;36m'
WHITE='\033[1;37m'
RESET='\033[0m'
BOLD='\033[1m'

# Clear screen
clear

# Banner with skull
banner() {
    echo -e "${RED}
    ═══════════════════════════════════════════════════════════
                        
                    ${WHITE}.・゜゜・．．・゜゜・．${RED}
                ${WHITE}　　　　　  ／＼　　 　 ／＼${RED}
              ${WHITE}　 　　　  ／　　＼　 ／　　＼${RED}
            ${WHITE}　　　　　 ｜　　　 ●　　　　｜${RED}
          ${WHITE}　　　　　　｜　　　　　　　　 ｜${RED}
        ${WHITE}　　　　　　　＼　　╱▔▔▔╲　 ／${RED}
      ${WHITE}　　　　　　　　 ＼／　　　　＼／${RED}
    ${WHITE}　　　　　　　　　　　　　　　　　　${RED}
    
    ${CYAN}╔════════════════════════════════════════════════════════╗
    ║                                                        ║
    ║         ${YELLOW}████████╗ ██████╗  ██████╗ ██╗     ███████╗${CYAN}  ║
    ║         ${YELLOW}╚══██╔══╝██╔═══██╗██╔═══██╗██║     ╚══███╔╝${CYAN}  ║
    ║            ${YELLOW}██║   ██║   ██║██║   ██║██║       ███╔╝${CYAN}   ║
    ║            ${YELLOW}██║   ██║   ██║██║   ██║██║      ███╔╝${CYAN}    ║
    ║            ${YELLOW}██║   ╚██████╔╝╚██████╔╝███████╗███████╗${CYAN}  ║
    ║            ${YELLOW}╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝${CYAN}  ║
    ║                                                        ║
    ╚════════════════════════════════════════════════════════╝${RESET}
    
    ${PURPLE}┌────────────────────────────────────────────────────────┐
    │  ${WHITE}Version: ${GREEN}1.0.0${PURPLE}        │  ${WHITE}Author: ${GREEN}00xk${PURPLE}               │
    │  ${WHITE}GitHub: ${CYAN}github.com/00xk/Toolz${PURPLE}                     │
    └────────────────────────────────────────────────────────┘${RESET}
    
    ═══════════════════════════════════════════════════════════
    "
}

# Main menu
menu() {
    echo -e "${CYAN}
    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃                    ${WHITE}MAIN MENU${CYAN}                          ┃
    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛${RESET}
    "
    echo -e "    ${GREEN}[${WHITE}1${GREEN}]${YELLOW} ➤ ${WHITE}System Information${RESET}"
    echo -e "    ${GREEN}[${WHITE}2${GREEN}]${YELLOW} ➤ ${WHITE}Network Tools${RESET}"
    echo -e "    ${GREEN}[${WHITE}3${GREEN}]${YELLOW} ➤ ${WHITE}Update Tool${RESET}"
    echo -e "    ${GREEN}[${WHITE}4${GREEN}]${YELLOW} ➤ ${WHITE}About${RESET}"
    echo -e "    ${RED}[${WHITE}0${RED}]${YELLOW} ➤ ${WHITE}Exit${RESET}"
    echo ""
    echo -ne "    ${CYAN}┌─[${WHITE}Select Option${CYAN}]
    └──╼ ${GREEN}$ ${RESET}"
}

# System Information
system_info() {
    clear
    echo -e "${YELLOW}
    ╔══════════════════════════════════════════════════════╗
    ║           SYSTEM INFORMATION                         ║
    ╚══════════════════════════════════════════════════════╝${RESET}
    "
    echo -e "${CYAN}[+] Operating System:${RESET}"
    uname -a
    echo ""
    echo -e "${CYAN}[+] Hostname:${RESET}"
    hostname
    echo ""
    echo -e "${CYAN}[+] Current User:${RESET}"
    whoami
    echo ""
    echo -e "${CYAN}[+] Date & Time:${RESET}"
    date
    echo ""
    echo -e "${CYAN}[+] Uptime:${RESET}"
    uptime
    echo ""
    echo -e "${GREEN}[✓] Information gathered successfully!${RESET}"
    echo ""
    read -p "Press Enter to continue..."
}

# Network Tools
network_tools() {
    clear
    echo -e "${YELLOW}
    ╔══════════════════════════════════════════════════════╗
    ║              NETWORK TOOLS                           ║
    ╚══════════════════════════════════════════════════════╝${RESET}
    "
    echo -e "${CYAN}[+] Network Interfaces:${RESET}"
    ip addr show 2>/dev/null || ifconfig 2>/dev/null || echo "Network tools not available"
    echo ""
    echo -e "${CYAN}[+] Active Connections:${RESET}"
    netstat -tuln 2>/dev/null | head -20 || ss -tuln 2>/dev/null | head -20 || echo "Connection info not available"
    echo ""
    echo -e "${GREEN}[✓] Network information displayed!${RESET}"
    echo ""
    read -p "Press Enter to continue..."
}

# Update function
update_tool() {
    clear
    echo -e "${PURPLE}
    ╔══════════════════════════════════════════════════════╗
    ║              UPDATE TOOL                             ║
    ╚══════════════════════════════════════════════════════╝${RESET}
    "
    echo -e "${CYAN}[*] Checking for updates...${RESET}"
    echo ""
    
    # Check if git is installed
    if ! command -v git &> /dev/null; then
        echo -e "${RED}[✗] Git is not installed!${RESET}"
        echo -e "${YELLOW}[!] Please install git first:${RESET}"
        echo -e "${WHITE}    sudo apt install git -y${RESET}"
        echo ""
        read -p "Press Enter to continue..."
        return
    fi
    
    # Repository URL
    REPO_URL="https://github.com/00xk/Toolz"
    TOOL_DIR="$HOME/Toolz"
    
    echo -e "${CYAN}[+] Repository: ${WHITE}$REPO_URL${RESET}"
    echo ""
    
    # Check if directory exists
    if [ -d "$TOOL_DIR" ]; then
        echo -e "${YELLOW}[*] Tool directory found. Updating...${RESET}"
        cd "$TOOL_DIR"
        git pull origin main 2>/dev/null || git pull origin master 2>/dev/null
        
        if [ $? -eq 0 ]; then
            echo -e "${GREEN}[✓] Tool updated successfully!${RESET}"
        else
            echo -e "${RED}[✗] Update failed!${RESET}"
        fi
    else
        echo -e "${YELLOW}[*] Tool directory not found. Installing...${RESET}"
        cd "$HOME"
        git clone "$REPO_URL"
        
        if [ $? -eq 0 ]; then
            echo -e "${GREEN}[✓] Tool installed successfully!${RESET}"
            echo -e "${CYAN}[+] Location: ${WHITE}$TOOL_DIR${RESET}"
        else
            echo -e "${RED}[✗] Installation failed!${RESET}"
        fi
    fi
    
    echo ""
    read -p "Press Enter to continue..."
}

# About
about() {
    clear
    echo -e "${PURPLE}
    ╔══════════════════════════════════════════════════════╗
    ║                   ABOUT                              ║
    ╚══════════════════════════════════════════════════════╝${RESET}
    "
    echo -e "${CYAN}[+] Tool Name:${WHITE} Toolz${RESET}"
    echo -e "${CYAN}[+] Version:${WHITE} 1.0.0${RESET}"
    echo -e "${CYAN}[+] Author:${WHITE} 00xk${RESET}"
    echo -e "${CYAN}[+] GitHub:${WHITE} https://github.com/00xk/Toolz${RESET}"
    echo -e "${CYAN}[+] Description:${WHITE} A colorful multi-purpose system tool${RESET}"
    echo ""
    echo -e "${YELLOW}[!] For educational and authorized use only!${RESET}"
    echo ""
    read -p "Press Enter to continue..."
}

# Main loop
main() {
    while true; do
        clear
        banner
        menu
        read choice
        
        case $choice in
            1)
                system_info
                ;;
            2)
                network_tools
                ;;
            3)
                update_tool
                ;;
            4)
                about
                ;;
            0)
                clear
                echo -e "${PURPLE}
    ╔══════════════════════════════════════════════════════╗
    ║              Thank you for using Toolz!              ║
    ║                   Goodbye! 👋                        ║
    ╚══════════════════════════════════════════════════════╝${RESET}
                "
                exit 0
                ;;
            *)
                echo -e "${RED}
    [✗] Invalid option! Please select 0-4${RESET}"
                sleep 2
                ;;
        esac
    done
}

# Check if running as root (optional warning)
if [ "$EUID" -eq 0 ]; then 
    echo -e "${YELLOW}[!] Running as root. Please be careful!${RESET}"
    sleep 1
fi

# Run main function
main
