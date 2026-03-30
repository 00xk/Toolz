#!/usr/bin/env python3
import os
import time
import shutil
import sys
import re

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
PINK    = "\033[38;5;213m"
GOLD    = "\033[38;5;220m"
RESET   = "\033[0m"
BOLD    = "\033[1m"
DIM     = "\033[2m"


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
    sys.stdout.write("\r" + " " * 60 + "\r")


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
#  DIVIDER
# ══════════════════════════════════════════
def divider(color=GRAY, char="─", width=52):
    print(f"  {color}{char * width}{RESET}")


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
{DIM}       github.com/00xk/Toolz   │   v4.0   │   Linux & Termux{RESET}
""")


# ══════════════════════════════════════════════════════════
#  SHERLOCK LOGO
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
{GRAY}  ┌─  Engine ───────────────────────────────────────────────┐{RESET}
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
{LBLUE}  ██╗██████╗     ████████╗██████╗  █████╗  ██████╗███████╗██████╗
  ██║██╔══██╗    ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗
  ██║██████╔╝       ██║   ██████╔╝███████║██║     █████╗  ██████╔╝
  ██║██╔═══╝        ██║   ██╔══██╗██╔══██║██║     ██╔══╝  ██╔══██╗
  ██║██║            ██║   ██║  ██║██║  ██║╚██████╗███████╗██║  ██║
  ╚═╝╚═╝            ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚══════╝╚═╝  ╚═╝{RESET}
{GRAY}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}
{LBLUE}              🌐  IP GEOLOCATION & TRACE ENGINE{RESET}
{GRAY}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}
{GRAY}  ┌─  Reveals ──────────────────────────────────────────────┐{RESET}
{LGREEN}  │{WHITE}   ✦  Country, Region, City & ZIP                     {LGREEN}│{RESET}
{LGREEN}  │{WHITE}   ✦  ISP / Organization & AS Number                  {LGREEN}│{RESET}
{LGREEN}  │{WHITE}   ✦  Latitude & Longitude coordinates                {LGREEN}│{RESET}
{LGREEN}  │{WHITE}   ✦  Timezone & Currency info                        {LGREEN}│{RESET}
{GRAY}  └──────────────────────────────────────────────────────────┘{RESET}
""")


# ══════════════════════════════════════════
#  PHONE TRACER LOGO
# ══════════════════════════════════════════
def phone_logo():
    print(f"""
{PINK}  ██████╗ ██╗  ██╗ ██████╗ ███╗   ██╗███████╗
  ██╔══██╗██║  ██║██╔═══██╗████╗  ██║██╔════╝
  ██████╔╝███████║██║   ██║██╔██╗ ██║█████╗  
  ██╔═══╝ ██╔══██║██║   ██║██║╚██╗██║██╔══╝  
  ██║     ██║  ██║╚██████╔╝██║ ╚████║███████╗
  ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝{RESET}
{PINK}  ██████╗  ██████╗ ██╗███╗   ██╗████████╗
  ██╔══██╗██╔═══██╗██║████╗  ██║╚══██╔══╝
  ██████╔╝██║   ██║██║██╔██╗ ██║   ██║   
  ██╔═══╝ ██║   ██║██║██║╚██╗██║   ██║   
  ██║     ╚██████╔╝██║██║ ╚████║   ██║   
  ╚═╝      ╚═════╝ ╚═╝╚═╝  ╚═══╝   ╚═╝  {RESET}
{GRAY}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}
{PINK}         📱  MOBILE NUMBER OSINT ENGINE{RESET}
{GRAY}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}
{GRAY}  ┌─  What It Reveals ──────────────────────────────────┐{RESET}
{PINK}  │{WHITE}   ✦  Country, Region & Local format              {PINK}│{RESET}
{PINK}  │{WHITE}   ✦  Carrier / Network operator                  {PINK}│{RESET}
{PINK}  │{WHITE}   ✦  Line type  (mobile / landline / VoIP)       {PINK}│{RESET}
{PINK}  │{WHITE}   ✦  Number validity & international format       {PINK}│{RESET}
{PINK}  │{WHITE}   ✦  Deep scan via PhoneInfoga engine            {PINK}│{RESET}
{GRAY}  └──────────────────────────────────────────────────────┘{RESET}
""")


