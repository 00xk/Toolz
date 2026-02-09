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
GRAY='\033[0;37m'

# Clear screen
clear

# Banner with skull
banner() {
    echo -e "${RED}"
    echo "    ══════════════════════════════════════════════════════════════"
    echo ""
    echo -e "                      ${WHITE}.・゜゜・．．・゜゜・．${RED}"
    echo -e "                  ${WHITE}　　　　　  ／＼　　 　 ／＼${RED}"
    echo -e "                ${WHITE}　 　　　  ／　　＼　 ／　　＼${RED}"
    echo -e "              ${WHITE}　　　　　 ｜　　　 ●　　　　｜${RED}"
    echo -e "            ${WHITE}　　　　　　｜　　　　　　　　 ｜${RED}"
    echo -e "          ${WHITE}　　　　　　　＼　　╱▔▔▔╲　 ／${RED}"
    echo -e "        ${WHITE}　　　　　　　　 ＼／　　　　＼／${RED}"
    echo -e "      ${WHITE}　　　　　　　　　　　　　　　　　　${RED}"
    echo ""
    echo -e "${CYAN}    ╔════════════════════════════════════════════════════════╗"
    echo -e "    ║                                                        ║"
    echo -e "    ║       ${YELLOW}████████╗ ██████╗  ██████╗ ██╗     ███████╗${CYAN}      ║"
    echo -e "    ║       ${YELLOW}╚══██╔══╝██╔═══██╗██╔═══██╗██║     ╚══███╔╝${CYAN}      ║"
    echo -e "    ║          ${YELLOW}██║   ██║   ██║██║   ██║██║       ███╔╝${CYAN}       ║"
    echo -e "    ║          ${YELLOW}██║   ██║   ██║██║   ██║██║      ███╔╝${CYAN}        ║"
    echo -e "    ║          ${YELLOW}██║   ╚██████╔╝╚██████╔╝███████╗███████╗${CYAN}      ║"
    echo -e "    ║          ${YELLOW}╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝${CYAN}      ║"
    echo -e "    ║                                                        ║"
    echo -e "    ╚════════════════════════════════════════════════════════╝${RESET}"
    echo ""
    echo -e "${PURPLE}    ┌────────────────────────────────────────────────────────┐"
    echo -e "    │  ${WHITE}Version: ${GREEN}2.0.0${PURPLE}        ${GRAY}│${PURPLE}  ${WHITE}Author: ${GREEN}00xk${PURPLE}                 │"
    echo -e "    │  ${WHITE}GitHub: ${CYAN}github.com/00xk/Toolz${PURPLE}                         │"
    echo -e "    └─────────────────────────────────────────────────────────┘${RESET}"
    echo ""
    echo "    ══════════════════════════════════════════════════════════════"
}

# Main menu
menu() {
    echo ""
    echo -e "${CYAN}    ╔══════════════════════════════════════════════════════════╗"
    echo -e "    ║                      ${WHITE}MAIN MENU${CYAN}                           ║"
    echo -e "    ╚══════════════════════════════════════════════════════════╝${RESET}"
    echo ""
    echo -e "    ${GREEN}┌─────────────────────────────────────────────────────────┐${RESET}"
    echo -e "    ${GREEN}│${RESET}  ${YELLOW}[${WHITE}1${YELLOW}]${RESET} ${WHITE}➤${RESET}  System Information                              ${GREEN}│${RESET}"
    echo -e "    ${GREEN}│${RESET}  ${YELLOW}[${WHITE}2${YELLOW}]${RESET} ${WHITE}➤${RESET}  Network Tools                                   ${GREEN}│${RESET}"
    echo -e "    ${GREEN}│${RESET}  ${YELLOW}[${WHITE}3${YELLOW}]${RESET} ${WHITE}➤${RESET}  Disk & Storage Info                             ${GREEN}│${RESET}"
    echo -e "    ${GREEN}│${RESET}  ${YELLOW}[${WHITE}4${YELLOW}]${RESET} ${WHITE}➤${RESET}  Process Monitor                                 ${GREEN}│${RESET}"
    echo -e "    ${GREEN}│${RESET}  ${YELLOW}[${WHITE}5${YELLOW}]${RESET} ${WHITE}➤${RESET}  Update Tool                                     ${GREEN}│${RESET}"
    echo -e "    ${GREEN}│${RESET}  ${YELLOW}[${WHITE}6${YELLOW}]${RESET} ${WHITE}➤${RESET}  About                                           ${GREEN}│${RESET}"
    echo -e "    ${GREEN}│${RESET}  ${RED}[${WHITE}0${RED}]${RESET} ${WHITE}➤${RESET}  Exit                                            ${GREEN}│${RESET}"
    echo -e "    ${GREEN}└─────────────────────────────────────────────────────────┘${RESET}"
    echo ""
    echo -ne "    ${CYAN}┌─[${WHITE}Select Option${CYAN}]${RESET}\n"
    echo -ne "    ${CYAN}└──>${RESET} ${GREEN}"
}

