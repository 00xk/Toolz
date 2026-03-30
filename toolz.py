#!/usr/bin/env python3
import os
import time
import platform
import subprocess

# Colors
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
CYAN = "\033[1;36m"
WHITE = "\033[1;37m"
PURPLE = "\033[1;35m"
GRAY = "\033[0;37m"
RESET = "\033[0m"

def clear():
    os.system("clear")

def banner():
    print(RED + "════════════════════════════════════════════════════════════════")
    print(f"{CYAN}Toolz v3.0 - Advanced System Tool{RESET}")
    print("════════════════════════════════════════════════════════════════")

def menu():
    print(f"""
{CYAN}[1]{WHITE} System Monitor
{CYAN}[2]{WHITE} Update Tool
{CYAN}[3]{WHITE} About
{RED}[0]{WHITE} Exit
""")

def run_cmd(cmd):
    try:
        return subprocess.check_output(cmd, shell=True).decode().strip()
    except:
        return "N/A"

# ================================
# SYSTEM MONITOR
# ================================
def system_monitor():
    while True:
        clear()
        print(f"{YELLOW}===== SYSTEM MONITOR ====={RESET}\n")

        print(f"{CYAN}OS Info:{RESET}")
        print("OS:", platform.system())
        print("Kernel:", platform.release())
        print("Arch:", platform.machine())

        print(f"\n{CYAN}Host Info:{RESET}")
        print("Hostname:", platform.node())
        print("User:", run_cmd("whoami"))
        print("Uptime:", run_cmd("uptime -p"))

        print(f"\n{CYAN}CPU & Memory:{RESET}")
        cpu = run_cmd("grep -m1 'model name' /proc/cpuinfo | cut -d: -f2")
        print("CPU:", cpu[:60])
        print("Memory:", run_cmd("free -h | grep Mem"))

        print(f"\n{CYAN}Network:{RESET}")
        print("IP:", run_cmd("hostname -I"))
        print("Gateway:", run_cmd("ip route | grep default | awk '{print $3}'"))
        print("Public IP:", run_cmd("curl -s ifconfig.me"))

        print(f"\n{CYAN}Disk:{RESET}")
        print(run_cmd("df -h | head -5"))

        print(f"\n{CYAN}Top CPU Processes:{RESET}")
        print(run_cmd("ps aux --sort=-%cpu | head -5"))

        print(f"\n{GREEN}[R] Refresh  [B] Back{RESET}")
        choice = input(">> ").lower()
        if choice == "b":
            break

# ================================
# UPDATE TOOL
# ================================
def update_tool():
    clear()
    print(f"{PURPLE}===== UPDATE TOOL ====={RESET}\n")

    if run_cmd("which git") == "":
        print(f"{RED}Git not installed!{RESET}")
        input("Press Enter...")
        return

    repo = "https://github.com/00xk/Toolz"
    tool_dir = os.path.expanduser("~/Toolz")

    if os.path.exists(tool_dir):
        print(f"{YELLOW}Updating existing repo...{RESET}")
        os.system(f"cd {tool_dir} && git pull")
    else:
        print(f"{YELLOW}Cloning repo...{RESET}")
        os.system(f"cd ~ && git clone {repo}")

    input("\nDone. Press Enter...")

# ================================
# ABOUT
# ================================
def about():
    clear()
    print(f"""{PURPLE}
===== ABOUT TOOLZ =====

Name: Toolz
Version: 3.0
Author: 00xk

Features:
- System Monitoring
- Network Info
- Disk Usage
- Auto Update

WARNING:
Educational use only!
{RESET}
""")
    input("Press Enter...")

# ================================
# MAIN LOOP
# ================================
def main():
    while True:
        clear()
        banner()
        menu()
        choice = input(">> ")

        if choice == "1":
            system_monitor()
        elif choice == "2":
            update_tool()
        elif choice == "3":
            about()
        elif choice == "0":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice")
            time.sleep(1)

# ================================
# START
# ================================
if __name__ == "__main__":
    main()
