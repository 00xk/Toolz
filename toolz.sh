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
    echo -e "${RED}"
    echo "    ================================================================"
    echo ""
    echo -e "                    ${WHITE}.・゜゜・．．・゜゜・．${RED}"
    echo -e "                ${WHITE}　　　　　  ／＼　　 　 ／＼${RED}"
    echo -e "              ${WHITE}　 　　　  ／　　＼　 ／　　＼${RED}"
    echo -e "            ${WHITE}　　　　　 ｜　　　 ●　　　　｜${RED}"
    echo -e "          ${WHITE}　　　　　　｜　　　　　　　　 ｜${RED}"
    echo -e "        ${WHITE}　　　　　　　＼　　╱▔▔▔╲　 ／${RED}"
    echo -e "      ${WHITE}　　　　　　　　 ＼／　　　　＼／${RED}"
    echo -e "    ${WHITE}　　　　　　　　　　　　　　　　　　${RED}"
    echo ""
    echo -e "${CYAN}    +========================================================+"
    echo -e "    |                                                        |"
    echo -e "    |       ${YELLOW}████████╗ ██████╗  ██████╗ ██╗     ███████╗${CYAN}  |"
    echo -e "    |       ${YELLOW}╚══██╔══╝██╔═══██╗██╔═══██╗██║     ╚══███╔╝${CYAN}  |"
    echo -e "    |          ${YELLOW}██║   ██║   ██║██║   ██║██║       ███╔╝${CYAN}   |"
    echo -e "    |          ${YELLOW}██║   ██║   ██║██║   ██║██║      ███╔╝${CYAN}    |"
    echo -e "    |          ${YELLOW}██║   ╚██████╔╝╚██████╔╝███████╗███████╗${CYAN}  |"
    echo -e "    |          ${YELLOW}╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝${CYAN}  |"
    echo -e "    |                                                        |"
    echo -e "    +========================================================+${RESET}"
    echo ""
    echo -e "${PURPLE}    +------------------------------------------------------+"
    echo -e "    |  ${WHITE}Version: ${GREEN}1.0.0${PURPLE}      |  ${WHITE}Author: ${GREEN}00xk${PURPLE}                 |"
    echo -e "    |  ${WHITE}GitHub: ${CYAN}github.com/00xk/Toolz${PURPLE}                   |"
    echo -e "    +------------------------------------------------------+${RESET}"
    echo ""
    echo "    ================================================================"
}

# Main menu
menu() {
    echo ""
    echo -e "${CYAN}    +======================================================+"
    echo -e "    |                  ${WHITE}MAIN MENU${CYAN}                        |"
    echo -e "    +======================================================+${RESET}"
    echo ""
    echo -e "    ${GREEN}[${WHITE}1${GREEN}]${YELLOW} ➤  ${WHITE}System Information${RESET}"
    echo -e "    ${GREEN}[${WHITE}2${GREEN}]${YELLOW} ➤  ${WHITE}Network Tools${RESET}"
    echo -e "    ${GREEN}[${WHITE}3${GREEN}]${YELLOW} ➤  ${WHITE}Update Tool${RESET}"
    echo -e "    ${GREEN}[${WHITE}4${GREEN}]${YELLOW} ➤  ${WHITE}About${RESET}"
    echo -e "    ${RED}[${WHITE}0${RED}]${YELLOW} ➤  ${WHITE}Exit${RESET}"
    echo ""
    echo -ne "    ${CYAN}+--[${WHITE}Select Option${CYAN}]"
    echo -ne "\n    ${CYAN}└──>  ${GREEN}${RESET}"
}

