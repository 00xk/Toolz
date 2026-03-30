#!/usr/bin/env python3
import os
import time
import shutil

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
# 💀 MAIN LOGO
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
# 🕵️ SHERLOCK LOGO
# =========================
def sherlock_logo():
    print(f"""{PURPLE}
        ┌──────────────────────────────────────────────┐
        │                SHERLOCK OSINT                │
        └──────────────────────────────────────────────┘
{RESET}{CYAN}
              .-.
             (o o)
             | O \\
             |   |
            /|   |\\
           /_|   |_\\
             /   \\
            /_____\\

{RESET}{GREEN}        🕵️  USERNAME INVESTIGATION SYSTEM  🕵️{RESET}

{YELLOW}        > Scan usernames across 400+ sites
        > Fast OSINT lookup
        > Multi-target support{RESET}
""")

# =========================
# INSTALL SHERLOCK
# =========================
def install_sherlock():
    print(f"{YELLOW}[!] Sherlock not found. Installing...{RESET}")
    time.sleep(1)

    if os.system("python3 -m pip install sherlock-project > /dev/null 2>&1") == 0:
        print(f"{GREEN}[✓] Installed successfully!{RESET}")
    else:
        print(f"{RED}[✗] Install failed!{RESET}")
        input("Press Enter...")

# =========================
# SHERLOCK TOOL
# =========================
def sherlock_checker():
    if shutil.which("sherlock") is None:
        install_sherlock()

    while True:
        clear()
        sherlock_logo()

        print(f"""{CYAN}
┌────────────────────────────────────┐
│            SHERLOCK MENU           │
└────────────────────────────────────┘

{GREEN}[1]{WHITE} ➤ Scan Single Username
{GREEN}[2]{WHITE} ➤ Scan Multiple Usernames
{GREEN}[3]{WHITE} ➤ Back
{RESET}
""")

        choice = input(">> ")

        # SINGLE USER
        if choice == "1":
            username = input("\nEnter username: ")

            print(f"""{CYAN}
[+] Initializing Sherlock Engine...
[+] Target: {YELLOW}{username}{CYAN}
[+] Scanning platforms...
{RESET}""")
            time.sleep(1)

            os.system(f"sherlock {username}")
            input("\nPress Enter...")

        # MULTI USER
        elif choice == "2":
            path = input("\nEnter file path: ")

            if not os.path.exists(path):
                print(f"{RED}File not found!{RESET}")
                input("Press Enter...")
                continue

            with open(path, "r") as f:
                for user in f:
                    user = user.strip()
                    if user:
                        print(f"{PURPLE}═══════════════════════════════{RESET}")
                        print(f"{CYAN}[TARGET]{RESET} {YELLOW}{user}{RESET}")
                        print(f"{CYAN}[STATUS]{RESET} Scanning...\n")
                        os.system(f"sherlock {user}")

            input("\nDone. Press Enter...")

        elif choice == "3":
            break

        else:
            print(f"{RED}Invalid option{RESET}")
            time.sleep(1)

# =========================
# PHISHING (SAFE DEMO)
# =========================
def phishing():
    clear()
    print(f"""{RED}
┌────────────────────────────┐
│     PHISHING MODULE        │
└────────────────────────────┘
{RESET}""")

    print(f"{YELLOW}This is for educational purposes only!{RESET}")
    print("Learn how phishing works to protect yourself.\n")

    input("Press Enter...")

# =========================
# FORCE UPDATE
# =========================
def update():
    clear()
    print(f"{PURPLE}=== FORCE UPDATE ==={RESET}\n")

    home = os.path.expanduser("~")
    tool_dir = os.path.join(home, "Toolz")

    print(f"{YELLOW}[+] Removing old version...{RESET}")
    time.sleep(1)

    if os.path.exists(tool_dir):
        os.system(f"rm -rf {tool_dir}")

    print(f"{CYAN}[+] Downloading latest version...{RESET}")
    time.sleep(1)

    os.system(f"cd {home} && git clone https://github.com/00xk/Toolz.git")

    print(f"{GREEN}[✓] Updated successfully!{RESET}")
    time.sleep(2)

    os.system(f"cd {tool_dir} && python3 toolz.py")
    exit()

# =========================
# MAIN MENU
# =========================
def menu():
    print(f"""{CYAN}
┌────────────────────────────────────┐
│              MAIN MENU             │
└────────────────────────────────────┘

{GREEN}[1]{WHITE} Sherlock Checker
{GREEN}[2]{WHITE} Phishing (Demo)
{GREEN}[3]{WHITE} Update Tool
{RED}[4]{WHITE} Exit
{RESET}
""")

# =========================
# MAIN LOOP
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
            print(f"{RED}Invalid option{RESET}")
            time.sleep(1)

if __name__ == "__main__":
    main()
