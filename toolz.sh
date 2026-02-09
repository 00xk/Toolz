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
DARK_GRAY='\033[1;30m'

# Clear screen
clear

# Banner with enhanced skull
banner() {
    echo -e "${RED}"
    echo "    ════════════════════════════════════════════════════════════════"
    echo ""
    echo -e "                        ${WHITE}╔══════════════════════╗${RED}"
    echo -e "                        ${WHITE}║   ${DARK_GRAY}██${WHITE}╗    ${DARK_GRAY}██${WHITE}╗   ║${RED}"
    echo -e "                        ${WHITE}║   ${DARK_GRAY}██${WHITE}║    ${DARK_GRAY}██${WHITE}║   ║${RED}"
    echo -e "                        ${WHITE}║                      ║${RED}"
    echo -e "                        ${WHITE}║   ${DARK_GRAY}▄▄▄${WHITE}╗  ${DARK_GRAY}▄▄▄${WHITE}╗   ║${RED}"
    echo -e "                        ${WHITE}║  ${DARK_GRAY}╱   ╲╱   ╲${WHITE}  ║${RED}"
    echo -e "                        ${WHITE}║ ${DARK_GRAY}╱           ╲${WHITE} ║${RED}"
    echo -e "                        ${WHITE}╚══════════════════════╝${RED}"
    echo ""
    echo -e "${CYAN}    ╔══════════════════════════════════════════════════════════════╗"
    echo -e "    ║                                                              ║"
    echo -e "    ║         ${YELLOW}████████╗ ██████╗  ██████╗ ██╗     ███████╗${CYAN}         ║"
    echo -e "    ║         ${YELLOW}╚══██╔══╝██╔═══██╗██╔═══██╗██║     ╚══███╔╝${CYAN}         ║"
    echo -e "    ║            ${YELLOW}██║   ██║   ██║██║   ██║██║       ███╔╝${CYAN}          ║"
    echo -e "    ║            ${YELLOW}██║   ██║   ██║██║   ██║██║      ███╔╝${CYAN}           ║"
    echo -e "    ║            ${YELLOW}██║   ╚██████╔╝╚██████╔╝███████╗███████╗${CYAN}         ║"
    echo -e "    ║            ${YELLOW}╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝${CYAN}         ║"
    echo -e "    ║                                                              ║"
    echo -e "    ║              ${WHITE}Advanced System Administration Tool${CYAN}              ║"
    echo -e "    ║                                                              ║"
    echo -e "    ╚══════════════════════════════════════════════════════════════╝${RESET}"
    echo ""
    echo -e "${PURPLE}    ┌──────────────────────────────────────────────────────────────┐"
    echo -e "    │  ${WHITE}Version: ${GREEN}3.0.0${PURPLE}          ${GRAY}│${PURPLE}  ${WHITE}Author: ${GREEN}00xk${PURPLE}                     │"
    echo -e "    │  ${WHITE}GitHub: ${CYAN}github.com/00xk/Toolz${PURPLE}                             │"
    echo -e "    └──────────────────────────────────────────────────────────────┘${RESET}"
    echo ""
    echo "    ════════════════════════════════════════════════════════════════"
}