# ══════════════════════════════════════════
#  INSTALL HELPERS
# ══════════════════════════════════════════
def install_sherlock():
    print(f"\n{YELLOW}  [!] Sherlock not found. Installing...{RESET}\n")
    progress_bar("Installing sherlock-project", 2.0, YELLOW)
    if os.system("python3 -m pip install sherlock-project -q") == 0:
        print(f"\n  {GREEN}[✔] Sherlock installed successfully!{RESET}\n")
    else:
        print(f"\n  {RED}[✘] Installation failed. Check your connection.{RESET}\n")
        input(f"  {DIM}Press Enter to continue...{RESET}")


def install_ip_tracer():
    print(f"\n{YELLOW}  [!] IP-Tracer not found. Installing...{RESET}\n")
    home = os.path.expanduser("~")
    tracer_dir = os.path.join(home, "IP-Tracer")
    steps = [
        (f"  {CYAN}[1/3] Cloning IP-Tracer...{RESET}",
         f"git clone https://github.com/rajkumardusad/IP-Tracer.git {tracer_dir} -q"),
        (f"  {CYAN}[2/3] Setting permissions...{RESET}",
         f"chmod +x {tracer_dir}/install"),
        (f"  {CYAN}[3/3] Running installer...{RESET}",
         f"cd {tracer_dir} && sh install"),
    ]
    for msg, cmd in steps:
        print(msg)
        os.system(cmd)
        time.sleep(0.5)
    print(f"\n  {GREEN}[✔] IP-Tracer installed!{RESET}\n")
    input(f"  {DIM}Press Enter to continue...{RESET}")


def install_phoneinfoga():
    print(f"\n{YELLOW}  [!] PhoneInfoga not found. Installing...{RESET}\n")
    home = os.path.expanduser("~")
    pif_dir = os.path.join(home, "PhoneInfoga")

    steps = [
        (f"  {PINK}[1/4] Cloning PhoneInfoga...{RESET}",
         f"git clone https://github.com/ExpertAnonymous/PhoneInfoga.git {pif_dir} -q"),
        (f"  {PINK}[2/4] Setting permissions...{RESET}",
         f"chmod +x {pif_dir}/phoneinfoga.py 2>/dev/null; chmod +x {pif_dir}/*.sh 2>/dev/null; true"),
        (f"  {PINK}[3/4] Installing Python deps...{RESET}",
         f"cd {pif_dir} && python3 -m pip install -r requirements.txt -q 2>/dev/null; true"),
        (f"  {PINK}[4/4] Installing phonenumbers lib...{RESET}",
         f"python3 -m pip install phonenumbers -q"),
    ]
    for msg, cmd in steps:
        print(msg)
        os.system(cmd)
        time.sleep(0.5)

    print(f"\n  {GREEN}[✔] PhoneInfoga installed!{RESET}\n")
    input(f"  {DIM}Press Enter to continue...{RESET}")


def install_phonenumbers_lib():
    """Install the phonenumbers Python lib silently (used for quick local parse)."""
    os.system("python3 -m pip install phonenumbers -q 2>/dev/null")