# System Information
system_info() {
    clear
    echo ""
    echo -e "${YELLOW}    ╔══════════════════════════════════════════════════════════╗"
    echo -e "    ║              SYSTEM INFORMATION                          ║"
    echo -e "    ╚══════════════════════════════════════════════════════════╝${RESET}"
    echo ""
    
    echo -e "${CYAN}    ┌─[${WHITE}Operating System${CYAN}]${RESET}"
    echo -e "    ${GRAY}└──>${RESET} $(uname -s) $(uname -r)"
    echo ""
    
    echo -e "${CYAN}    ┌─[${WHITE}Hostname${CYAN}]${RESET}"
    echo -e "    ${GRAY}└──>${RESET} $(hostname)"
    echo ""
    
    echo -e "${CYAN}    ┌─[${WHITE}Current User${CYAN}]${RESET}"
    echo -e "    ${GRAY}└──>${RESET} $(whoami)"
    echo ""
    
    echo -e "${CYAN}    ┌─[${WHITE}Date & Time${CYAN}]${RESET}"
    echo -e "    ${GRAY}└──>${RESET} $(date '+%Y-%m-%d %H:%M:%S %Z')"
    echo ""
    
    echo -e "${CYAN}    ┌─[${WHITE}System Uptime${CYAN}]${RESET}"
    UPTIME=$(uptime -p 2>/dev/null || uptime | awk '{print $3,$4}')
    echo -e "    ${GRAY}└──>${RESET} $UPTIME"
    echo ""
    
    echo -e "${CYAN}    ┌─[${WHITE}CPU Information${CYAN}]${RESET}"
    CPU=$(grep -m1 "model name" /proc/cpuinfo 2>/dev/null | cut -d: -f2 | xargs || echo "CPU info not available")
    echo -e "    ${GRAY}└──>${RESET} $CPU"
    echo ""
    
    echo -e "${CYAN}    ┌─[${WHITE}Memory Usage${CYAN}]${RESET}"
    if command -v free &> /dev/null; then
        MEM_INFO=$(free -h | grep Mem | awk '{printf "Total: %s | Used: %s | Free: %s | Usage: %.1f%%", $2, $3, $4, ($3/$2)*100}')
        echo -e "    ${GRAY}└──>${RESET} $MEM_INFO"
    else
        echo -e "    ${GRAY}└──>${RESET} Memory info not available"
    fi
    echo ""
    
    echo -e "${CYAN}    ┌─[${WHITE}Kernel Version${CYAN}]${RESET}"
    echo -e "    ${GRAY}└──>${RESET} $(uname -v)"
    echo ""
    
    echo -e "${GREEN}    ╔══════════════════════════════════════════════════════════╗"
    echo -e "    ║  ✓  Information gathered successfully!                   ║"
    echo -e "    ╚══════════════════════════════════════════════════════════╝${RESET}"
    echo ""
    echo -ne "${PURPLE}    Press Enter to continue...${RESET}"
    read
}