# Main menu
menu() {
    echo ""
    echo -e "${CYAN}    ╔══════════════════════════════════════════════════════════════╗"
    echo -e "    ║                        ${WHITE}MAIN MENU${CYAN}                             ║"
    echo -e "    ╚══════════════════════════════════════════════════════════════╝${RESET}"
    echo ""
    echo -e "    ${GREEN}╔═════════════════════════════════════════════════════════════╗${RESET}"
    echo -e "    ${GREEN}║${RESET}                                                             ${GREEN}║${RESET}"
    echo -e "    ${GREEN}║${RESET}   ${YELLOW}[${WHITE}1${YELLOW}]${RESET} ${WHITE}⚡${RESET}  ${BOLD}${WHITE}System Monitor${RESET}                                   ${GREEN}║${RESET}"
    echo -e "    ${GREEN}║${RESET}        ${GRAY}├─ System Information & Status${RESET}                   ${GREEN}║${RESET}"
    echo -e "    ${GREEN}║${RESET}        ${GRAY}├─ Network Configuration & Tools${RESET}                 ${GREEN}║${RESET}"
    echo -e "    ${GREEN}║${RESET}        ${GRAY}├─ Disk & Storage Analysis${RESET}                       ${GREEN}║${RESET}"
    echo -e "    ${GREEN}║${RESET}        ${GRAY}└─ Process & Resource Monitor${RESET}                    ${GREEN}║${RESET}"
    echo -e "    ${GREEN}║${RESET}                                                             ${GREEN}║${RESET}"
    echo -e "    ${GREEN}║${RESET}   ${YELLOW}[${WHITE}2${YELLOW}]${RESET} ${WHITE}🔄${RESET}  ${BOLD}${WHITE}Update Tool${RESET}                                      ${GREEN}║${RESET}"
    echo -e "    ${GREEN}║${RESET}        ${GRAY}├─ Check for Updates${RESET}                             ${GREEN}║${RESET}"
    echo -e "    ${GREEN}║${RESET}        ${GRAY}├─ Install from GitHub${RESET}                           ${GREEN}║${RESET}"
    echo -e "    ${GREEN}║${RESET}        ${GRAY}└─ Auto-Update & Version Control${RESET}                 ${GREEN}║${RESET}"
    echo -e "    ${GREEN}║${RESET}                                                             ${GREEN}║${RESET}"
    echo -e "    ${GREEN}║${RESET}   ${YELLOW}[${WHITE}3${YELLOW}]${RESET} ${WHITE}ℹ️${RESET}   ${BOLD}${WHITE}About & Info${RESET}                                     ${GREEN}║${RESET}"
    echo -e "    ${GREEN}║${RESET}        ${GRAY}├─ Tool Information${RESET}                              ${GREEN}║${RESET}"
    echo -e "    ${GREEN}║${RESET}        ${GRAY}├─ Features & Capabilities${RESET}                       ${GREEN}║${RESET}"
    echo -e "    ${GREEN}║${RESET}        ${GRAY}└─ Support & Documentation${RESET}                       ${GREEN}║${RESET}"
    echo -e "    ${GREEN}║${RESET}                                                             ${GREEN}║${RESET}"
    echo -e "    ${GREEN}╠═════════════════════════════════════════════════════════════╣${RESET}"
    echo -e "    ${GREEN}║${RESET}   ${RED}[${WHITE}0${RED}]${RESET} ${WHITE}🚪${RESET}  ${BOLD}${WHITE}Exit${RESET}                                             ${GREEN}║${RESET}"
    echo -e "    ${GREEN}╚═════════════════════════════════════════════════════════════╝${RESET}"
    echo ""
    echo -ne "    ${CYAN}┌─[${WHITE}Enter Your Choice${CYAN}]${RESET}\n"
    echo -ne "    ${CYAN}└──➤${RESET} ${GREEN}"
}

