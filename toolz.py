#!/usr/bin/env python3
import os
import time
import shutil
import sys

# ══════════════════════════════════════════
#  COLOR PALETTE
# ══════════════════════════════════════════
RED    = "\033[1;31m"
GREEN  = "\033[1;32m"
YELLOW = "\033[1;33m"
CYAN   = "\033[1;36m"
WHITE  = "\033[1;37m"
PURPLE = "\033[1;35m"
ORANGE = "\033[38;5;208m"
GRAY   = "\033[1;90m"
RESET  = "\033[0m"
BOLD   = "\033[1m"
DIM    = "\033[2m"


def clear():
    os.system("clear")


# ══════════════════════════════════════════
#  SPINNER
# ══════════════════════════════════════════
def spinner(label="Scanning", duration=1.5):
    frames = ["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏"]
    end_t = time.time() + duration
    i = 0
    while time.time() < end_t:
        sys.stdout.write(f"\r  {CYAN}{frames[i % len(frames)]}  {WHITE}{label}...{RESET}")
        sys.stdout.flush()
        time.sleep(0.08)
        i += 1
    sys.stdout.write("\r" + " " * 50 + "\r")


# ══════════════════════════════════════════
#  MAIN BANNER
# ══════════════════════════════════════════
def logo():
    print(f"""{RED}
  ████████╗ ██████╗  ██████╗ ██╗     ███████╗
  ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ╚══███╔╝
     ██║   ██║   ██║██║   ██║██║       ███╔╝ 
     ██║   ██║   ██║██║   ██║██║      ███╔╝  
     ██║   ╚██████╔╝╚██████╔╝███████╗███████╗
     ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝{RESET}
{GRAY}  ─────────────────────────────────────────────{RESET}
{ORANGE}           ☠  ADVANCED HACKING TOOLKIT  ☠{RESET}
{GRAY}  ─────────────────────────────────────────────{RESET}
{DIM}          github.com/00xk/Toolz  |  v2.0{RESET}
""")


# ══════════════════════════════════════════════════════════
#  SHERLOCK LOGO — compact portrait (your smaller version)
#  Hat  = ORANGE  │  Face = YELLOW  │  Pipe = GRAY + CYAN
# ══════════════════════════════════════════════════════════
def sherlock_logo():
    H = ORANGE   # hat
    F = YELLOW   # face / body
    P = GRAY     # pipe
    A = CYAN     # pipe accent / smoke
    R = RESET

    print(f"""
{H}                      %#######                           {R}
{H}                  #################                      {R}
{H}                ######################                   {R}
{H}               #########################                 {R}
{H}             #############################               {R}
{H}             ##############################              {R}
{H}            ################################             {R}
{H}           ########################################      {R}
{H}           ######################%%#*%%%%%%#####%%%%     {R}
{H}           %#################%%#+:......:=%%%%%%%        {R}
{F}           %#############%%%#**#:.........-              {R}
{F}           %#########%%%#******-..........:              {R}
{F}            %########********+.....::..::..:-            {R}
{F}            %#######*****--***.....:-==:.....-           {R}
{F}            ########*#+....**#-...............:          {R}
{F}           #######%**#:....+#*:................:         {R}
{F}           #####%%***#-.......................::-         {R}
{F}          %%%%%#*******+:...................:::           {R}
{P}             ##***********-.................:-           {R}
{P}            ########******+.................:+           {R}
{P}           ############***+.................:#**         {R}
{P}         #################-...............::: {R}{P}#**          {R}
{P}        ###################*-.............:   {R}{P}****{R} {A}*******  {R}
{P}        %%%%%%###############*-:::........:   {R}{P}****{R} {A}******#  {R}
{P}             @@%%%%#############%*+::::::::   {R}{P}****{R} {A}******#  {R}
{P}                  %%%%%##########%%##         {R}{P}***********#{R}
{P}                      @%%%########%%#%        {R}{P}#**********#{R}
{P}                         @@%%%#####%%%        {R}{P}%###******#%{R}
{P}                             @%%####%%#          {R}{P}%######   {R}
{P}                                %%%#%%%#                   {R}
{P}                                  @%%@@%                   {R}
{P}                                    @@                     {R}
""")

    print(f"""{PURPLE}  ╔══════════════════════════════════════════════════╗
  ║        S H E R L O C K   O S I N T              ║
  ║     "When you eliminate the impossible..."       ║
  ╚══════════════════════════════════════════════════╝{RESET}

{GRAY}  ┌─  Capabilities ─────────────────────────────────────┐{RESET}
{GREEN}  │{WHITE}   ✦  Scan usernames across 400+ platforms         {GREEN}│{RESET}
{GREEN}  │{WHITE}   ✦  Multi-target batch scanning                   {GREEN}│{RESET}
{GREEN}  │{WHITE}   ✦  Export results to file                        {GREEN}│{RESET}
{GREEN}  │{WHITE}   ✦  Fast & silent OSINT reconnaissance            {GREEN}│{RESET}
{GRAY}  └────────────────────────────────────────────────────┘{RESET}
""")


