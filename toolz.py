#!/usr/bin/env python3
# ╔══════════════════════════════════════════════════════════════╗
# ║                  T O O L Z  v6.0                            ║
# ║         Advanced OSINT & Utility Toolkit                    ║
# ║         Linux & Termux  |  github.com/00xk/Toolz            ║
# ╚══════════════════════════════════════════════════════════════╝

import os, sys, time, shutil

# ─────────────────────────────────────────────────────────────
#  COLORS
# ─────────────────────────────────────────────────────────────
R   = "\033[0m"
BD  = "\033[1m"
DIM = "\033[2m"
K   = "\033[1;90m"      # dark gray
W   = "\033[1;37m"      # white
RE  = "\033[1;31m"      # red
GR  = "\033[1;32m"      # green
YL  = "\033[1;33m"      # yellow
CY  = "\033[1;36m"      # cyan
PU  = "\033[1;35m"      # purple
OR  = "\033[38;5;208m"  # orange
LB  = "\033[38;5;39m"   # light blue
LG  = "\033[38;5;82m"   # light green
PK  = "\033[38;5;213m"  # pink
GD  = "\033[38;5;220m"  # gold


# ─────────────────────────────────────────────────────────────
#  CORE UTILITIES
# ─────────────────────────────────────────────────────────────
def clr():
    os.system("clear")

def pause(msg="Press Enter to continue..."):
    input(f"\n  {DIM}{msg}{R}")

def ln(c=K, ch="─", w=56):
    print(f"  {c}{ch*w}{R}")

def row(label, value, lc=K, vc=W, lw=16):
    print(f"  {lc}│{R}  {DIM}{label:<{lw}}{R}  {vc}{value}{R}")

def box_top(c=K, w=56):
    print(f"  {c}┌{'─'*w}┐{R}")

def box_bot(c=K, w=56):
    print(f"  {c}└{'─'*w}┘{R}")

def box_row(text, c=K, w=56):
    print(f"  {c}│{R} {text:<{w-1}}{c}│{R}")

def spinner(label, dur=1.5, c=CY):
    fr = ["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏"]
    t  = time.time() + dur
    i  = 0
    while time.time() < t:
        sys.stdout.write(f"\r  {c}{fr[i%10]}{R}  {W}{label}...{R}  ")
        sys.stdout.flush()
        time.sleep(0.08)
        i += 1
    sys.stdout.write("\r" + " "*64 + "\r")

def pbar(label, dur=1.8, c=CY):
    for i in range(21):
        filled = int(30 * i / 20)
        bar = "█" * filled + "░" * (30 - filled)
        sys.stdout.write(f"\r  {c}[{bar}]{R} {W}{5*i:3d}%{R}  {DIM}{label}{R}")
        sys.stdout.flush()
        time.sleep(dur / 20)
    print()

def section(title, c=CY):
    print(f"\n  {c}{'─'*4} {BD}{title}{R}{c} {'─'*(48-len(title))}{R}")

def ok(msg):  print(f"\n  {GR}[✔]{R} {W}{msg}{R}")
def err(msg): print(f"\n  {RE}[✘]{R} {W}{msg}{R}")
def warn(msg):print(f"\n  {YL}[!]{R} {W}{msg}{R}")
def info(msg):print(f"\n  {CY}[i]{R} {W}{msg}{R}")

def norm_phone(n):
    n = n.strip().replace(" ","").replace("-","").replace("(","").replace(")","")
    if n and not n.startswith("+"):
        n = "+" + n
    return n

def valid_ip(ip):
    parts = ip.split(".")
    return (len(parts) == 4 and
            all(p.isdigit() and 0 <= int(p) <= 255 for p in parts))

def prompt(label, c=CY):
    return input(f"  {c}  {label}:{R} ").strip()

def choose(c=CY):
    return input(f"\n  {c}▶{R} ").strip()


# ─────────────────────────────────────────────────────────────
#  PHONEINFOGA DETECTION
#  Searches all common install locations so the "not installed"
#  bug never triggers if the user already has it.
# ─────────────────────────────────────────────────────────────
_PIF_SEARCH_DIRS = [
    os.path.expanduser("~"),          # ~/PhoneInfoga/phoneinfoga.py
    os.path.expanduser("~/storage"),  # Termux external storage
    "/opt",                           # Linux system installs
    "/usr/local",
    os.getcwd(),                      # current working directory
]
_PIF_DIRNAME = "PhoneInfoga"
_PIF_SCRIPT  = "phoneinfoga.py"