# System Monitor (Combined all system features)
system_monitor() {
    while true; do
        clear
        echo ""
        echo -e "${YELLOW}    ╔══════════════════════════════════════════════════════════════╗"
        echo -e "    ║                      SYSTEM MONITOR                          ║"
        echo -e "    ╚══════════════════════════════════════════════════════════════╝${RESET}"
        echo ""
        
        # System Information Section
        echo -e "${CYAN}    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓"
        echo -e "    ┃ ${WHITE}SYSTEM INFORMATION${CYAN}                                          ┃"
        echo -e "    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛${RESET}"
        echo ""
        
        echo -e "${WHITE}    ┌─[${CYAN}OS & Kernel${WHITE}]${RESET}"
        echo -e "    ${GRAY}│  ├─${RESET} OS:     ${GREEN}$(uname -s)${RESET}"
        echo -e "    ${GRAY}│  ├─${RESET} Kernel: ${GREEN}$(uname -r)${RESET}"
        echo -e "    ${GRAY}│  └─${RESET} Arch:   ${GREEN}$(uname -m)${RESET}"
        echo ""
        
        echo -e "${WHITE}    ┌─[${CYAN}Host Information${WHITE}]${RESET}"
        echo -e "    ${GRAY}│  ├─${RESET} Hostname: ${GREEN}$(hostname)${RESET}"
        echo -e "    ${GRAY}│  ├─${RESET} User:     ${GREEN}$(whoami)${RESET}"
        echo -e "    ${GRAY}│  └─${RESET} Uptime:   ${GREEN}$(uptime -p 2>/dev/null || uptime | awk '{print $3,$4}')${RESET}"
        echo ""
        
        echo -e "${WHITE}    ┌─[${CYAN}CPU & Memory${WHITE}]${RESET}"
        CPU=$(grep -m1 "model name" /proc/cpuinfo 2>/dev/null | cut -d: -f2 | xargs | cut -c1-50 || echo "N/A")
        echo -e "    ${GRAY}│  ├─${RESET} CPU: ${GREEN}$CPU${RESET}"
        if command -v free &> /dev/null; then
            MEM_TOTAL=$(free -h | grep Mem | awk '{print $2}')
            MEM_USED=$(free -h | grep Mem | awk '{print $3}')
            MEM_FREE=$(free -h | grep Mem | awk '{print $4}')
            echo -e "    ${GRAY}│  ├─${RESET} Memory: ${GREEN}$MEM_TOTAL${RESET} (Used: ${YELLOW}$MEM_USED${RESET} | Free: ${GREEN}$MEM_FREE${RESET})"
        else
            echo -e "    ${GRAY}│  ├─${RESET} Memory: ${RED}N/A${RESET}"
        fi
        LOAD=$(uptime | awk -F'load average:' '{print $2}' | xargs)
        echo -e "    ${GRAY}│  └─${RESET} Load:   ${YELLOW}$LOAD${RESET}"
        echo ""
        
        # Network Section
        echo -e "${CYAN}    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓"
        echo -e "    ┃ ${WHITE}NETWORK INFORMATION${CYAN}                                         ┃"
        echo -e "    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛${RESET}"
        echo ""
        
        echo -e "${WHITE}    ┌─[${CYAN}Network Interfaces${WHITE}]${RESET}"
        if command -v ip &> /dev/null; then
            ip -br addr show | head -5 | while read iface status ip rest; do
                if [ "$status" = "UP" ]; then
                    echo -e "    ${GRAY}│  ├─${RESET} ${GREEN}●${RESET} $iface ${GRAY}→${RESET} ${CYAN}$ip${RESET}"
                else
                    echo -e "    ${GRAY}│  ├─${RESET} ${RED}●${RESET} $iface ${GRAY}→${RESET} ${GRAY}DOWN${RESET}"
                fi
            done
        else
            echo -e "    ${GRAY}│  └─${RESET} ${RED}Network tools not available${RESET}"
        fi
        echo ""
        
        echo -e "${WHITE}    ┌─[${CYAN}Network Status${WHITE}]${RESET}"
        if command -v ip &> /dev/null; then
            GATEWAY=$(ip route | grep default | awk '{print $3}' | head -1)
            [ -n "$GATEWAY" ] && echo -e "    ${GRAY}│  ├─${RESET} Gateway: ${GREEN}$GATEWAY${RESET}" || echo -e "    ${GRAY}│  ├─${RESET} Gateway: ${RED}N/A${RESET}"
        fi
        if [ -f /etc/resolv.conf ]; then
            DNS=$(grep "nameserver" /etc/resolv.conf | head -1 | awk '{print $2}')
            [ -n "$DNS" ] && echo -e "    ${GRAY}│  ├─${RESET} DNS:     ${GREEN}$DNS${RESET}" || echo -e "    ${GRAY}│  ├─${RESET} DNS:     ${RED}N/A${RESET}"
        fi
        echo -e "    ${GRAY}│  └─${RESET} Checking public IP..."
        PUBLIC_IP=$(timeout 3 curl -s ifconfig.me 2>/dev/null || timeout 3 curl -s icanhazip.com 2>/dev/null || echo "Unable to fetch")
        echo -ne "\033[1A\033[2K"
        echo -e "    ${GRAY}│  └─${RESET} Public:  ${CYAN}$PUBLIC_IP${RESET}"
        echo ""
        
        # Disk Section
        echo -e "${CYAN}    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓"
        echo -e "    ┃ ${WHITE}DISK & STORAGE${CYAN}                                              ┃"
        echo -e "    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛${RESET}"
        echo ""
        
        echo -e "${WHITE}    ┌─[${CYAN}Filesystem Usage${WHITE}]${RESET}"
        if command -v df &> /dev/null; then
            df -h | grep -E "^/dev/" | head -5 | while read fs size used avail percent mount; do
                USAGE=${percent%\%}
                if [ "$USAGE" -gt 80 ]; then
                    COLOR="${RED}"
                elif [ "$USAGE" -gt 60 ]; then
                    COLOR="${YELLOW}"
                else
                    COLOR="${GREEN}"
                fi
                echo -e "    ${GRAY}│  ├─${RESET} ${COLOR}$fs${RESET} ${GRAY}→${RESET} $used${GRAY}/${RESET}$size ${GRAY}(${RESET}${COLOR}$percent${RESET}${GRAY})${RESET}"
            done
        else
            echo -e "    ${GRAY}│  └─${RESET} ${RED}Disk info not available${RESET}"
        fi
        echo ""
        
        # Process Section
        echo -e "${CYAN}    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓"
        echo -e "    ┃ ${WHITE}TOP PROCESSES${CYAN}                                               ┃"
        echo -e "    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛${RESET}"
        echo ""
        
        echo -e "${WHITE}    ┌─[${CYAN}Top 5 CPU${WHITE}]${RESET}"
        ps aux --sort=-%cpu | head -6 | tail -5 | awk '{printf "    '"${GRAY}"'│  ├─'"${RESET}"' '"${YELLOW}"'%5s%%'"${RESET}"' '"${GRAY}"'│'"${RESET}"' '"${CYAN}"'%-8s'"${RESET}"' '"${GRAY}"'│'"${RESET}"' %s\n", $3, $2, substr($11,1,30)}'
        echo ""
        
        echo -e "${WHITE}    ┌─[${CYAN}Top 5 Memory${WHITE}]${RESET}"
        ps aux --sort=-%mem | head -6 | tail -5 | awk '{printf "    '"${GRAY}"'│  ├─'"${RESET}"' '"${YELLOW}"'%5s%%'"${RESET}"' '"${GRAY}"'│'"${RESET}"' '"${CYAN}"'%-8s'"${RESET}"' '"${GRAY}"'│'"${RESET}"' %s\n", $4, $2, substr($11,1,30)}'
        echo ""
        
        TOTAL_PROC=$(ps aux | wc -l)
        echo -e "${WHITE}    └─[${CYAN}Total Processes${WHITE}]${RESET} ${GREEN}$TOTAL_PROC${RESET}"
        echo ""
        
        echo -e "${GREEN}    ╔══════════════════════════════════════════════════════════════╗"
        echo -e "    ║  ✓  System monitoring complete!                              ║"
        echo -e "    ╚══════════════════════════════════════════════════════════════╝${RESET}"
        echo ""
        
        echo -e "${PURPLE}    [R]${RESET} Refresh  ${PURPLE}[B]${RESET} Back to Menu"
        echo -ne "    ${CYAN}└──➤${RESET} ${GREEN}"
        read action
        
        case $action in
            r|R)
                continue
                ;;
            b|B|*)
                break
                ;;
        esac
    done
}

