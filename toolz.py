#!/usr/bin/env python3
import os
import time
import subprocess

# Colors
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
CYAN = "\033[1;36m"
WHITE = "\033[1;37m"
PURPLE = "\033[1;35m"
RESET = "\033[0m"

def clear():
    os.system("clear")

# =========================
# 💀 LOGO
# =========================
def logo():
    print(f"""{RED}
        ████████╗ ██████╗  ██████╗ ██╗     ███████╗
        ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ╚══███╔╝
           ██║   ██║   ██║██║   ██║██║       ███╔╝
           ██║   ██║   ██║██║   ██║██║      ███╔╝
           ██║   ╚██████╔╝╚██████╔╝███████╗███████╗
           ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝

              ☠️  ADVANCED HACKING TOOL ☠️
{RESET}""")

# =========================
# 🕵️ Sherlock Checker
# =========================
def sherlock_checker():
    clear()
    print(f"{CYAN}=== Sherlock Username Checker ==={RESET}\n")

    username = input("Enter username: ")

    print(f"\n{YELLOW}Searching for '{username}'...{RESET}\n")
    time.sleep(1)

    # Fake demo results (safe)
    sites = ["Instagram", "Twitter", "GitHub", "TikTok"]

    for site in sites:
        print(f"{GREEN}[FOUND]{RESET} {site}: https://{site.lower()}.com/{username}")
        time.sleep(0.3)

    input("\nPress Enter...")

# =========================
# 🎣 Phishing (SAFE DEMO)
# =========================
def phishing():
    clear()
    print(f"{RED}=== Phishing Module (EDUCATIONAL) ==={RESET}\n")

    print(f"{YELLOW}This is a demo for awareness only.{RESET}")
    print("Learn how phishing works to protect yourself.\n")

    print(f"{CYAN}Example:{RESET}")
    print("Fake login pages try to steal credentials.\n")

    input("Press Enter...")

# =========================
# 🔄 Update
# =========================
def update():
    clear()
    print(f"{PURPLE}=== Updating Tool ==={RESET}\n")

    if os.system("which git > /dev/null") != 0:
        print(f"{RED}Git not installed!{RESET}")
        input("Press Enter...")
        return

    os.system("git pull")
    input("\nUpdated. Press Enter...")

# =========================
# 📋 MENU
# =========================
def menu():
    print(f"""
{GREEN}[1]{WHITE} Sherlock Checker
{GREEN}[2]{WHITE} Phishing (Demo)
{GREEN}[3]{WHITE} Update
{RED}[4]{WHITE} Exit
""")

# =========================
# 🚀 MAIN
# =========================
def main():
    while True:
        clear()
        logo()
        menu()

        choice = input(">> ")

        if choice == "1":
            sherlock_checker()
        elif choice == "2":
            phishing()
        elif choice == "3":
            update()
        elif choice == "4":
            print("Goodbye 👋")
            break
        else:
            print("Invalid option")
            time.sleep(1)

if __name__ == "__main__":
    main()