# Network Tools
network_tools() {
    clear
    echo ""
    echo -e "${YELLOW}    ╔══════════════════════════════════════════════════════════╗"
    echo -e "    ║                 NETWORK TOOLS                            ║"
    echo -e "    ╚══════════════════════════════════════════════════════════╝${RESET}"
    echo ""
    
    echo -e "${CYAN}    ┌─[${WHITE}Network Interfaces${CYAN}]${RESET}"
    if command -v ip &> /dev/null; then
        ip -br addr show | while read line; do
            echo -e "    ${GRAY}├──>${RESET} $line"
        done
    elif command -v ifconfig &> /dev/null; then
        ifconfig | grep -E "^[a-z]" | awk '{print $1}' | while read iface; do
            echo -e "    ${GRAY}├──>${RESET} $iface"
        done
    else
        echo -e "    ${GRAY}└──>${RESET} Network tools not available"
    fi
    echo ""
    
    echo -e "${CYAN}    ┌─[${WHITE}IP Addresses${CYAN}]${RESET}"
    if command -v hostname &> /dev/null; then
        hostname -I 2>/dev/null | tr ' ' '\n' | grep -v '^$' | while read ip; do
            echo -e "    ${GRAY}├──>${RESET} $ip"
        done
    else
        echo -e "    ${GRAY}└──>${RESET} IP info not available"
    fi
    echo ""
    
    echo -e "${CYAN}    ┌─[${WHITE}Default Gateway${CYAN}]${RESET}"
    if command -v ip &> /dev/null; then
        GATEWAY=$(ip route | grep default | awk '{print $3}' | head -1)
        [ -n "$GATEWAY" ] && echo -e "    ${GRAY}└──>${RESET} $GATEWAY" || echo -e "    ${GRAY}└──>${RESET} No gateway found"
    else
        echo -e "    ${GRAY}└──>${RESET} Route info not available"
    fi
    echo ""
    
    echo -e "${CYAN}    ┌─[${WHITE}DNS Servers${CYAN}]${RESET}"
    if [ -f /etc/resolv.conf ]; then
        grep "nameserver" /etc/resolv.conf | awk '{print $2}' | while read dns; do
            echo -e "    ${GRAY}├──>${RESET} $dns"
        done
    else
        echo -e "    ${GRAY}└──>${RESET} DNS info not available"
    fi
    echo ""
    
    echo -e "${CYAN}    ┌─[${WHITE}Public IP Address${CYAN}]${RESET}"
    PUBLIC_IP=$(curl -s ifconfig.me 2>/dev/null || curl -s icanhazip.com 2>/dev/null || echo "Unable to fetch")
    echo -e "    ${GRAY}└──>${RESET} $PUBLIC_IP"
    echo ""
    
    echo -e "${GREEN}    ╔══════════════════════════════════════════════════════════╗"
    echo -e "    ║  ✓  Network information displayed!                       ║"
    echo -e "    ╚══════════════════════════════════════════════════════════╝${RESET}"
    echo ""
    echo -ne "${PURPLE}    Press Enter to continue...${RESET}"
    read
}

# Disk & Storage Info
disk_storage() {
    clear
    echo ""
    echo -e "${YELLOW}    ╔══════════════════════════════════════════════════════════╗"
    echo -e "    ║              DISK & STORAGE INFORMATION                  ║"
    echo -e "    ╚══════════════════════════════════════════════════════════╝${RESET}"
    echo ""
    
    echo -e "${CYAN}    ┌─[${WHITE}Disk Usage${CYAN}]${RESET}"
    if command -v df &> /dev/null; then
        df -h | grep -E "^/dev/" | awk '{printf "    '"${GRAY}"'├──>'"${RESET}"' %s | Size: %s | Used: %s | Avail: %s | Use%%: %s\n", $1, $2, $3, $4, $5}'
    else
        echo -e "    ${GRAY}└──>${RESET} Disk info not available"
    fi
    echo ""
    
    echo -e "${CYAN}    ┌─[${WHITE}Mounted Filesystems${CYAN}]${RESET}"
    mount | grep "^/dev/" | awk '{print $1" on "$3" type "$5}' | while read line; do
        echo -e "    ${GRAY}├──>${RESET} $line"
    done
    echo ""
    
    echo -e "${CYAN}    ┌─[${WHITE}Disk I/O Statistics${CYAN}]${RESET}"
    if command -v iostat &> /dev/null; then
        iostat -d | tail -n +4 | head -5 | while read line; do
            echo -e "    ${GRAY}├──>${RESET} $line"
        done
    else
        echo -e "    ${GRAY}└──>${RESET} iostat not available (install sysstat)"
    fi
    echo ""
    
    echo -e "${GREEN}    ╔══════════════════════════════════════════════════════════╗"
    echo -e "    ║  ✓  Storage information displayed!                       ║"
    echo -e "    ╚══════════════════════════════════════════════════════════╝${RESET}"
    echo ""
    echo -ne "${PURPLE}    Press Enter to continue...${RESET}"
    read
}