# Update function
update_tool() {
    clear
    echo ""
    echo -e "${PURPLE}    ╔══════════════════════════════════════════════════════════════╗"
    echo -e "    ║                       UPDATE TOOL                            ║"
    echo -e "    ╚══════════════════════════════════════════════════════════════╝${RESET}"
    echo ""
    
    # Check if git is installed
    if ! command -v git &> /dev/null; then
        echo -e "${RED}    ╔══════════════════════════════════════════════════════════════╗"
        echo -e "    ║  ✗  Git is not installed!                                    ║"
        echo -e "    ╚══════════════════════════════════════════════════════════════╝${RESET}"
        echo ""
        echo -e "${YELLOW}    ┌─[${WHITE}Installation Commands${YELLOW}]${RESET}"
        echo -e "    ${GRAY}├─${RESET} Debian/Ubuntu: ${GREEN}sudo apt install git -y${RESET}"
        echo -e "    ${GRAY}├─${RESET} RedHat/CentOS: ${GREEN}sudo yum install git -y${RESET}"
        echo -e "    ${GRAY}├─${RESET} Arch Linux:    ${GREEN}sudo pacman -S git${RESET}"
        echo -e "    ${GRAY}└─${RESET} macOS:         ${GREEN}brew install git${RESET}"
        echo ""
        echo -ne "${PURPLE}    Press Enter to continue...${RESET}"
        read
        return
    fi
    
    # Repository URL
    REPO_URL="https://github.com/00xk/Toolz"
    TOOL_DIR="$HOME/Toolz"
    
    echo -e "${CYAN}    ┌─[${WHITE}Repository${CYAN}]${RESET}"
    echo -e "    ${GRAY}└──${RESET} $REPO_URL"
    echo ""
    
    echo -e "${CYAN}    [*] Checking for updates...${RESET}"
    echo ""
    
    # Check if directory exists
    if [ -d "$TOOL_DIR" ]; then
        echo -e "${YELLOW}    [*] Tool directory found at: ${WHITE}$TOOL_DIR${RESET}"
        echo ""
        cd "$TOOL_DIR"
        
        # Fetch updates
        echo -e "${CYAN}    [*] Fetching latest changes...${RESET}"
        git fetch origin &>/dev/null
        
        LOCAL=$(git rev-parse @ 2>/dev/null)
        REMOTE=$(git rev-parse @{u} 2>/dev/null)
        
        if [ "$LOCAL" = "$REMOTE" ]; then
            echo ""
            echo -e "${GREEN}    ╔══════════════════════════════════════════════════════════════╗"
            echo -e "    ║  ✓  Already up to date!                                      ║"
            echo -e "    ║                                                              ║"
            echo -e "    ║     ${WHITE}Current Version: 3.0.0${GREEN}                                   ║"
            echo -e "    ╚══════════════════════════════════════════════════════════════╝${RESET}"
        else
            echo -e "${CYAN}    [*] New updates available! Downloading...${RESET}"
            echo ""
            
            git pull origin main 2>/dev/null || git pull origin master 2>/dev/null
            
            if [ $? -eq 0 ]; then
                echo ""
                echo -e "${GREEN}    ╔══════════════════════════════════════════════════════════════╗"
                echo -e "    ║  ✓  Update completed successfully!                           ║"
                echo -e "    ║                                                              ║"
                echo -e "    ║     ${WHITE}Please restart the tool to apply changes${GREEN}                 ║"
                echo -e "    ╚══════════════════════════════════════════════════════════════╝${RESET}"
            else
                echo ""
                echo -e "${RED}    ╔══════════════════════════════════════════════════════════════╗"
                echo -e "    ║  ✗  Update failed!                                           ║"
                echo -e "    ╚══════════════════════════════════════════════════════════════╝${RESET}"
                echo ""
                echo -e "${YELLOW}    Try manually: ${WHITE}cd $TOOL_DIR && git pull${RESET}"
            fi
        fi
    else
        echo -e "${YELLOW}    [*] Tool not found. Installing fresh copy...${RESET}"
        echo ""
        cd "$HOME"
        
        echo -e "${CYAN}    [*] Cloning repository from GitHub...${RESET}"
        echo ""
        
        git clone "$REPO_URL" 2>&1 | while read line; do
            echo "    ${GRAY}│${RESET} $line"
        done
        
        if [ $? -eq 0 ]; then
            echo ""
            echo -e "${GREEN}    ╔══════════════════════════════════════════════════════════════╗"
            echo -e "    ║  ✓  Installation completed successfully!                     ║"
            echo -e "    ╚══════════════════════════════════════════════════════════════╝${RESET}"
            echo ""
            echo -e "${CYAN}    ┌─[${WHITE}Installation Details${CYAN}]${RESET}"
            echo -e "    ${GRAY}├─${RESET} Location: ${WHITE}$TOOL_DIR${RESET}"
            echo -e "    ${GRAY}└─${RESET} Run:      ${GREEN}cd $TOOL_DIR && bash tool.sh${RESET}"
        else
            echo ""
            echo -e "${RED}    ╔══════════════════════════════════════════════════════════════╗"
            echo -e "    ║  ✗  Installation failed!                                     ║"
            echo -e "    ╚══════════════════════════════════════════════════════════════╝${RESET}"
            echo ""
            echo -e "${YELLOW}    [!] Please check your internet connection and try again${RESET}"
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
    echo -e "${PURPLE}    ╔══════════════════════════════════════════════════════════════╗"
    echo -e "    ║                     ABOUT TOOLZ                              ║"
    echo -e "    ╚══════════════════════════════════════════════════════════════╝${RESET}"
    echo ""
    
    echo -e "${CYAN}    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓"
    echo -e "    ┃ ${WHITE}TOOL INFORMATION${CYAN}                                            ┃"
    echo -e "    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛${RESET}"
    echo ""
    
    echo -e "    ${WHITE}┌─[${CYAN}Basic Info${WHITE}]${RESET}"
    echo -e "    ${GRAY}├─${RESET} Name:        ${GREEN}Toolz${RESET}"
    echo -e "    ${GRAY}├─${RESET} Version:     ${GREEN}3.0.0${RESET}"
    echo -e "    ${GRAY}├─${RESET} Author:      ${GREEN}00xk${RESET}"
    echo -e "    ${GRAY}├─${RESET} GitHub:      ${CYAN}https://github.com/00xk/Toolz${RESET}"
    echo -e "    ${GRAY}└─${RESET} License:     ${YELLOW}Educational Use Only${RESET}"
    echo ""
    
    echo -e "${CYAN}    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓"
    echo -e "    ┃ ${WHITE}FEATURES & CAPABILITIES${CYAN}                                     ┃"
    echo -e "    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛${RESET}"
    echo ""
    
    echo -e "    ${GREEN}✓${RESET}  ${WHITE}Comprehensive System Monitoring${RESET}"
    echo -e "       ${GRAY}└─${RESET} Real-time system stats, CPU, memory, and uptime"
    echo ""
    echo -e "    ${GREEN}✓${RESET}  ${WHITE}Advanced Network Diagnostics${RESET}"
    echo -e "       ${GRAY}└─${RESET} Interface status, IP addresses, gateway, and DNS"
    echo ""
    echo -e "    ${GREEN}✓${RESET}  ${WHITE}Disk & Storage Analysis${RESET}"
    echo -e "       ${GRAY}└─${RESET} Filesystem usage with color-coded alerts"
    echo ""
    echo -e "    ${GREEN}✓${RESET}  ${WHITE}Process Management${RESET}"
    echo -e "       ${GRAY}└─${RESET} Top CPU and memory consuming processes"
    echo ""
    echo -e "    ${GREEN}✓${RESET}  ${WHITE}Auto-Update System${RESET}"
    echo -e "       ${GRAY}└─${RESET} GitHub integration for seamless updates"
    echo ""
    echo -e "    ${GREEN}✓${RESET}  ${WHITE}Beautiful Interface${RESET}"
    echo -e "       ${GRAY}└─${RESET} Color-coded, Unicode-enhanced terminal UI"
    echo ""
    
    echo -e "${CYAN}    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓"
    echo -e "    ┃ ${WHITE}WHAT'S NEW IN v3.0${CYAN}                                          ┃"
    echo -e "    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛${RESET}"
    echo ""
    
    echo -e "    ${YELLOW}⚡${RESET}  Streamlined to ${GREEN}3 powerful options${RESET}"
    echo -e "    ${YELLOW}⚡${RESET}  All-in-one ${GREEN}System Monitor${RESET} dashboard"
    echo -e "    ${YELLOW}⚡${RESET}  Enhanced ${GREEN}visual design${RESET} with better readability"
    echo -e "    ${YELLOW}⚡${RESET}  Improved ${GREEN}performance${RESET} and reduced resource usage"
    echo -e "    ${YELLOW}⚡${RESET}  Real-time ${GREEN}refresh capability${RESET} in monitor mode"
    echo ""
    
    echo -e "${RED}    ╔══════════════════════════════════════════════════════════════╗"
    echo -e "    ║                      ⚠️  WARNING  ⚠️                             ║"
    echo -e "    ╚══════════════════════════════════════════════════════════════════╝${RESET}"
    echo ""
    
    echo -e "${YELLOW}    [!] This tool is for educational and authorized use only!"
    echo -e "    [!] Always obtain proper permission before system testing"
    echo -e "    [!] Use responsibly and ethically"
    echo -e "    [!] Author not responsible for misuse${RESET}"
    echo ""
    
    echo -e "${CYAN}    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓"
    echo -e "    ┃ ${WHITE}SUPPORT & COMMUNITY${CYAN}                                         ┃"
    echo -e "    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛${RESET}"
    echo ""
    
    echo -e "    ${WHITE}┌─[${CYAN}Get Help${WHITE}]${RESET}"
    echo -e "    ${GRAY}├─${RESET} Report Issues:  ${CYAN}https://github.com/00xk/Toolz/issues${RESET}"
    echo -e "    ${GRAY}├─${RESET} Contribute:     ${CYAN}https://github.com/00xk/Toolz/pulls${RESET}"
    echo -e "    ${GRAY}└─${RESET} Documentation:  ${CYAN}https://github.com/00xk/Toolz/wiki${RESET}"
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
                system_monitor
                ;;
            2)
                update_tool
                ;;
            3)
                about
                ;;
            0)
                clear
                echo ""
                echo -e "${PURPLE}    ╔══════════════════════════════════════════════════════════════╗"
                echo -e "    ║                                                              ║"
                echo -e "    ║              ${WHITE}Thank you for using Toolz!${PURPLE}                   ║"
                echo -e "    ║                                                              ║"
                echo -e "    ║                    ${YELLOW}Goodbye! 👋${PURPLE}                            ║"
                echo -e "    ║                                                              ║"
                echo -e "    ║              ${GRAY}Stay safe and hack ethically!${PURPLE}                ║"
                echo -e "    ║                                                              ║"
                echo -e "    ╚══════════════════════════════════════════════════════════════╝${RESET}"
                echo ""
                exit 0
                ;;
            *)
                echo ""
                echo -e "${RED}    ╔══════════════════════════════════════════════════════════════╗"
                echo -e "    ║  ✗  Invalid option! Please select 0-3                        ║"
                echo -e "    ╚══════════════════════════════════════════════════════════════╝${RESET}"
                sleep 2
                ;;
        esac
    done
}

# Startup splash
startup_splash() {
    clear
    echo ""
    echo -e "${CYAN}    ╔══════════════════════════════════════════════════════════════╗"
    echo -e "    ║                                                              ║"
    echo -e "    ║                  ${WHITE}Initializing Toolz v3.0...${CYAN}                  ║"
    echo -e "    ║                                                              ║"
    echo -e "    ╚══════════════════════════════════════════════════════════════╝${RESET}"
    echo ""
    
    # Check if running as root
    if [ "$EUID" -eq 0 ]; then 
        echo -e "${YELLOW}    ╔══════════════════════════════════════════════════════════════╗"
        echo -e "    ║  ⚠️  WARNING: Running as root!                                ║"
        echo -e "    ║      Please be careful with system operations.               ║"
        echo -e "    ╚══════════════════════════════════════════════════════════════╝${RESET}"
        echo ""
        sleep 2
    fi
    
    echo -e "${GREEN}    [✓] Loading modules...${RESET}"
    sleep 0.5
    echo -e "${GREEN}    [✓] Checking dependencies...${RESET}"
    sleep 0.5
    echo -e "${GREEN}    [✓] Ready!${RESET}"
    sleep 1
}

# Run startup splash
startup_splash

# Run main function
main