# ══════════════════════════════════════════
#  QUICK LOCAL PHONE PARSE
#  Uses the `phonenumbers` library — offline
# ══════════════════════════════════════════
def quick_phone_parse(number: str):
    """
    Parse a phone number offline with the phonenumbers lib.
    Returns a dict of basic info or None if lib not available / number invalid.
    """
    try:
        import phonenumbers
        from phonenumbers import geocoder, carrier, timezone, number_type, PhoneNumberType

        parsed = phonenumbers.parse(number, None)
        if not phonenumbers.is_valid_number(parsed):
            return {"valid": False}

        ntype_map = {
            PhoneNumberType.MOBILE:          "📱 Mobile",
            PhoneNumberType.FIXED_LINE:      "☎  Landline",
            PhoneNumberType.FIXED_LINE_OR_MOBILE: "📱/☎  Mobile or Landline",
            PhoneNumberType.VOIP:            "💻 VoIP",
            PhoneNumberType.TOLL_FREE:       "🆓 Toll-Free",
            PhoneNumberType.PREMIUM_RATE:    "💰 Premium Rate",
            PhoneNumberType.SHARED_COST:     "🤝 Shared Cost",
            PhoneNumberType.PAGER:           "📟 Pager",
            PhoneNumberType.UNKNOWN:         "❓ Unknown",
        }
        ntype     = number_type(parsed)
        line_str  = ntype_map.get(ntype, "❓ Unknown")
        region    = geocoder.description_for_number(parsed, "en")
        carr      = carrier.name_for_number(parsed, "en")
        tzones    = timezone.time_zones_for_number(parsed)
        intl_fmt  = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        natl_fmt  = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.NATIONAL)
        e164_fmt  = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164)
        country_code = parsed.country_code
        national_num = parsed.national_number

        return {
            "valid":        True,
            "country_code": f"+{country_code}",
            "national":     str(national_num),
            "intl_format":  intl_fmt,
            "natl_format":  natl_fmt,
            "e164":         e164_fmt,
            "region":       region or "Unknown",
            "carrier":      carr or "Unknown",
            "line_type":    line_str,
            "timezones":    list(tzones),
        }
    except ImportError:
        return None
    except Exception:
        return {"valid": False}


def display_quick_info(info, number):
    if not info or not info.get("valid"):
        print(f"{RED}Invalid number{RESET}")
        return

    device = detect_device_info(info)
    adv = advanced_phone_analysis(info)

    print(f"""
  {GRAY}╔══════════════════════════════════════════════════════╗{RESET}
  {GRAY}║{PINK}        📱  ELITE PHONE INTEL                     {GRAY}║{RESET}
  {GRAY}╠══════════════════════════════════════════════════════╣{RESET}
  {GRAY}║ Number   {GOLD}{info['e164']:<38}{GRAY}║{RESET}
  {GRAY}║ Region   {CYAN}{info['region']:<38}{GRAY}║{RESET}
  {GRAY}║ Carrier  {YELLOW}{info['carrier']:<38}{GRAY}║{RESET}
  {GRAY}║ Type     {WHITE}{info['line_type']:<38}{GRAY}║{RESET}
  {GRAY}║ Device   {GREEN}{device:<38}{GRAY}║{RESET}
  {GRAY}║ VoIP     {RED if adv['voip']=='Yes' else GREEN}{adv['voip']:<38}{GRAY}║{RESET}
  {GRAY}║ Risk     {YELLOW}{adv['risk']:<38}{GRAY}║{RESET}
  {GRAY}╚══════════════════════════════════════════════════════╝{RESET}
""")

    social_scan(number)