# System Information
system_info() {
    clear
    echo ""
    echo -e "${YELLOW}    +====================================================+"
    echo -e "    |         SYSTEM INFORMATION                         |"
    echo -e "    +====================================================+${RESET}"
    echo ""
    echo -e "${CYAN}    [+] Operating System:${RESET}"
    echo "        $(uname -a)"
    echo ""
    echo -e "${CYAN}    [+] Hostname:${RESET}"
    echo "        $(hostname)"
    echo ""
    echo -e "${CYAN}    [+] Current User:${RESET}"
    echo "        $(whoami)"
    echo ""
    echo -e "${CYAN}    [+] Date & Time:${RESET}"
    echo "        $(date)"
    echo ""
    echo -e "${CYAN}    [+] Uptime:${RESET}"
    echo "        $(uptime -p 2>/dev/null || uptime)"
    echo ""
    echo -e "${CYAN}    [+] Disk Usage:${RESET}"
    df -h / 2>/dev/null | tail -n 1 | awk '{print "        "$1" - Total: "$2" | Used: "$3" | Available: "$4" | Use%: "$5}'
    echo ""
    echo -e "${CYAN}    [+] Memory Usage:${RESET}"
    free -h 2>/dev/null | grep Mem | awk '{print "        Total: "$2" | Used: "$3" | Free: "$4}' || echo "        Memory info not available"
    echo ""
    echo -e "${GREEN}    [✓] Information gathered successfully!${RESET}"
    echo ""
    echo -ne "${PURPLE}    Press Enter to continue...${RESET}"
    read
}

# Network Tools
network_tools() {
    clear
    echo ""
    echo -e "${YELLOW}    +====================================================+"
    echo -e "    |            NETWORK TOOLS                           |"
    echo -e "    +====================================================+${RESET}"
    echo ""
    echo -e "${CYAN}    [+] Network Interfaces:${RESET}"
    echo ""
    if command -v ip &> /dev/null; then
        ip addr show | grep -E "^[0-9]|inet " | sed 's/^/        /'
    elif command -v ifconfig &> /dev/null; then
        ifconfig | grep -E "^[a-z]|inet " | sed 's/^/        /'
    else
        echo "        Network tools not available"
    fi
    echo ""
    echo -e "${CYAN}    [+] Default Gateway:${RESET}"
    if command -v ip &> /dev/null; then
        ip route | grep default | sed 's/^/        /' || echo "        No gateway found"
    else
        route -n | grep "^0.0.0.0" | sed 's/^/        /' 2>/dev/null || echo "        Route info not available"
    fi
    echo ""
    echo -e "${CYAN}    [+] DNS Servers:${RESET}"
    if [ -f /etc/resolv.conf ]; then
        grep "nameserver" /etc/resolv.conf | sed 's/^/        /' || echo "        No DNS servers found"
    else
        echo "        DNS info not available"
    fi
    echo ""
    echo -e "${GREEN}    [✓] Network information displayed!${RESET}"
    echo ""
    echo -ne "${PURPLE}    Press Enter to continue...${RESET}"
    read
}