def find_phoneinfoga():
    """
    Return the full path to phoneinfoga.py if found anywhere,
    or None if not installed.  Checks PATH first (in case it's
    a system-wide install), then all search dirs.
    """
    # 1. Check if it's on PATH as a command
    if shutil.which("phoneinfoga"):
        return "phoneinfoga"          # callable directly

    # 2. Search common directories
    for base in _PIF_SEARCH_DIRS:
        candidate = os.path.join(base, _PIF_DIRNAME, _PIF_SCRIPT)
        if os.path.isfile(candidate):
            return candidate

    # 3. Walk one level deeper in home (handles nested clones)
    home = os.path.expanduser("~")
    try:
        for entry in os.scandir(home):
            if entry.is_dir():
                candidate = os.path.join(entry.path, _PIF_SCRIPT)
                if os.path.isfile(candidate):
                    # Verify it looks like PhoneInfoga (contains -n flag)
                    try:
                        with open(candidate) as f:
                            snippet = f.read(512)
                        if "phoneinfoga" in snippet.lower() or "-n" in snippet:
                            return candidate
                    except Exception:
                        pass
    except Exception:
        pass

    return None

def run_phoneinfoga(pif_path, number):
    """Run PhoneInfoga safely with the correct python interpreter."""
    if pif_path == "phoneinfoga":
        os.system(f"phoneinfoga -n {number}")
    else:
        os.system(f"python3 \"{pif_path}\" -n {number}")


# ─────────────────────────────────────────────────────────────
#  DEPENDENCY HELPERS
# ─────────────────────────────────────────────────────────────
def pip_install(pkg, label=None):
    label = label or pkg
    print(f"\n  {YL}[~] Installing {label}...{R}")
    # Try system-packages-allowed first (newer Debian/Ubuntu/Termux)
    ret = os.system(
        f"python3 -m pip install {pkg} -q --break-system-packages 2>/dev/null"
        f" || python3 -m pip install {pkg} -q"
    )
    if ret == 0:
        ok(f"{label} installed successfully.")
    else:
        err(f"Failed to install {label}.")
    return ret == 0

def ensure_phonenumbers():
    try:
        import phonenumbers  # noqa
        return True
    except ImportError:
        return pip_install("phonenumbers", "phonenumbers")


# ─────────────────────────────────────────────────────────────
#  TOOL INSTALLERS
# ─────────────────────────────────────────────────────────────
def install_sherlock():
    print(f"\n  {YL}[~] Installing Sherlock...{R}\n")
    pbar("sherlock-project", 2.0, YL)
    ret = os.system(
        "python3 -m pip install sherlock-project -q --break-system-packages 2>/dev/null"
        " || python3 -m pip install sherlock-project -q"
    )
    if ret == 0:
        ok("Sherlock installed.")
    else:
        err("Sherlock install failed.")
    pause()

def install_ip_tracer():
    home = os.path.expanduser("~")
    dst  = os.path.join(home, "IP-Tracer")
    print(f"\n  {LB}[~] Installing IP-Tracer...{R}\n")

    if os.path.isdir(dst):
        warn("Old IP-Tracer folder found — removing it first.")
        os.system(f"rm -rf {dst}")

    steps = [
        ("Cloning repository",
         f"git clone https://github.com/rajkumardusad/IP-Tracer.git \"{dst}\" -q"),
        ("Setting permissions",
         f"chmod +x \"{dst}/install\""),
        ("Running installer",
         f"cd \"{dst}\" && bash install 2>/dev/null || sh install 2>/dev/null"),
    ]
    for i, (lbl, cmd) in enumerate(steps, 1):
        print(f"  {LB}[{i}/{len(steps)}]{R} {lbl}...")
        os.system(cmd)
        time.sleep(0.5)

    found = shutil.which("trace") or shutil.which("ip-tracer")
    if found:
        ok("IP-Tracer ready.")
    else:
        warn("IP-Tracer installed but 'trace' not in PATH yet.\n"
             "       Restart your terminal or run:  export PATH=$PATH:~/.local/bin")
    pause()

