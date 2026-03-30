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

def sherlock_logo():
    print(f"""{CYAN}
   ███████╗██╗  ██╗███████╗██████╗ ██╗      ██████╗  ██████╗██╗  ██╗
   ██╔════╝██║  ██║██╔════╝██╔══██╗██║     ██╔═══██╗██╔════╝██║ ██╔╝
   ███████╗███████║█████╗  ██████╔╝██║     ██║   ██║██║     █████╔╝ 
   ╚════██║██╔══██║██╔══╝  ██╔══██╗██║     ██║   ██║██║     ██╔═██╗ 
   ███████║██║  ██║███████╗██║  ██║███████╗╚██████╔╝╚██████╗██║  ██╗
   ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝

                🕵️ USERNAME OSINT TOOL 🕵️
{RESET}""")

def install_sherlock():
    print(f"{YELLOW}[!] Sherlock not found. Installing...{RESET}")
    time.sleep(1)

    # Try pip install
    result = os.system("pip install sherlock-project > /dev/null 2>&1")

    if result != 0:
        result = os.system("pip3 install sherlock-project > /dev/null 2>&1")

    if result == 0:
        print(f"{GREEN}[✓] Sherlock installed successfully!{RESET}")
    else:
        print(f"{RED}[✗] Failed to install Sherlock!{RESET}")
        print(f"{WHITE}Try manually: pip install sherlock-project{RESET}")
        input("Press Enter...")

def sherlock_checker():
    # Check if sherlock exists
    if os.system("which sherlock > /dev/null 2>&1") != 0:
        install_sherlock()

    while True:
        clear()
        sherlock_logo()
        print(f"""
{GREEN}[1]{WHITE} Set Username
{GREEN}[2]{WHITE} Multi Username (from file)
{GREEN}[3]{WHITE} Back
""")

        choice = input(">> ")

        # =====================
        # SINGLE USERNAME
        # =====================
        if choice == "1":
            username = input("\nEnter username: ")

            print(f"\n{CYAN}[+] Running Sherlock...{RESET}\n")
            time.sleep(1)

            # Run Sherlock
            os.system(f"sherlock {username}")

            input("\nPress Enter...")

        # =====================
        # MULTI USERNAME FILE
        # =====================
        elif choice == "2":
            filepath = input("\nEnter file path (usernames list): ")

            if not os.path.exists(filepath):
                print(f"{RED}File not found!{RESET}")
                input("Press Enter...")
                continue

            print(f"\n{CYAN}[+] Running Sherlock on list...{RESET}\n")
            time.sleep(1)

            # Loop through file
            with open(filepath, "r") as f:
                for user in f:
                    user = user.strip()
                    if user:
                        print(f"{YELLOW}Checking: {user}{RESET}")
                        os.system(f"sherlock {user}")
                        print("\n" + "-"*40)

            input("\nDone. Press Enter...")

        # =====================
        # BACK
        # =====================
        elif choice == "3":
            break

        else:
            print(f"{RED}Invalid option{RESET}")
            time.sleep(1)

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
    print(f"{PURPLE}=== FORCE UPDATE TOOL ==={RESET}\n")

    home = os.path.expanduser("~")
    tool_dir = os.path.join(home, "Toolz")
    repo = "https://github.com/00xk/Toolz.git"

    # Check git
    if os.system("which git > /dev/null") != 0:
        print(f"{RED}Git is not installed!{RESET}")
        input("Press Enter...")
        return

    print(f"{YELLOW}[+] Removing old version...{RESET}")
    time.sleep(1)

    # Remove old folder
    if os.path.exists(tool_dir):
        os.system(f"rm -rf {tool_dir}")

    print(f"{CYAN}[+] Downloading latest version...{RESET}")
    time.sleep(1)

    # Clone fresh
    os.system(f"cd {home} && git clone {repo}")

    print(f"{GREEN}[✓] Update completed successfully!{RESET}")
    print(f"{WHITE}Restarting tool...{RESET}")
    time.sleep(2)

    # Restart tool
    os.system(f"cd {tool_dir} && python3 toolz.py")

    exit()

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