# Process Monitor
process_monitor() {
    clear
    echo ""
    echo -e "${YELLOW}    ╔══════════════════════════════════════════════════════════╗"
    echo -e "    ║                PROCESS MONITOR                           ║"
    echo -e "    ╚══════════════════════════════════════════════════════════╝${RESET}"
    echo ""
    
    echo -e "${CYAN}    ┌─[${WHITE}Top 10 CPU Processes${CYAN}]${RESET}"
    ps aux --sort=-%cpu | head -11 | tail -10 | awk '{printf "    '"${GRAY}"'├──>'"${RESET}"' %s | CPU: %s%% | MEM: %s%% | CMD: %s\n", $2, $3, $4, $11}'
    echo ""
    
    echo -e "${CYAN}    ┌─[${WHITE}Top 10 Memory Processes${CYAN}]${RESET}"
    ps aux --sort=-%mem | head -11 | tail -10 | awk '{printf "    '"${GRAY}"'├──>'"${RESET}"' %s | MEM: %s%% | CPU: %s%% | CMD: %s\n", $2, $4, $3, $11}'
    echo ""
    
    echo -e "${CYAN}    ┌─[${WHITE}System Load Average${CYAN}]${RESET}"
    LOAD=$(uptime | awk -F'load average:' '{print $2}')
    echo -e "    ${GRAY}└──>${RESET} $LOAD"
    echo ""
    
    echo -e "${CYAN}    ┌─[${WHITE}Total Processes${CYAN}]${RESET}"
    TOTAL_PROC=$(ps aux | wc -l)
    echo -e "    ${GRAY}└──>${RESET} $TOTAL_PROC processes running"
    echo ""
    
    echo -e "${GREEN}    ╔══════════════════════════════════════════════════════════╗"
    echo -e "    ║  ✓  Process information displayed!                       ║"
    echo -e "    ╚══════════════════════════════════════════════════════════╝${RESET}"
    echo ""
    echo -ne "${PURPLE}    Press Enter to continue...${RESET}"
    read
}