def install_phoneinfoga():
    home = os.path.expanduser("~")
    dst  = os.path.join(home, _PIF_DIRNAME)
    print(f"\n  {PK}[~] Installing PhoneInfoga...{R}\n")

    if os.path.isdir(dst):
        warn("Old PhoneInfoga folder found — removing it first.")
        os.system(f"rm -rf \"{dst}\"")

    steps = [
        ("Cloning repository",
         f"git clone https://github.com/ExpertAnonymous/PhoneInfoga.git \"{dst}\" -q"),
        ("Setting permissions",
         f"chmod 777 \"{dst}\"/* 2>/dev/null; true"),
        ("Running setup script",
         f"cd \"{dst}\" && bash phoneinfoga.sh 2>/dev/null; true"),
        ("Installing phonenumbers lib",
         "python3 -m pip install phonenumbers -q --break-system-packages 2>/dev/null"
         " || python3 -m pip install phonenumbers -q"),
    ]
    for i, (lbl, cmd) in enumerate(steps, 1):
        print(f"  {PK}[{i}/{len(steps)}]{R} {lbl}...")
        os.system(cmd)
        time.sleep(0.5)

    found = find_phoneinfoga()
    if found:
        ok(f"PhoneInfoga ready →  {found}")
    else:
        err("phoneinfoga.py not found after install. Check your connection and retry.")
    pause()


# ─────────────────────────────────────────────────────────────
#  PHONE QUICK PARSE  (offline · phonenumbers library)
# ─────────────────────────────────────────────────────────────
def phone_parse(number):
    if not ensure_phonenumbers():
        return None
    try:
        import phonenumbers as pn
        from phonenumbers import geocoder, carrier, timezone, number_type, PhoneNumberType

        p = pn.parse(number, None)
        if not pn.is_valid_number(p):
            return {"valid": False}

        TYPE_MAP = {
            PhoneNumberType.MOBILE:               "📱 Mobile",
            PhoneNumberType.FIXED_LINE:           "☎  Landline",
            PhoneNumberType.FIXED_LINE_OR_MOBILE: "📱☎ Mobile / Landline",
            PhoneNumberType.VOIP:                 "💻 VoIP",
            PhoneNumberType.TOLL_FREE:            "🆓 Toll-Free",
            PhoneNumberType.PREMIUM_RATE:         "💰 Premium Rate",
            PhoneNumberType.SHARED_COST:          "🤝 Shared Cost",
            PhoneNumberType.PAGER:                "📟 Pager",
        }
        tzs = list(timezone.time_zones_for_number(p))
        return {
            "valid":     True,
            "e164":      pn.format_number(p, pn.PhoneNumberFormat.E164),
            "intl":      pn.format_number(p, pn.PhoneNumberFormat.INTERNATIONAL),
            "natl":      pn.format_number(p, pn.PhoneNumberFormat.NATIONAL),
            "cc":        f"+{p.country_code}",
            "region":    geocoder.description_for_number(p, "en") or "Unknown",
            "carrier":   carrier.name_for_number(p, "en")         or "Unknown",
            "line_type": TYPE_MAP.get(number_type(p), "❓ Unknown"),
            "timezones": tzs,
        }
    except Exception:
        return {"valid": False}

def show_phone_info(info, number):
    if info is None:
        warn("phonenumbers library unavailable — skipping quick parse.")
        return

    if not info.get("valid"):
        print(f"""
  {RE}╔══════════════════════════════════════════════════════════╗
  ║  ✘  INVALID NUMBER                                       ║
  ║     '{number}'
  ║     Always include the country code, e.g.  +971501234567 ║
  ╚══════════════════════════════════════════════════════════╝{R}
""")
        return

    tz = ", ".join(info["timezones"]) if info["timezones"] else "Unknown"
    # Truncate timezone string if too long
    tz = tz[:50] + "…" if len(tz) > 50 else tz

    print(f"""
  {K}╔══════════════════════════════════════════════════════════╗{R}
  {K}║{R}{BD}{PK}           📱  QUICK PARSE RESULTS                      {R}{K}║{R}
  {K}╠══════════════════════════════════════════════════════════╣{R}""")
    row("E.164",         info["e164"],      lc=K, vc=GD)
    row("International", info["intl"],      lc=K, vc=W)
    row("National",      info["natl"],      lc=K, vc=W)
    row("Country Code",  info["cc"],        lc=K, vc=LG)
    row("Region",        info["region"],    lc=K, vc=CY)
    row("Carrier",       info["carrier"],   lc=K, vc=YL)
    row("Line Type",     info["line_type"], lc=K, vc=W)
    row("Timezone(s)",   tz,                lc=K, vc=LB)
    print(f"  {K}╚══════════════════════════════════════════════════════════╝{R}")


