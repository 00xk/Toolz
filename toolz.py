#!/usr/bin/env python3
import os
import time
import shutil
import sys
import subprocess

# ══════════════════════════════════════════
#  COLOR PALETTE
# ══════════════════════════════════════════
RED     = "\033[1;31m"
GREEN   = "\033[1;32m"
YELLOW  = "\033[1;33m"
CYAN    = "\033[1;36m"
WHITE   = "\033[1;37m"
PURPLE  = "\033[1;35m"
ORANGE  = "\033[38;5;208m"
GRAY    = "\033[1;90m"
LBLUE   = "\033[38;5;39m"
LGREEN  = "\033[38;5;82m"
RESET   = "\033[0m"
BOLD    = "\033[1m"
DIM     = "\033[2m"
BLINK   = "\033[5m"


def clear():
    os.system("clear")


# ══════════════════════════════════════════
#  SPINNER
# ══════════════════════════════════════════
def spinner(label="Processing", duration=1.5, color=CYAN):
    frames = ["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏"]
    end_t = time.time() + duration
    i = 0
    while time.time() < end_t:
        sys.stdout.write(f"\r  {color}{frames[i % len(frames)]}{RESET}  {WHITE}{label}...{RESET}")
        sys.stdout.flush()
        time.sleep(0.08)
        i += 1
    sys.stdout.write("\r" + " " * 55 + "\r")


# ══════════════════════════════════════════
#  PROGRESS BAR
# ══════════════════════════════════════════
def progress_bar(label="Loading", duration=1.5, color=CYAN):
    width = 30
    steps = 20
    for i in range(steps + 1):
        filled = int(width * i / steps)
        bar = "█" * filled + "░" * (width - filled)
        pct = int(100 * i / steps)
        sys.stdout.write(f"\r  {color}[{bar}]{RESET} {WHITE}{pct:3d}%{RESET}  {DIM}{label}{RESET}")
        sys.stdout.flush()
        time.sleep(duration / steps)
    print()


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
{GRAY}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}
{ORANGE}       ☠   A D V A N C E D   T O O L K I T   ☠{RESET}
{GRAY}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}
{DIM}       github.com/00xk/Toolz   │   v3.0   │   Linux & Termux{RESET}
""")


# ══════════════════════════════════════════════════════════
#  SHERLOCK LOGO — compact portrait
#  Hat = ORANGE │ Face = YELLOW │ Pipe = GRAY + CYAN
# ══════════════════════════════════════════════════════════
def sherlock_logo():
    H = ORANGE
    F = YELLOW
    P = GRAY
    A = CYAN
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

    print(f"""{PURPLE}  ╔══════════════════════════════════════════════════════╗
  ║          S H E R L O C K   O S I N T              ║
  ║       "When you eliminate the impossible..."       ║
  ╚══════════════════════════════════════════════════════╝{RESET}
{GRAY}  ┌─  Engine Info ──────────────────────────────────────────┐{RESET}
{GREEN}  │{WHITE}   ✦  400+ platforms scanned simultaneously          {GREEN}│{RESET}
{GREEN}  │{WHITE}   ✦  Multi-target batch mode supported              {GREEN}│{RESET}
{GREEN}  │{WHITE}   ✦  Export results to .txt file                    {GREEN}│{RESET}
{GRAY}  └──────────────────────────────────────────────────────┘{RESET}
""")


# ══════════════════════════════════════════
#  IP-TRACER LOGO
# ══════════════════════════════════════════
def ip_tracer_logo():
    print(f"""
{LBLUE}   ██╗██████╗     ████████╗██████╗  █████╗  ██████╗███████╗██████╗
   ██║██╔══██╗    ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗
   ██║██████╔╝       ██║   ██████╔╝███████║██║     █████╗  ██████╔╝
   ██║██╔═══╝        ██║   ██╔══██╗██╔══██║██║     ██╔══╝  ██╔══██╗
   ██║██║            ██║   ██║  ██║██║  ██║╚██████╗███████╗██║  ██║
   ╚═╝╚═╝            ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚══════╝╚═╝  ╚═╝{RESET}

{GRAY}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}
{LBLUE}              🌐  IP GEOLOCATION & TRACE ENGINE{RESET}
{GRAY}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}