# ══════════════════════════════════════════
#  INSTALL SHERLOCK
# ══════════════════════════════════════════
def install_sherlock():
    print(f"\n{YELLOW}  [!] Sherlock not found. Installing...{RESET}\n")
    for b in ["▰", "▰▰", "▰▰▰", "▰▰▰▰", "▰▰▰▰▰"]:
        sys.stdout.write(f"\r  {CYAN}  [{b:<5}]{RESET}")
        sys.stdout.flush()
        time.sleep(0.3)
    print()
    if os.system("python3 -m pip install sherlock-project -q") == 0:
        print(f"\n  {GREEN}[✔] Sherlock installed successfully!{RESET}\n")
    else:
        print(f"\n  {RED}[✘] Installation failed. Check your connection.{RESET}\n")
        input("  Press Enter to continue...")


# ══════════════════════════════════════════
#  SHERLOCK TOOL
# ══════════════════════════════════════════
def sherlock_checker():
    if shutil.which("sherlock") is None:
        install_sherlock()

    while True:
        clear()
        sherlock_logo()

        print(f"""{GRAY}  ┌─  Select Mode ──────────────────────────────┐{RESET}
  {GREEN}[1]{WHITE}   ➤  Single Username Scan                 {GRAY}│{RESET}
  {GREEN}[2]{WHITE}   ➤  Batch Scan from File                 {GRAY}│{RESET}
  {GREEN}[3]{WHITE}   ➤  Save Results to File                 {GRAY}│{RESET}
  {RED}[0]{WHITE}   ➤  Back to Main Menu                   {GRAY}│{RESET}
{GRAY}  └─────────────────────────────────────────────┘{RESET}
""")

        choice = input(f"  {CYAN}▶{RESET} ").strip()

        if choice == "1":
            username = input(f"\n  {YELLOW}Target username:{RESET} ").strip()
            if not username:
                continue
            print(f"""
  {GRAY}┌──────────────────────────────────────────┐{RESET}
  {GRAY}│{CYAN}  [TARGET] {YELLOW}{username:<32}{CYAN}{GRAY}│{RESET}
  {GRAY}│{WHITE}  [ENGINE] Sherlock OSINT                  {GRAY}│{RESET}
  {GRAY}│{WHITE}  [SITES]  400+ platforms                  {GRAY}│{RESET}
  {GRAY}└──────────────────────────────────────────┘{RESET}
""")
            spinner("Initializing engine", 1.2)
            print(f"  {GREEN}[✔] Launching scan...\n{RESET}")
            os.system(f"sherlock {username}")
            print(f"\n  {GRAY}──────────────────────────────────────────{RESET}")
            input(f"  {DIM}Press Enter to continue...{RESET}")

        elif choice == "2":
            path = input(f"\n  {YELLOW}File path:{RESET} ").strip()
            if not os.path.exists(path):
                print(f"\n  {RED}[✘] File not found: {path}{RESET}")
                input(f"  {DIM}Press Enter...{RESET}")
                continue
            with open(path, "r") as f:
                users = [u.strip() for u in f if u.strip()]
            print(f"\n  {CYAN}[+] Loaded {len(users)} target(s){RESET}\n")
            time.sleep(0.8)
            for i, user in enumerate(users, 1):
                print(f"  {PURPLE}┌──[ Target {i}/{len(users)} ]{'─'*24}┐{RESET}")
                print(f"  {PURPLE}│{RESET}  {CYAN}Username:{RESET} {YELLOW}{user}{RESET}")
                print(f"  {PURPLE}└{'─'*37}┘{RESET}\n")
                os.system(f"sherlock {user}")
                print()
            input(f"\n  {GREEN}[✔] Batch complete. Press Enter...{RESET}")

        elif choice == "3":
            username = input(f"\n  {YELLOW}Target username:{RESET} ").strip()
            if not username:
                continue
            outfile = f"{username}_results.txt"
            spinner("Scanning & saving", 1.5)
            os.system(f"sherlock {username} --output {outfile}")
            print(f"\n  {GREEN}[✔] Results saved to:{RESET} {CYAN}{outfile}{RESET}")
            input(f"  {DIM}Press Enter...{RESET}")

        elif choice == "0":
            break
        else:
            print(f"\n  {RED}[✘] Invalid option{RESET}")
            time.sleep(1)