# ─────────────────────────────────────────────────────────────
#  LOGOS
# ─────────────────────────────────────────────────────────────
def logo_main():
    print(f"""{RE}
  ████████╗ ██████╗  ██████╗ ██╗     ███████╗
  ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ╚══███╔╝
     ██║   ██║   ██║██║   ██║██║       ███╔╝ 
     ██║   ██║   ██║██║   ██║██║      ███╔╝  
     ██║   ╚██████╔╝╚██████╔╝███████╗███████╗
     ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝{R}
{K}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{R}
{OR}        ☠   A D V A N C E D   T O O L K I T   ☠{R}
{K}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{R}
{DIM}        github.com/00xk/Toolz  │  v6.0  │  Linux & Termux{R}
""")

def logo_sherlock():
    H=OR; F=YL; P=K; A=CY
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
    print(f"""{PU}  ╔════════════════════════════════════════════════════════╗
  ║          S H E R L O C K   O S I N T                ║
  ║       "When you eliminate the impossible..."         ║
  ╚════════════════════════════════════════════════════════╝{R}
{K}  ┌────────────────────────────────────────────────────────┐{R}
{GR}  │{W}   ✦ 400+ platforms   ✦ Batch mode   ✦ Export to file  {GR}│{R}
{K}  └────────────────────────────────────────────────────────┘{R}
""")

def logo_ip():
    print(f"""
{LB}  ██╗██████╗     ████████╗██████╗  █████╗  ██████╗███████╗██████╗
  ██║██╔══██╗    ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗
  ██║██████╔╝       ██║   ██████╔╝███████║██║     █████╗  ██████╔╝
  ██║██╔═══╝        ██║   ██╔══██╗██╔══██║██║     ██╔══╝  ██╔══██╗
  ██║██║            ██║   ██║  ██║██║  ██║╚██████╗███████╗██║  ██║
  ╚═╝╚═╝            ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚══════╝╚═╝  ╚═╝{R}
{K}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{R}
{LB}              🌐  IP GEOLOCATION & TRACE ENGINE{R}
{K}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{R}
{K}  ┌────────────────────────────────────────────────────────────┐{R}
{LG}  │{W}   ✦ Country · City · ISP · ASN · Lat/Lon · Timezone      {LG}│{R}
{K}  └────────────────────────────────────────────────────────────┘{R}
""")

def logo_phone():
    print(f"""
{PK}  ██████╗ ██╗  ██╗ ██████╗ ███╗   ██╗███████╗
  ██╔══██╗██║  ██║██╔═══██╗████╗  ██║██╔════╝
  ██████╔╝███████║██║   ██║██╔██╗ ██║█████╗  
  ██╔═══╝ ██╔══██║██║   ██║██║╚██╗██║██╔══╝  
  ██║     ██║  ██║╚██████╔╝██║ ╚████║███████╗
  ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝{R}
{PK}  ██████╗  ██████╗ ██╗███╗   ██╗████████╗
  ██╔══██╗██╔═══██╗██║████╗  ██║╚══██╔══╝
  ██████╔╝██║   ██║██║██╔██╗ ██║   ██║   
  ██╔═══╝ ██║   ██║██║██║╚██╗██║   ██║   
  ██║     ╚██████╔╝██║██║ ╚████║   ██║   
  ╚═╝      ╚═════╝ ╚═╝╚═╝  ╚═══╝   ╚═╝  {R}
{K}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{R}
{PK}            📱  MOBILE NUMBER OSINT ENGINE{R}
{K}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{R}
{K}  ┌────────────────────────────────────────────────────────────┐{R}
{PK}  │{W}   ✦ Carrier · Region · Line type  ✦ Validity check        {PK}│{R}
{PK}  │{W}   ✦ PhoneInfoga deep OSINT scan  (all countries)          {PK}│{R}
{K}  └────────────────────────────────────────────────────────────┘{R}
""")


# ─────────────────────────────────────────────────────────────
#  MENU HELPERS
# ─────────────────────────────────────────────────────────────
def menu_header(title):
    print(f"{K}  ╔════════════════════════════════════════════════════════╗{R}")
    pad = (56 - len(title)) // 2
    print(f"  {K}║{R}{' '*pad}{BD}{W}{title}{R}{' '*(56-pad-len(title))}{K}║{R}")
    print(f"{K}  ╠════════════════════════════════════════════════════════╣{R}")