# Update function
update_tool() {
    clear
    echo ""
    echo -e "${PURPLE}    +====================================================+"
    echo -e "    |            UPDATE TOOL                             |"
    echo -e "    +====================================================+${RESET}"
    echo ""
    echo -e "${CYAN}    [*] Checking for updates...${RESET}"
    echo ""
    
    # Check if git is installed
    if ! command -v git &> /dev/null; then
        echo -e "${RED}    [✗] Git is not installed!${RESET}"
        echo -e "${YELLOW}    [!] Please install git first:${RESET}"
        echo -e "${WHITE}        sudo apt install git -y${RESET}"
        echo -e "${WHITE}        or${RESET}"
        echo -e "${WHITE}        sudo yum install git -y${RESET}"
        echo ""
        echo -ne "${PURPLE}    Press Enter to continue...${RESET}"
        read
        return
    fi
    
    # Repository URL
    REPO_URL="https://github.com/00xk/Toolz"
    TOOL_DIR="$HOME/Toolz"
    
    echo -e "${CYAN}    [+] Repository: ${WHITE}$REPO_URL${RESET}"
    echo ""
    
    # Check if directory exists
    if [ -d "$TOOL_DIR" ]; then
        echo -e "${YELLOW}    [*] Tool directory found. Updating...${RESET}"
        echo ""
        cd "$TOOL_DIR"
        
        # Fetch updates
        git fetch origin &>/dev/null
        LOCAL=$(git rev-parse @)
        REMOTE=$(git rev-parse @{u} 2>/dev/null)
        
        if [ "$LOCAL" = "$REMOTE" ]; then
            echo -e "${GREEN}    [✓] Already up to date!${RESET}"
        else
            echo -e "${CYAN}    [*] New updates available. Pulling changes...${RESET}"
            git pull origin main 2>/dev/null || git pull origin master 2>/dev/null
            
            if [ $? -eq 0 ]; then
                echo -e "${GREEN}    [✓] Tool updated successfully!${RESET}"
                echo -e "${CYAN}    [+] Please restart the tool to use new features${RESET}"
            else
                echo -e "${RED}    [✗] Update failed!${RESET}"
                echo -e "${YELLOW}    [!] Try manually: cd $TOOL_DIR && git pull${RESET}"
            fi
        fi
    else
        echo -e "${YELLOW}    [*] Tool directory not found. Installing...${RESET}"
        echo ""
        cd "$HOME"
        
        echo -e "${CYAN}    [*] Cloning repository...${RESET}"
        git clone "$REPO_URL" 2>&1 | sed 's/^/        /'
        
        if [ $? -eq 0 ]; then
            echo ""
            echo -e "${GREEN}    [✓] Tool installed successfully!${RESET}"
            echo -e "${CYAN}    [+] Location: ${WHITE}$TOOL_DIR${RESET}"
            echo -e "${CYAN}    [+] Run: ${WHITE}cd $TOOL_DIR && bash tool.sh${RESET}"
        else
            echo ""
            echo -e "${RED}    [✗] Installation failed!${RESET}"
            echo -e "${YELLOW}    [!] Check your internet connection and try again${RESET}"
        fi
    fi
    
    echo ""
    echo -ne "${PURPLE}    Press Enter to continue...${RESET}"
    read
}

# About
about() {
    clear
    echo ""
    echo -e "${PURPLE}    +====================================================+"
    echo -e "    |                 ABOUT                              |"
    echo -e "    +====================================================+${RESET}"
    echo ""
    echo -e "${CYAN}    [+] Tool Name:    ${WHITE}Toolz${RESET}"
    echo -e "${CYAN}    [+] Version:      ${WHITE}1.0.0${RESET}"
    echo -e "${CYAN}    [+] Author:       ${WHITE}00xk${RESET}"
    echo -e "${CYAN}    [+] GitHub:       ${WHITE}https://github.com/00xk/Toolz${RESET}"
    echo -e "${CYAN}    [+] Description:  ${WHITE}A colorful multi-purpose system tool${RESET}"
    echo ""
    echo -e "${YELLOW}    +====================================================+"
    echo -e "    |              FEATURES                              |"
    echo -e "    +====================================================+${RESET}"
    echo ""
    echo -e "    ${GREEN}✓${WHITE}  System Information Display${RESET}"
    echo -e "    ${GREEN}✓${WHITE}  Network Tools & Diagnostics${RESET}"
    echo -e "    ${GREEN}✓${WHITE}  Auto-Update from GitHub${RESET}"
    echo -e "    ${GREEN}✓${WHITE}  Colorful Interface${RESET}"
    echo -e "    ${GREEN}✓${WHITE}  Easy to Use${RESET}"
    echo ""
    echo -e "${RED}    +====================================================+"
    echo -e "    |              WARNING                               |"
    echo -e "    +====================================================+${RESET}"
    echo ""
    echo -e "${YELLOW}    [!] For educational and authorized use only!${RESET}"
    echo -e "${YELLOW}    [!] Always get permission before testing on systems${RESET}"
    echo ""
    echo -ne "${PURPLE}    Press Enter to continue...${RESET}"
    read
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
                echo ""
                echo -e "${PURPLE}    +====================================================+"
                echo -e "    |        Thank you for using Toolz!                  |"
                echo -e "    |              Goodbye! 👋                           |"
                echo -e "    +====================================================+${RESET}"
                echo ""
                exit 0
                ;;
            *)
                echo ""
                echo -e "${RED}    [✗] Invalid option! Please select 0-4${RESET}"
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