# Update function
update_tool() {
    clear
    echo ""
    echo -e "${PURPLE}    ╔══════════════════════════════════════════════════════════╗"
    echo -e "    ║                   UPDATE TOOL                            ║"
    echo -e "    ╚══════════════════════════════════════════════════════════╝${RESET}"
    echo ""
    echo -e "${CYAN}    [*] Checking for updates...${RESET}"
    echo ""
    
    # Check if git is installed
    if ! command -v git &> /dev/null; then
        echo -e "${RED}    ╔══════════════════════════════════════════════════════════╗"
        echo -e "    ║  ✗  Git is not installed!                                ║"
        echo -e "    ╚══════════════════════════════════════════════════════════╝${RESET}"
        echo ""
        echo -e "${YELLOW}    [!] Please install git first:${RESET}"
        echo -e "${WHITE}        • Debian/Ubuntu: ${GREEN}sudo apt install git -y${RESET}"
        echo -e "${WHITE}        • RedHat/CentOS: ${GREEN}sudo yum install git -y${RESET}"
        echo -e "${WHITE}        • Arch Linux:    ${GREEN}sudo pacman -S git${RESET}"
        echo ""
        echo -ne "${PURPLE}    Press Enter to continue...${RESET}"
        read
        return
    fi
    
    # Repository URL
    REPO_URL="https://github.com/00xk/Toolz"
    TOOL_DIR="$HOME/Toolz"
    
    echo -e "${CYAN}    ┌─[${WHITE}Repository${CYAN}]${RESET}"
    echo -e "    ${GRAY}└──>${RESET} $REPO_URL"
    echo ""
    
    # Check if directory exists
    if [ -d "$TOOL_DIR" ]; then
        echo -e "${YELLOW}    [*] Tool directory found. Checking for updates...${RESET}"
        echo ""
        cd "$TOOL_DIR"
        
        # Fetch updates
        git fetch origin &>/dev/null
        LOCAL=$(git rev-parse @ 2>/dev/null)
        REMOTE=$(git rev-parse @{u} 2>/dev/null)
        
        if [ "$LOCAL" = "$REMOTE" ]; then
            echo -e "${GREEN}    ╔══════════════════════════════════════════════════════════╗"
            echo -e "    ║  ✓  Already up to date!                                  ║"
            echo -e "    ╚══════════════════════════════════════════════════════════╝${RESET}"
        else
            echo -e "${CYAN}    [*] New updates available. Pulling changes...${RESET}"
            echo ""
            git pull origin main 2>/dev/null || git pull origin master 2>/dev/null
            
            if [ $? -eq 0 ]; then
                echo ""
                echo -e "${GREEN}    ╔══════════════════════════════════════════════════════════╗"
                echo -e "    ║  ✓  Tool updated successfully!                           ║"
                echo -e "    ╚══════════════════════════════════════════════════════════╝${RESET}"
                echo ""
                echo -e "${CYAN}    [+] Please restart the tool to use new features${RESET}"
            else
                echo ""
                echo -e "${RED}    ╔══════════════════════════════════════════════════════════╗"
                echo -e "    ║  ✗  Update failed!                                       ║"
                echo -e "    ╚══════════════════════════════════════════════════════════╝${RESET}"
                echo ""
                echo -e "${YELLOW}    [!] Try manually: ${WHITE}cd $TOOL_DIR && git pull${RESET}"
            fi
        fi
    else
        echo -e "${YELLOW}    [*] Tool directory not found. Installing...${RESET}"
        echo ""
        cd "$HOME"
        
        echo -e "${CYAN}    [*] Cloning repository...${RESET}"
        echo ""
        git clone "$REPO_URL"
        
        if [ $? -eq 0 ]; then
            echo ""
            echo -e "${GREEN}    ╔══════════════════════════════════════════════════════════╗"
            echo -e "    ║  ✓  Tool installed successfully!                         ║"
            echo -e "    ╚══════════════════════════════════════════════════════════╝${RESET}"
            echo ""
            echo -e "${CYAN}    ┌─[${WHITE}Installation Path${CYAN}]${RESET}"
            echo -e "    ${GRAY}└──>${RESET} $TOOL_DIR"
            echo ""
            echo -e "${CYAN}    ┌─[${WHITE}Run Command${CYAN}]${RESET}"
            echo -e "    ${GRAY}└──>${RESET} cd $TOOL_DIR && bash tool.sh"
        else
            echo ""
            echo -e "${RED}    ╔══════════════════════════════════════════════════════════╗"
            echo -e "    ║  ✗  Installation failed!                                 ║"
            echo -e "    ╚══════════════════════════════════════════════════════════╝${RESET}"
            echo ""
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
    echo -e "${PURPLE}    ╔══════════════════════════════════════════════════════════╗"
    echo -e "    ║                      ABOUT                               ║"
    echo -e "    ╚══════════════════════════════════════════════════════════╝${RESET}"
    echo ""
    echo -e "${CYAN}    ┌─[${WHITE}Tool Information${CYAN}]${RESET}"
    echo -e "    ${GRAY}├──>${RESET} Name:        ${WHITE}Toolz${RESET}"
    echo -e "    ${GRAY}├──>${RESET} Version:     ${WHITE}2.0.0${RESET}"
    echo -e "    ${GRAY}├──>${RESET} Author:      ${WHITE}00xk${RESET}"
    echo -e "    ${GRAY}├──>${RESET} GitHub:      ${CYAN}https://github.com/00xk/Toolz${RESET}"
    echo -e "    ${GRAY}└──>${RESET} Description: ${WHITE}A colorful multi-purpose system tool${RESET}"
    echo ""
    echo -e "${YELLOW}    ╔══════════════════════════════════════════════════════════╗"
    echo -e "    ║                     FEATURES                             ║"
    echo -e "    ╚══════════════════════════════════════════════════════════╝${RESET}"
    echo ""
    echo -e "    ${GREEN}✓${RESET}  Comprehensive System Information Display"
    echo -e "    ${GREEN}✓${RESET}  Advanced Network Tools & Diagnostics"
    echo -e "    ${GREEN}✓${RESET}  Disk & Storage Analysis"
    echo -e "    ${GREEN}✓${RESET}  Real-time Process Monitoring"
    echo -e "    ${GREEN}✓${RESET}  Auto-Update from GitHub Repository"
    echo -e "    ${GREEN}✓${RESET}  Beautiful Colorful Interface"
    echo -e "    ${GREEN}✓${RESET}  Cross-Platform Compatibility"
    echo -e "    ${GREEN}✓${RESET}  Easy to Use & Lightweight"
    echo ""
    echo -e "${RED}    ╔══════════════════════════════════════════════════════════╗"
    echo -e "    ║                     WARNING                              ║"
    echo -e "    ╚══════════════════════════════════════════════════════════╝${RESET}"
    echo ""
    echo -e "${YELLOW}    [!] For educational and authorized use only!"
    echo -e "    [!] Always get permission before testing on systems"
    echo -e "    [!] Use responsibly and ethically${RESET}"
    echo ""
    echo -e "${CYAN}    ┌─[${WHITE}Support${CYAN}]${RESET}"
    echo -e "    ${GRAY}├──>${RESET} Report Issues: ${CYAN}https://github.com/00xk/Toolz/issues${RESET}"
    echo -e "    ${GRAY}└──>${RESET} Contribute:    ${CYAN}https://github.com/00xk/Toolz/pulls${RESET}"
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
                disk_storage
                ;;
            4)
                process_monitor
                ;;
            5)
                update_tool
                ;;
            6)
                about
                ;;
            0)
                clear
                echo ""
                echo -e "${PURPLE}    ╔══════════════════════════════════════════════════════════╗"
                echo -e "    ║                                                          ║"
                echo -e "    ║            ${WHITE}Thank you for using Toolz!${PURPLE}                   ║"
                echo -e "    ║                                                          ║"
                echo -e "    ║                  ${YELLOW}Goodbye! 👋${PURPLE}                           ║"
                echo -e "    ║                                                          ║"
                echo -e "    ╚══════════════════════════════════════════════════════════╝${RESET}"
                echo ""
                exit 0
                ;;
            *)
                echo ""
                echo -e "${RED}    ╔══════════════════════════════════════════════════════════╗"
                echo -e "    ║  ✗  Invalid option! Please select 0-6                    ║"
                echo -e "    ╚══════════════════════════════════════════════════════════╝${RESET}"
                sleep 2
                ;;
        esac
    done
}

# Startup checks
startup_checks() {
    # Check if running as root
    if [ "$EUID" -eq 0 ]; then 
        echo -e "${YELLOW}"
        echo "    ╔══════════════════════════════════════════════════════════╗"
        echo "    ║  ⚠  Running as root! Please be careful.                 ║"
        echo "    ╚══════════════════════════════════════════════════════════╝"
        echo -e "${RESET}"
        sleep 2
    fi
}

# Run startup checks
startup_checks

# Run main function
main