def menu_item(key, icon, label, kc=GR):
    print(f"  {K}║{R}   {kc}[{key}]{R}  {icon}  {W}{label:<46}{K}║{R}")

def menu_gap():
    print(f"  {K}║{R}{' '*58}{K}║{R}")

def menu_footer():
    print(f"  {K}╚════════════════════════════════════════════════════════╝{R}\n")


# ─────────────────────────────────────────────────────────────
#  MODULE: SHERLOCK
# ─────────────────────────────────────────────────────────────
def mod_sherlock():
    if not shutil.which("sherlock"):
        warn("Sherlock is not installed.")
        print(f"  {DIM}Installing automatically...{R}\n")
        install_sherlock()
        if not shutil.which("sherlock"):
            err("Installation failed. Returning to main menu.")
            pause(); return

    while True:
        clr(); logo_sherlock()
        menu_header("SHERLOCK — USERNAME HUNT")
        menu_item("1", "🔍", "Single username scan")
        menu_item("2", "📂", "Batch scan from file")
        menu_item("3", "💾", "Scan and save results to file")
        menu_gap()
        menu_item("0", "✖ ", "Back to main menu", kc=RE)
        menu_footer()
        ch = choose(PU)

        if ch == "1":
            u = prompt("Target username", YL)
            if not u: continue

            section("Target Info", PU)
            print(f"  {K}┌────────────────────────────────────────────────────┐{R}")
            print(f"  {K}│{R}  {DIM}Username :{R}  {YL}{u}{R}")
            print(f"  {K}│{R}  {DIM}Engine   :{R}  {W}Sherlock  ·  400+ platforms{R}")
            print(f"  {K}└────────────────────────────────────────────────────┘{R}")
            spinner("Initializing scan", 1.0, PU)
            print(); ln(PU); print()
            os.system(f"sherlock \"{u}\"")
            print(); ln(PU)
            pause()

        elif ch == "2":
            path = prompt("File path (one username per line)", YL)
            if not path: continue
            if not os.path.isfile(path):
                err(f"File not found: {path}"); pause(); continue

            with open(path) as f:
                users = [l.strip() for l in f if l.strip()]

            if not users:
                warn("File is empty."); pause(); continue

            info(f"Loaded {len(users)} username(s).")
            time.sleep(0.6)

            for i, u in enumerate(users, 1):
                section(f"Target {i}/{len(users)} → {u}", PU)
                os.system(f"sherlock \"{u}\"")
                print()

            ok(f"Batch scan complete — {len(users)} target(s) processed.")
            pause()

        elif ch == "3":
            u = prompt("Username to scan", YL)
            if not u: continue
            out = f"{u}_sherlock.txt"
            spinner(f"Scanning & saving to {out}", 1.5, PU)
            os.system(f"sherlock \"{u}\" --output \"{out}\"")
            ok(f"Results saved → {out}")
            pause()

        elif ch == "0":
            break
        else:
            err("Invalid option."); time.sleep(0.8)


# ─────────────────────────────────────────────────────────────
#  MODULE: IP TRACER
# ─────────────────────────────────────────────────────────────
def get_ip_cmd():
    return next((c for c in ["trace", "ip-tracer"] if shutil.which(c)), None)