{GRAY}  ┌─  What It Reveals ──────────────────────────────────────────┐{RESET}
{LGREEN}  │{WHITE}   ✦  Country, Region, City & ZIP                     {LGREEN}│{RESET}
{LGREEN}  │{WHITE}   ✦  ISP / Organization name                         {LGREEN}│{RESET}
{LGREEN}  │{WHITE}   ✦  Latitude & Longitude coordinates                {LGREEN}│{RESET}
{LGREEN}  │{WHITE}   ✦  Timezone & Currency info                        {LGREEN}│{RESET}
{LGREEN}  │{WHITE}   ✦  AS Number & reverse lookup                      {LGREEN}│{RESET}
{GRAY}  └──────────────────────────────────────────────────────────┘{RESET}
""")


# ══════════════════════════════════════════
#  INSTALL SHERLOCK
# ══════════════════════════════════════════
def install_sherlock():
    print(f"\n{YELLOW}  [!] Sherlock not found. Installing...{RESET}\n")
    progress_bar("Installing sherlock-project", 2.0, YELLOW)
    if os.system("python3 -m pip install sherlock-project -q") == 0:
        print(f"\n  {GREEN}[✔] Sherlock installed successfully!{RESET}\n")
    else:
        print(f"\n  {RED}[✘] Installation failed. Check your connection.{RESET}\n")
        input(f"  {DIM}Press Enter to continue...{RESET}")


# ══════════════════════════════════════════
#  INSTALL IP-TRACER
# ══════════════════════════════════════════
def install_ip_tracer():
    print(f"\n{YELLOW}  [!] IP-Tracer not found. Installing...{RESET}\n")
    home = os.path.expanduser("~")
    tracer_dir = os.path.join(home, "IP-Tracer")

    steps = [
        (f"  {CYAN}[1/3] Cloning IP-Tracer repository...{RESET}",
         f"git clone https://github.com/rajkumardusad/IP-Tracer.git {tracer_dir} -q"),
        (f"  {CYAN}[2/3] Setting permissions...{RESET}",
         f"chmod +x {tracer_dir}/install"),
        (f"  {CYAN}[3/3] Running installer...{RESET}",
         f"cd {tracer_dir} && sh install"),
    ]

    for msg, cmd in steps:
        print(msg)
        ret = os.system(cmd)
        time.sleep(0.5)
        if ret != 0:
            print(f"\n  {RED}[✘] Step failed. You may need to run manually:{RESET}")
            print(f"  {DIM}{cmd}{RESET}\n")

    if shutil.which("trace") or shutil.which("ip-tracer"):
        print(f"\n  {GREEN}[✔] IP-Tracer installed successfully!{RESET}\n")
    else:
        print(f"\n  {YELLOW}[~] IP-Tracer installed but 'trace' not in PATH.{RESET}")
        print(f"  {DIM}Try: export PATH=$PATH:~/.local/bin or restart terminal.{RESET}\n")

    input(f"  {DIM}Press Enter to continue...{RESET}")


# ══════════════════════════════════════════
#  SHERLOCK TOOL
# ══════════════════════════════════════════
def sherlock_checker():
    if shutil.which("sherlock") is None:
        install_sherlock()

    while True:
        clear()
        sherlock_logo()

        print(f"""{GRAY}  ┌─  Select Mode ────────────────────────────────────┐{RESET}
  {GREEN}[1]{WHITE}   ➤  Single Username Scan                     {GRAY}│{RESET}
  {GREEN}[2]{WHITE}   ➤  Batch Scan from File                     {GRAY}│{RESET}
  {GREEN}[3]{WHITE}   ➤  Scan & Save Results to File              {GRAY}│{RESET}
  {RED}[0]{WHITE}   ➤  Back to Main Menu                       {GRAY}│{RESET}
{GRAY}  └───────────────────────────────────────────────────┘{RESET}
""")
        choice = input(f"  {CYAN}▶{RESET} ").strip()

        # ── Single ──
        if choice == "1":
            username = input(f"\n  {YELLOW}Target username:{RESET} ").strip()
            if not username:
                continue
            print(f"""
  {GRAY}┌────────────────────────────────────────────────┐{RESET}
  {GRAY}│{CYAN}  [TARGET]  {YELLOW}{username:<37}{CYAN}{GRAY}│{RESET}
  {GRAY}│{WHITE}  [ENGINE]  Sherlock OSINT v2.x               {GRAY}│{RESET}
  {GRAY}│{WHITE}  [SITES]   400+ platforms                    {GRAY}│{RESET}
  {GRAY}└────────────────────────────────────────────────┘{RESET}