# ══════════════════════════════════════════
#  SHERLOCK MODULE
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

        if choice == "1":
            username = input(f"\n  {YELLOW}Target username:{RESET} ").strip()
            if not username:
                continue
            print(f"""
  {GRAY}┌────────────────────────────────────────────────┐{RESET}
  {GRAY}│{CYAN}  [TARGET]  {YELLOW}{username:<37}{CYAN}{GRAY}│{RESET}
  {GRAY}│{WHITE}  [ENGINE]  Sherlock OSINT                     {GRAY}│{RESET}
  {GRAY}│{WHITE}  [SITES]   400+ platforms                     {GRAY}│{RESET}
  {GRAY}└────────────────────────────────────────────────┘{RESET}
""")
            spinner("Initializing Sherlock engine", 1.2, PURPLE)
            print(f"\n  {GREEN}[✔] Scan started:\n{RESET}")
            divider(GRAY)
            print()
            os.system(f"sherlock {username}")
            print()
            divider(GRAY)
            input(f"\n  {DIM}Press Enter to continue...{RESET}")

        elif choice == "2":
            path = input(f"\n  {YELLOW}File path (one username per line):{RESET} ").strip()
            if not os.path.exists(path):
                print(f"\n  {RED}[✘] File not found: {path}{RESET}")
                input(f"  {DIM}Press Enter...{RESET}")
                continue
            with open(path, "r") as f:
                users = [u.strip() for u in f if u.strip()]
            print(f"\n  {CYAN}[+] Loaded {len(users)} target(s){RESET}\n")
            time.sleep(0.6)
            for i, user in enumerate(users, 1):
                print(f"  {PURPLE}╔══[ {i}/{len(users)} ══ {YELLOW}{user}{PURPLE} ]{'═'*15}╗{RESET}")
                print(f"  {PURPLE}╚{'═'*42}╝{RESET}\n")
                os.system(f"sherlock {user}")
                print()
            input(f"\n  {GREEN}[✔] Batch complete. Press Enter...{RESET}")

        elif choice == "3":
            username = input(f"\n  {YELLOW}Target username:{RESET} ").strip()
            if not username:
                continue
            outfile = f"{username}_sherlock.txt"
            spinner("Scanning & exporting", 1.5, PURPLE)
            os.system(f"sherlock {username} --output {outfile}")
            print(f"\n  {GREEN}[✔] Saved →{RESET} {CYAN}{outfile}{RESET}")
            input(f"  {DIM}Press Enter...{RESET}")

        elif choice == "0":
            break
        else:
            print(f"\n  {RED}[✘] Invalid option{RESET}")
            time.sleep(1)


# ══════════════════════════════════════════
#  IP-TRACER MODULE
# ══════════════════════════════════════════
def ip_tracer():
    cmd = next((c for c in ["trace", "ip-tracer"] if shutil.which(c)), None)

    if cmd is None:
        clear()
        ip_tracer_logo()
        print(f"  {YELLOW}[!] IP-Tracer is not installed.{RESET}\n")
        print(f"  {GREEN}[1]{WHITE}  Auto-install   {RED}[0]{WHITE}  Back{RESET}\n")
        if input(f"  {LBLUE}▶{RESET} ").strip() == "1":
            install_ip_tracer()
            cmd = next((c for c in ["trace", "ip-tracer"] if shutil.which(c)), None)
        if cmd is None:
            return

    while True:
        clear()
        ip_tracer_logo()
        print(f"""{GRAY}  ┌─  Select Mode ────────────────────────────────────┐{RESET}
  {GREEN}[1]{WHITE}   ➤  Trace My Own IP                          {GRAY}│{RESET}
  {GREEN}[2]{WHITE}   ➤  Trace a Target IP                        {GRAY}│{RESET}
  {GREEN}[3]{WHITE}   ➤  Batch Trace from File                    {GRAY}│{RESET}
  {RED}[0]{WHITE}   ➤  Back to Main Menu                       {GRAY}│{RESET}
{GRAY}  └───────────────────────────────────────────────────┘{RESET}
""")
        choice = input(f"  {LBLUE}▶{RESET} ").strip()

        if choice == "1":
            spinner("Fetching your IP info", 1.5, LBLUE)
            print(f"\n  {LGREEN}[✔] Results:\n{RESET}")
            divider(LBLUE)
            print()
            os.system(f"{cmd} -m")
            print()
            divider(LBLUE)
            input(f"\n  {DIM}Press Enter...{RESET}")

        elif choice == "2":
            target = input(f"\n  {YELLOW}Target IP address:{RESET} ").strip()
            if not target:
                continue
            parts = target.split(".")
            if not (len(parts) == 4 and all(p.isdigit() and 0 <= int(p) <= 255 for p in parts)):
                print(f"\n  {RED}[✘] Invalid IP: use format  xxx.xxx.xxx.xxx{RESET}")
                input(f"  {DIM}Press Enter...{RESET}")
                continue
            print(f"""
  {GRAY}┌────────────────────────────────────────────────┐{RESET}
  {GRAY}│{LBLUE}  [TARGET]  {YELLOW}{target:<37}{LBLUE}{GRAY}│{RESET}
  {GRAY}│{WHITE}  [ENGINE]  IP-Tracer via ip-api.com           {GRAY}│{RESET}
  {GRAY}└────────────────────────────────────────────────┘{RESET}
""")
            spinner(f"Tracing {target}", 1.5, LBLUE)
            print(f"\n  {LGREEN}[✔] Results:\n{RESET}")
            divider(LBLUE)
            print()
            os.system(f"{cmd} -t {target}")
            print()
            divider(LBLUE)
            input(f"\n  {DIM}Press Enter...{RESET}")

        elif choice == "3":
            path = input(f"\n  {YELLOW}File path (one IP per line):{RESET} ").strip()
            if not os.path.exists(path):
                print(f"\n  {RED}[✘] File not found: {path}{RESET}")
                input(f"  {DIM}Press Enter...{RESET}")
                continue
            with open(path, "r") as f:
                ips = [l.strip() for l in f if l.strip()]
            print(f"\n  {CYAN}[+] Loaded {len(ips)} IP(s){RESET}\n")
            for i, ip in enumerate(ips, 1):
                print(f"  {LBLUE}╔══[ {i}/{len(ips)} ══ {YELLOW}{ip}{LBLUE} ]{'═'*10}╗{RESET}")
                print(f"  {LBLUE}╚{'═'*36}╝{RESET}\n")
                os.system(f"{cmd} -t {ip}")
                print()
                time.sleep(0.4)
            input(f"\n  {LGREEN}[✔] Batch done. Press Enter...{RESET}")

        elif choice == "0":
            break
        else:
            print(f"\n  {RED}[✘] Invalid option{RESET}")
            time.sleep(1)