def mod_ip():
    if not get_ip_cmd():
        warn("IP-Tracer is not installed.")
        print(f"  {DIM}Installing automatically...{R}\n")
        install_ip_tracer()
        if not get_ip_cmd():
            err("Installation failed. Try restarting your terminal.")
            pause(); return

    while True:
        clr(); logo_ip()
        cmd = get_ip_cmd()

        menu_header("IP-TRACER — GEOLOCATION")
        menu_item("1", "🏠", "Trace my own IP address")
        menu_item("2", "🎯", "Trace a target IP address")
        menu_item("3", "📂", "Batch trace from file")
        menu_gap()
        menu_item("0", "✖ ", "Back to main menu", kc=RE)
        menu_footer()
        ch = choose(LB)

        if ch == "1":
            spinner("Fetching your IP info", 1.2, LB)
            print(); ln(LB); print()
            os.system(f"{cmd} -m")
            print(); ln(LB); pause()

        elif ch == "2":
            ip = prompt("Target IP address", YL)
            if not ip: continue

            if not valid_ip(ip):
                err("Invalid IP format. Use: xxx.xxx.xxx.xxx"); pause(); continue

            section("Target Info", LB)
            print(f"  {K}┌────────────────────────────────────────────────────┐{R}")
            print(f"  {K}│{R}  {DIM}Target :{R}  {YL}{ip}{R}")
            print(f"  {K}│{R}  {DIM}Engine :{R}  {W}IP-Tracer via ip-api.com{R}")
            print(f"  {K}└────────────────────────────────────────────────────┘{R}")
            spinner(f"Tracing {ip}", 1.5, LB)
            print(); ln(LB); print()
            os.system(f"{cmd} -t {ip}")
            print(); ln(LB); pause()

        elif ch == "3":
            path = prompt("File path (one IP per line)", YL)
            if not path: continue
            if not os.path.isfile(path):
                err(f"File not found: {path}"); pause(); continue

            with open(path) as f:
                ips = [l.strip() for l in f if l.strip()]

            if not ips:
                warn("File is empty."); pause(); continue

            info(f"Loaded {len(ips)} IP address(es).")
            time.sleep(0.5)

            for i, ip in enumerate(ips, 1):
                section(f"Target {i}/{len(ips)} → {ip}", LB)
                if not valid_ip(ip):
                    warn(f"Skipping invalid IP: {ip}")
                    continue
                os.system(f"{cmd} -t {ip}")
                print(); time.sleep(0.4)

            ok(f"Batch trace complete — {len(ips)} address(es) processed.")
            pause()

        elif ch == "0":
            break
        else:
            err("Invalid option."); time.sleep(0.8)


# ─────────────────────────────────────────────────────────────
#  MODULE: PHONE OSINT
# ─────────────────────────────────────────────────────────────
def mod_phone():
    while True:
        clr(); logo_phone()

        # Re-detect PhoneInfoga on EVERY loop iteration so install
        # status is always fresh and never stale.
        pif_path = find_phoneinfoga()
        pif_ok   = pif_path is not None

        if pif_ok:
            pif_label = f"{GR}Installed{R}  {DIM}({pif_path}){R}"
        else:
            pif_label = f"{RE}Not installed{R}  {DIM}— use option [4] to install{R}"

        section("PhoneInfoga Status", PK)
        print(f"  {K}│{R}  {pif_label}\n")

        menu_header("PHONE OSINT — NUMBER INTEL")
        menu_item("1", "⚡", "Quick scan     (offline · instant)")
        menu_item("2", "🔬", "Deep scan      (PhoneInfoga · full OSINT)")
        menu_item("3", "🔭", "Full scan      (quick + deep combined)")
        menu_item("4", "📂", "Batch scan     (file of numbers)")
        menu_gap()
        menu_item("5", "⚙ ", "Install / Reinstall PhoneInfoga", kc=GD)
        menu_item("0", "✖ ", "Back to main menu", kc=RE)
        menu_footer()
        ch = choose(PK)

        # ── 1. Quick scan (offline) ──────────────────────────
        if ch == "1":
            n = norm_phone(prompt("Phone number  e.g. +971501234567", YL))
            if not n: continue
            spinner("Parsing number", 0.8, PK)
            show_phone_info(phone_parse(n), n)
            pause()

        # ── 2. Deep scan (PhoneInfoga) ───────────────────────
        elif ch == "2":
            if not pif_ok:
                err("PhoneInfoga is not installed.")
                warn("Use option [5] to install it.")
                pause(); continue

            n = norm_phone(prompt("Phone number  e.g. +971501234567", YL))
            if not n: continue

            section("Deep Scan Target", PK)
            print(f"  {K}┌────────────────────────────────────────────────────┐{R}")
            print(f"  {K}│{R}  {DIM}Number :{R}  {GD}{n}{R}")
            print(f"  {K}│{R}  {DIM}Engine :{R}  {W}PhoneInfoga · search fingerprinting{R}")
            print(f"  {K}│{R}  {DIM}Path   :{R}  {DIM}{pif_path}{R}")
            print(f"  {K}└────────────────────────────────────────────────────┘{R}")

            spinner("Launching PhoneInfoga", 1.5, PK)
            print(); ln(PK); print()
            run_phoneinfoga(pif_path, n)
            print(); ln(PK); pause()

        # ── 3. Full scan (quick + deep) ──────────────────────
        elif ch == "3":
            n = norm_phone(prompt("Phone number  e.g. +971501234567", YL))
            if not n: continue

            section("Phase 1 · Quick Parse  (offline)", PK)
            spinner("Parsing number", 0.8, PK)
            parsed = phone_parse(n)
            show_phone_info(parsed, n)

            if parsed and not parsed.get("valid"):
                err("Invalid number — cannot continue."); pause(); continue

            if pif_ok:
                section("Phase 2 · PhoneInfoga Deep Scan", PK)
                spinner("Launching PhoneInfoga", 1.2, PK)
                print(); ln(PK); print()
                run_phoneinfoga(pif_path, n)
                print(); ln(PK)
            else:
                warn("PhoneInfoga not installed — skipping deep scan.")
                info("Use option [5] to install PhoneInfoga.")

            pause()

        # ── 4. Batch scan ────────────────────────────────────
        elif ch == "4":
            path = prompt("File path  (one number per line)", YL)
            if not path: continue
            if not os.path.isfile(path):
                err(f"File not found: {path}"); pause(); continue

            with open(path) as f:
                nums = [norm_phone(l) for l in f if l.strip()]

            if not nums:
                warn("File is empty."); pause(); continue

            info(f"Loaded {len(nums)} number(s).")
            time.sleep(0.5)

            for i, n in enumerate(nums, 1):
                section(f"Target {i}/{len(nums)} → {n}", PK)
                parsed = phone_parse(n)
                show_phone_info(parsed, n)

                if pif_ok and parsed and parsed.get("valid"):
                    print(f"  {DIM}Running deep scan...{R}\n")
                    run_phoneinfoga(pif_path, n)

                ln(PK); print(); time.sleep(0.3)

            ok(f"Batch scan complete — {len(nums)} number(s) processed.")
            pause()

        # ── 5. Install PhoneInfoga ───────────────────────────
        elif ch == "5":
            install_phoneinfoga()
            # Loop back — find_phoneinfoga() will re-detect on next iteration

        elif ch == "0":
            break
        else:
            err("Invalid option."); time.sleep(0.8)