""")
            spinner("Initializing Sherlock engine", 1.2, PURPLE)
            print(f"\n  {GREEN}[✔] Scan started — results below:\n{RESET}")
            print(f"  {GRAY}{'─'*50}{RESET}\n")
            os.system(f"sherlock {username}")
            print(f"\n  {GRAY}{'─'*50}{RESET}")
            input(f"\n  {DIM}Press Enter to continue...{RESET}")

        # ── Batch ──
        elif choice == "2":
            path = input(f"\n  {YELLOW}File path (one username per line):{RESET} ").strip()
            if not os.path.exists(path):
                print(f"\n  {RED}[✘] File not found: {path}{RESET}")
                input(f"  {DIM}Press Enter...{RESET}")
                continue
            with open(path, "r") as f:
                users = [u.strip() for u in f if u.strip()]
            print(f"\n  {CYAN}[+] Loaded {len(users)} target(s) from file{RESET}\n")
            time.sleep(0.8)
            for i, user in enumerate(users, 1):
                print(f"  {PURPLE}╔══[ Target {i}/{len(users)} ══ {YELLOW}{user}{PURPLE} ]{'═'*10}╗{RESET}")
                print(f"  {PURPLE}║{RESET}  {DIM}Scanning 400+ platforms...{RESET}")
                print(f"  {PURPLE}╚{'═'*42}╝{RESET}\n")
                os.system(f"sherlock {user}")
                print()
            input(f"\n  {GREEN}[✔] Batch scan complete. Press Enter...{RESET}")

        # ── Save ──
        elif choice == "3":
            username = input(f"\n  {YELLOW}Target username:{RESET} ").strip()
            if not username:
                continue
            outfile = f"{username}_sherlock.txt"
            spinner("Scanning & exporting results", 1.5, PURPLE)
            os.system(f"sherlock {username} --output {outfile}")
            print(f"\n  {GREEN}[✔] Results saved →{RESET} {CYAN}{outfile}{RESET}")
            input(f"  {DIM}Press Enter...{RESET}")

        elif choice == "0":
            break
        else:
            print(f"\n  {RED}[✘] Invalid option{RESET}")
            time.sleep(1)


# ══════════════════════════════════════════
#  IP-TRACER TOOL
# ══════════════════════════════════════════
def ip_tracer():
    # Detect available command (trace or ip-tracer)
    cmd = None
    for c in ["trace", "ip-tracer"]:
        if shutil.which(c):
            cmd = c
            break

    if cmd is None:
        clear()
        ip_tracer_logo()
        print(f"  {YELLOW}[!] IP-Tracer is not installed on this system.{RESET}\n")
        print(f"  {GRAY}┌─  Install Options ──────────────────────────────┐{RESET}")
        print(f"  {GREEN}│{WHITE}  [1]  Auto-install (git clone + sh install)    {GREEN}│{RESET}")
        print(f"  {RED}│{WHITE}  [0]  Back to Main Menu                        {RED}│{RESET}")
        print(f"  {GRAY}└────────────────────────────────────────────────┘{RESET}\n")
        opt = input(f"  {CYAN}▶{RESET} ").strip()
        if opt == "1":
            install_ip_tracer()
            # Re-detect after install
            for c in ["trace", "ip-tracer"]:
                if shutil.which(c):
                    cmd = c
                    break
            if cmd is None:
                return
        else:
            return

    while True:
        clear()
        ip_tracer_logo()

        print(f"""{GRAY}  ┌─  Select Mode ────────────────────────────────────┐{RESET}
  {GREEN}[1]{WHITE}   ➤  Trace My Own IP Address                  {GRAY}│{RESET}
  {GREEN}[2]{WHITE}   ➤  Trace a Target IP Address                {GRAY}│{RESET}
  {GREEN}[3]{WHITE}   ➤  Trace Multiple IPs from File             {GRAY}│{RESET}
  {RED}[0]{WHITE}   ➤  Back to Main Menu                       {GRAY}│{RESET}
{GRAY}  └───────────────────────────────────────────────────┘{RESET}
""")
        choice = input(f"  {LBLUE}▶{RESET} ").strip()

        # ── My IP ──
        if choice == "1":
            print(f"""
  {GRAY}┌────────────────────────────────────────────────┐{RESET}
  {GRAY}│{LBLUE}  [MODE]    Self IP Trace                      {GRAY}│{RESET}
  {GRAY}│{WHITE}  [SOURCE]  ip-api.com                         {GRAY}│{RESET}
  {GRAY}└────────────────────────────────────────────────┘{RESET}
""")
            spinner("Fetching your IP information", 1.5, LBLUE)
            print(f"\n  {LGREEN}[✔] Results:\n{RESET}")
            print(f"  {GRAY}{'─'*50}{RESET}\n")
            os.system(f"{cmd} -m")
            print(f"\n  {GRAY}{'─'*50}{RESET}")
            input(f"\n  {DIM}Press Enter to continue...{RESET}")

        # ── Target IP ──
        elif choice == "2":
            target = input(f"\n  {YELLOW}Enter target IP address:{RESET} ").strip()
            if not target:
                continue

            # Basic validation
            parts = target.split(".")
            valid = len(parts) == 4 and all(p.isdigit() and 0 <= int(p) <= 255 for p in parts)
            if not valid:
                print(f"\n  {RED}[✘] Invalid IP format. Use: xxx.xxx.xxx.xxx{RESET}")
                input(f"  {DIM}Press Enter...{RESET}")
                continue

            print(f"""
  {GRAY}┌────────────────────────────────────────────────┐{RESET}
  {GRAY}│{LBLUE}  [TARGET]  {YELLOW}{target:<37}{LBLUE}{GRAY}│{RESET}
  {GRAY}│{WHITE}  [ENGINE]  IP-Tracer via ip-api.com           {GRAY}│{RESET}
  {GRAY}│{WHITE}  [DATA]    Geo · ISP · ASN · Timezone         {GRAY}│{RESET}
  {GRAY}└────────────────────────────────────────────────┘{RESET}