def detect_device_info(info):
    carrier = (info.get("carrier") or "").lower()
    region = (info.get("region") or "").lower()

    if any(x in carrier for x in ["etisalat","vodafone","orange"]):
        return "🤖 Android (likely)"
    if any(x in region for x in ["usa","uk"]):
        return "🍎 iPhone (likely)"
    return "❓ Unknown"


def advanced_phone_analysis(info):
    carrier = (info.get("carrier") or "").lower()
    line = info.get("line_type","")

    voip = "Yes" if "voip" in line.lower() else "No"
    risk = "🟢 Low" if "mobile" in line.lower() else "🟡 Medium"

    return {"voip":voip,"risk":risk}


def social_scan(number):
    print(f"\n  {CYAN}[ SOCIAL ]{RESET}")
    print(f"  WhatsApp: https://wa.me/{number.replace('+','')}")
    print(f"  Telegram: https://t.me/{number.replace('+','')}")
# ══════════════════════════════════════════
#  PHONE NUMBER OSINT MODULE
# ══════════════════════════════════════════
def phone_tracer():
    # Silently try to ensure phonenumbers lib is available
    try:
        import phonenumbers  # noqa
    except ImportError:
        install_phonenumbers_lib()

    # Locate PhoneInfoga script
    home    = os.path.expanduser("~")
    pif_dir = os.path.join(home, "PhoneInfoga")
    pif_py  = os.path.join(pif_dir, "phoneinfoga.py")
    pif_installed = os.path.isfile(pif_py)

    while True:
        clear()
        phone_logo()

        print(f"""{GRAY}  ┌─  Select Mode ────────────────────────────────────┐{RESET}
  {GREEN}[1]{WHITE}   ➤  Quick Scan    (offline — instant)         {GRAY}│{RESET}
  {GREEN}[2]{WHITE}   ➤  Deep Scan     (PhoneInfoga — full OSINT)  {GRAY}│{RESET}
  {GREEN}[3]{WHITE}   ➤  Full Scan     (Quick + Deep combined)     {GRAY}│{RESET}
  {GREEN}[4]{WHITE}   ➤  Batch Scan    (file of numbers)           {GRAY}│{RESET}
  {GOLD}[5]{WHITE}   ➤  Install / Reinstall PhoneInfoga           {GRAY}│{RESET}
  {RED}[0]{WHITE}   ➤  Back to Main Menu                       {GRAY}│{RESET}
{GRAY}  └───────────────────────────────────────────────────┘{RESET}
""")
        choice = input(f"  {PINK}▶{RESET} ").strip()

        # ── Quick scan ──
        if choice == "1":
            number = input(f"\n  {YELLOW}Phone number {DIM}(with country code, e.g. +971501234567){RESET}{YELLOW}:{RESET} ").strip()
            if not number:
                continue
            # Normalize — add + if missing but starts with digits
            if not number.startswith("+") and number[0].isdigit():
                number = "+" + number
            spinner("Parsing number", 0.8, PINK)
            info = quick_phone_parse(number)
            display_quick_info(info, number)
            input(f"  {DIM}Press Enter to continue...{RESET}")

        # ── Deep scan ──
        elif choice == "2":
            if not pif_installed:
                print(f"\n  {YELLOW}[!] PhoneInfoga not found.{RESET}")
                print(f"  {DIM}    Select option [5] to install it first.{RESET}\n")
                input(f"  {DIM}Press Enter...{RESET}")
                continue
            number = input(f"\n  {YELLOW}Phone number {DIM}(with country code, e.g. +971501234567){RESET}{YELLOW}:{RESET} ").strip()
            if not number:
                continue
            if not number.startswith("+"):
                number = "+" + number
            print(f"""
  {GRAY}┌────────────────────────────────────────────────┐{RESET}
  {GRAY}│{PINK}  [TARGET]  {GOLD}{number:<37}{PINK}{GRAY}│{RESET}
  {GRAY}│{WHITE}  [ENGINE]  PhoneInfoga + Search Fingerprint  {GRAY}│{RESET}
  {GRAY}│{WHITE}  [MODE]    Deep OSINT scan                   {GRAY}│{RESET}
  {GRAY}└────────────────────────────────────────────────┘{RESET}
""")
            spinner("Launching PhoneInfoga deep scan", 1.5, PINK)
            print(f"\n  {LGREEN}[✔] Scanning...\n{RESET}")
            divider(PINK)
            print()
            os.system(f"python3 {pif_py} -n {number}")
            print()
            divider(PINK)
            input(f"\n  {DIM}Press Enter to continue...{RESET}")

        # ── Full scan (quick + deep) ──
        elif choice == "3":
            number = input(f"\n  {YELLOW}Phone number {DIM}(with country code, e.g. +971501234567){RESET}{YELLOW}:{RESET} ").strip()
            if not number:
                continue
            if not number.startswith("+"):
                number = "+" + number
            # Step 1 — Quick parse
            spinner("Quick parse (offline)", 0.8, PINK)
            info = quick_phone_parse(number)
            display_quick_info(info, number)
            if info and info.get("valid") is False:
                input(f"  {DIM}Press Enter...{RESET}")
                continue
            # Step 2 — Deep scan
            if not pif_installed:
                print(f"\n  {YELLOW}[~] PhoneInfoga not installed — skipping deep scan.{RESET}")
                print(f"  {DIM}    Use option [5] to install it.{RESET}\n")
            else:
                print(f"\n  {PINK}[ PHASE 2 ]  PhoneInfoga deep scan...{RESET}\n")
                spinner("Launching PhoneInfoga", 1.2, PINK)
                print(f"\n  {LGREEN}[✔] Results:\n{RESET}")
                divider(PINK)
                print()
                os.system(f"python3 {pif_py} -n {number}")
                print()
                divider(PINK)
            input(f"\n  {DIM}Press Enter to continue...{RESET}")

        # ── Batch ──
        elif choice == "4":
            path = input(f"\n  {YELLOW}File path {DIM}(one number per line, with country code){RESET}{YELLOW}:{RESET} ").strip()
            if not os.path.exists(path):
                print(f"\n  {RED}[✘] File not found: {path}{RESET}")
                input(f"  {DIM}Press Enter...{RESET}")
                continue
            with open(path, "r") as f:
                numbers = [l.strip() for l in f if l.strip()]
            print(f"\n  {CYAN}[+] Loaded {len(numbers)} number(s){RESET}\n")
            time.sleep(0.5)
            for i, num in enumerate(numbers, 1):
                if not num.startswith("+"):
                    num = "+" + num
                print(f"  {PINK}╔══[ Number {i}/{len(numbers)} ══ {GOLD}{num}{PINK} ]{'═'*5}╗{RESET}")
                print(f"  {PINK}╚{'═'*42}╝{RESET}")
                info = quick_phone_parse(num)
                display_quick_info(info, num)
                if pif_installed and info and info.get("valid") is not False:
                    print(f"  {DIM}Running deep scan...{RESET}\n")
                    os.system(f"python3 {pif_py} -n {num}")
                divider(PINK, "─", 52)
                print()
                time.sleep(0.3)
            input(f"\n  {LGREEN}[✔] Batch complete. Press Enter...{RESET}")

        # ── Install ──
        elif choice == "5":
            install_phoneinfoga()
            # Refresh pif_installed flag
            pif_installed = os.path.isfile(pif_py)

        elif choice == "0":
            break
        else:
            print(f"\n  {RED}[✘] Invalid option{RESET}")
            time.sleep(1)