# ─────────────────────────────────────────────────────────────
#  MODULE: UPDATE
# ─────────────────────────────────────────────────────────────
def mod_update():
    clr()
    print(f"""
  {PU}╔════════════════════════════════════════════════════════╗
  ║              F O R C E   U P D A T E                  ║
  ╚════════════════════════════════════════════════════════╝{R}
""")
    home     = os.path.expanduser("~")
    tool_dir = os.path.join(home, "Toolz")

    steps = [
        (f"  {YL}[1/3] Removing old installation...{R}",
         lambda: os.system(f"rm -rf \"{tool_dir}\"") if os.path.isdir(tool_dir) else None),
        (f"  {CY}[2/3] Pulling latest version from GitHub...{R}",
         lambda: os.system(f"cd \"{home}\" && git clone https://github.com/00xk/Toolz.git -q")),
        (f"  {GR}[3/3] Finalizing...{R}",
         lambda: time.sleep(0.5)),
    ]

    for msg, fn in steps:
        print(msg)
        fn()
        time.sleep(0.8)

    ok("Toolz updated to the latest version!")
    time.sleep(1.5)
    os.system(f"cd \"{tool_dir}\" && python3 toolz.py")
    sys.exit(0)


# ─────────────────────────────────────────────────────────────
#  MAIN MENU
# ─────────────────────────────────────────────────────────────
def main():
    while True:
        clr()
        logo_main()

        menu_header("M A I N   M E N U")
        menu_gap()
        menu_item("1", "🔍", "Sherlock OSINT   —  Username Hunt")
        menu_item("2", "🌐", "IP Tracer        —  Geolocation")
        menu_item("3", "📱", "Phone OSINT      —  Number Intelligence")
        menu_item("4", "🔄", "Update Tool      —  Pull Latest")
        menu_gap()
        menu_item("0", "✖ ", "Exit", kc=RE)
        menu_footer()

        ch = choose(CY)

        if   ch == "1": mod_sherlock()
        elif ch == "2": mod_ip()
        elif ch == "3": mod_phone()
        elif ch == "4": mod_update()
        elif ch == "0":
            clr()
            print(f"\n  {CY}Stay curious. Stay ethical.{R}  {DIM}Goodbye 👋{R}\n")
            sys.exit(0)
        else:
            err("Invalid — choose 0 to 4.")
            time.sleep(0.9)


if __name__ == "__main__":
    main()