""")
            spinner(f"Tracing {target}", 1.5, LBLUE)
            print(f"\n  {LGREEN}[✔] Trace complete — results below:\n{RESET}")
            print(f"  {GRAY}{'─'*50}{RESET}\n")
            os.system(f"{cmd} -t {target}")
            print(f"\n  {GRAY}{'─'*50}{RESET}")
            input(f"\n  {DIM}Press Enter to continue...{RESET}")

        # ── Batch IPs ──
        elif choice == "3":
            path = input(f"\n  {YELLOW}File path (one IP per line):{RESET} ").strip()
            if not os.path.exists(path):
                print(f"\n  {RED}[✘] File not found: {path}{RESET}")
                input(f"  {DIM}Press Enter...{RESET}")
                continue

            with open(path, "r") as f:
                ips = [line.strip() for line in f if line.strip()]

            print(f"\n  {CYAN}[+] Loaded {len(ips)} IP(s) from file{RESET}\n")
            time.sleep(0.6)

            for i, ip in enumerate(ips, 1):
                print(f"  {LBLUE}╔══[ IP {i}/{len(ips)} ══ {YELLOW}{ip}{LBLUE} ]{'═'*15}╗{RESET}")
                print(f"  {LBLUE}║{RESET}  {DIM}Tracing...{RESET}")
                print(f"  {LBLUE}╚{'═'*42}╝{RESET}\n")
                os.system(f"{cmd} -t {ip}")
                print()
                time.sleep(0.3)  # avoid rate-limiting ip-api

            input(f"\n  {LGREEN}[✔] Batch trace complete. Press Enter...{RESET}")

        elif choice == "0":
            break
        else:
            print(f"\n  {RED}[✘] Invalid option{RESET}")
            time.sleep(1)


# ══════════════════════════════════════════
#  FORCE UPDATE
# ══════════════════════════════════════════
def update():
    clear()
    print(f"""
  {PURPLE}╔══════════════════════════════════════════════════╗
  ║              F O R C E   U P D A T E             ║
  ╚══════════════════════════════════════════════════╝{RESET}
""")
    home     = os.path.expanduser("~")
    tool_dir = os.path.join(home, "Toolz")

    steps = [
        (f"  {YELLOW}[1/3] Removing old installation...{RESET}",
         lambda: os.system(f"rm -rf {tool_dir}") if os.path.exists(tool_dir) else None),
        (f"  {CYAN}[2/3] Pulling latest version from GitHub...{RESET}",
         lambda: os.system(f"cd {home} && git clone https://github.com/00xk/Toolz.git -q")),
        (f"  {GREEN}[3/3] Finalizing...{RESET}", lambda: None),
    ]
    for msg, action in steps:
        print(msg)
        action()
        time.sleep(0.9)

    print(f"\n  {GREEN}[✔] Toolz updated to latest version!{RESET}\n")
    time.sleep(1.5)
    os.system(f"cd {tool_dir} && python3 toolz.py")
    sys.exit(0)


# ══════════════════════════════════════════
#  MAIN MENU
# ══════════════════════════════════════════
def menu():
    print(f"""{GRAY}  ╔═══════════════════════════════════════════════════╗
  ║              M A I N   M E N U                 ║
  ╠═══════════════════════════════════════════════════╣
  ║                                                 ║
  ║   {GREEN}[1]{WHITE}   🔍  Sherlock OSINT  — Username Hunt       {GRAY}║
  ║   {LBLUE}[2]{WHITE}   🌐  IP Tracer       — Geolocation         {GRAY}║
  ║   {PURPLE}[3]{WHITE}   🔄  Update Tool     — Pull Latest         {GRAY}║
  ║   {RED}[0]{WHITE}   ✖   Exit                                {GRAY}║
  ║                                                 ║
  ╚═══════════════════════════════════════════════════╝{RESET}
""")


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
            ip_tracer()
        elif choice == "3":
            update()
        elif choice == "0":
            clear()
            print(f"\n  {CYAN}Stay curious. Stay ethical.{RESET}  {DIM}Goodbye 👋{RESET}\n")
            sys.exit(0)
        else:
            print(f"\n  {RED}[✘] Invalid option. Choose 0–3.{RESET}")
            time.sleep(1)


if __name__ == "__main__":
    main()