def install_twilio():
    os.system("python3 -m pip install twilio -q")


def sms_sender():
    try:
        from twilio.rest import Client
    except:
        install_twilio()
        from twilio.rest import Client

    clear()
    print(f"{CYAN}=== SMS TEST SYSTEM ==={RESET}\n")

    sid = input("SID: ")
    token = input("TOKEN: ")
    from_num = input("FROM (Twilio): ")
    to = input("TO: ")
    msg = input("MESSAGE: ")

    try:
        client = Client(sid, token)
        m = client.messages.create(body=msg, from_=from_num, to=to)
        print(f"{GREEN}Sent! SID: {m.sid}{RESET}")
    except Exception as e:
        print(f"{RED}Error: {e}{RESET}")

    input("\nPress Enter...")
# ══════════════════════════════════════════
#  FORCE UPDATE
# ══════════════════════════════════════════
def update():
    clear()
    print(f"""
  {PURPLE}╔══════════════════════════════════════════════════╗
  ║            F O R C E   U P D A T E              ║
  ╚══════════════════════════════════════════════════╝{RESET}
""")
    home     = os.path.expanduser("~")
    tool_dir = os.path.join(home, "Toolz")
    steps = [
        (f"  {YELLOW}[1/3] Removing old installation...{RESET}",
         lambda: os.system(f"rm -rf {tool_dir}") if os.path.exists(tool_dir) else None),
        (f"  {CYAN}[2/3] Cloning latest version...{RESET}",
         lambda: os.system(f"cd {home} && git clone https://github.com/00xk/Toolz.git -q")),
        (f"  {GREEN}[3/3] Finalizing...{RESET}",
         lambda: None),
    ]
    for msg, action in steps:
        print(msg)
        action()
        time.sleep(0.9)
    print(f"\n  {GREEN}[✔] Toolz updated!{RESET}\n")
    time.sleep(1.5)
    os.system(f"cd {tool_dir} && python3 toolz.py")
    sys.exit(0)


# ══════════════════════════════════════════
#  MAIN MENU
# ══════════════════════════════════════════
def menu():
    print(f"""{GRAY}  ╔═══════════════════════════════════════════════════════╗
  ║               M A I N   M E N U                    ║
  ╠═══════════════════════════════════════════════════════╣

  {GREEN}[1]{WHITE} Sherlock OSINT
  {LBLUE}[2]{WHITE} IP Tracer
  {PINK}[3]{WHITE} Phone OSINT
  {CYAN}[4]{WHITE} SMS Sender
  {PURPLE}[5]{WHITE} Update Tool
  {RED}[0]{WHITE} Exit

  ╚═══════════════════════════════════════════════════════╝{RESET}
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
            phone_tracer()
        elif choice == "4":
            sms_sender()
        elif choice == "5":
            update()
        elif choice == "0":
            clear()
            print(f"\n  {CYAN}Stay curious. Stay ethical.{RESET}  {DIM}Goodbye 👋{RESET}\n")
            sys.exit(0)
        else:
            print(f"\n  {RED}[✘] Invalid option. Choose 0–4.{RESET}")
            time.sleep(1)


if __name__ == "__main__":
    main()