# ══════════════════════════════════════════
#  PHISHING MODULE
# ══════════════════════════════════════════
def phishing():
    clear()
    print(f"""
  {RED}╔══════════════════════════════════════════════╗
  ║          PHISHING AWARENESS MODULE            ║
  ╚══════════════════════════════════════════════╝{RESET}

  {YELLOW}[!] For EDUCATIONAL purposes only.{RESET}
  {WHITE}    Understanding attacks helps you defend against them.{RESET}

  {GRAY}┌─  How Phishing Works ──────────────────────────┐{RESET}
  {WHITE}│  1. Attacker crafts a convincing fake page     {GRAY}│{RESET}
  {WHITE}│  2. Victim receives bait link via email/SMS    {GRAY}│{RESET}
  {WHITE}│  3. Credentials entered → silently captured   {GRAY}│{RESET}
  {WHITE}│  4. Attacker gains full unauthorized access   {GRAY}│{RESET}
  {GRAY}└────────────────────────────────────────────────┘{RESET}

  {GREEN}[Defense Tips]{RESET}
  {WHITE}  ✦  Always inspect the URL before logging in
  ✦  Enable 2FA on every important account
  ✦  Use a reputable password manager
  ✦  Never click links from unknown senders{RESET}
""")
    input(f"  {DIM}Press Enter to return...{RESET}")


# ══════════════════════════════════════════
#  FORCE UPDATE
# ══════════════════════════════════════════
def update():
    clear()
    print(f"""
  {PURPLE}╔══════════════════════════════════════════════╗
  ║               FORCE UPDATE                   ║
  ╚══════════════════════════════════════════════╝{RESET}
""")
    home     = os.path.expanduser("~")
    tool_dir = os.path.join(home, "Toolz")

    steps = [
        (f"  {YELLOW}[1/3] Removing old version...{RESET}",
         lambda: os.system(f"rm -rf {tool_dir}") if os.path.exists(tool_dir) else None),
        (f"  {CYAN}[2/3] Cloning latest release...{RESET}",
         lambda: os.system(f"cd {home} && git clone https://github.com/00xk/Toolz.git -q")),
        (f"  {GREEN}[3/3] Restarting...{RESET}", lambda: None),
    ]
    for msg, action in steps:
        print(msg)
        action()
        time.sleep(0.9)

    print(f"\n  {GREEN}[✔] Updated successfully!{RESET}\n")
    time.sleep(1.5)
    os.system(f"cd {tool_dir} && python3 toolz.py")
    sys.exit(0)


# ══════════════════════════════════════════
#  MAIN MENU
# ══════════════════════════════════════════
def menu():
    print(f"""{GRAY}  ╔═══════════════════════════════════════════════╗
  ║             M A I N   M E N U               ║
  ╚═══════════════════════════════════════════════╝{RESET}

  {GREEN}[1]{WHITE}   🔍  Sherlock OSINT Checker
  {GREEN}[2]{WHITE}   🎣  Phishing Awareness (Demo)
  {GREEN}[3]{WHITE}   🔄  Update Tool
  {RED}[0]{WHITE}   ✖   Exit
{RESET}""")


# ══════════════════════════════════════════
#  ENTRY POINT
# ══════════════════════════════════════════
def main():
    while True:
        clear()
        logo()
        menu()

        choice = input(f"  {CYAN}▶{RESET} ").strip()

        if choice == "1":
            sherlock_checker()
        elif choice == "2":
            phishing()
        elif choice == "3":
            update()
        elif choice == "0":
            clear()
            print(f"\n  {CYAN}Stay curious. Stay ethical. Goodbye 👋{RESET}\n")
            sys.exit(0)
        else:
            print(f"\n  {RED}[✘] Invalid option{RESET}")
            time.sleep(1)


if __name__ == "__main__":
    main()
