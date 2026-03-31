#!/usr/bin/env python3
# ╔══════════════════════════════════════════════════════════════╗
# ║                  T O O L Z  v7.0                            ║
# ║         Advanced OSINT & Utility Toolkit                    ║
# ║         Linux & Termux  |  github.com/00xk/Toolz            ║
# ╚══════════════════════════════════════════════════════════════╝

import os, sys, time, shutil, subprocess

# ─────────────────────────────────────────────────────────────
#  COLORS
# ─────────────────────────────────────────────────────────────
R   = "\033[0m"
BD  = "\033[1m"
DIM = "\033[2m"
K   = "\033[1;90m"
W   = "\033[1;37m"
RE  = "\033[1;31m"
GR  = "\033[1;32m"
YL  = "\033[1;33m"
CY  = "\033[1;36m"
PU  = "\033[1;35m"
OR  = "\033[38;5;208m"
LB  = "\033[38;5;39m"
LG  = "\033[38;5;82m"
PK  = "\033[38;5;213m"
GD  = "\033[38;5;220m"

# ─────────────────────────────────────────────────────────────
#  CORE UTILITIES
# ─────────────────────────────────────────────────────────────
def clr():
    os.system("clear")

def pause(msg="Press Enter to continue..."):
    input(f"\n  {DIM}{msg}{R}")

def ln(c=K, ch="─", w=58):
    print(f"  {c}{ch * w}{R}")

def row(label, value, lc=K, vc=W, lw=16):
    label_str = f"{DIM}{label:<{lw}}{R}"
    print(f"  {lc}│{R}  {label_str}  {vc}{value}{R}")

def spinner(label, dur=1.5, c=CY):
    fr = ["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏"]
    end = time.time() + dur
    i   = 0
    while time.time() < end:
        sys.stdout.write(f"\r  {c}{fr[i%10]}{R}  {W}{label}...{R}  ")
        sys.stdout.flush()
        time.sleep(0.08)
        i += 1
    sys.stdout.write("\r" + " "*64 + "\r")

def pbar(label, dur=2.0, c=CY):
    for i in range(21):
        filled = int(30 * i / 20)
        bar = "█" * filled + "░" * (30 - filled)
        sys.stdout.write(f"\r  {c}[{bar}]{R} {W}{5*i:3d}%{R}  {DIM}{label}{R}")
        sys.stdout.flush()
        time.sleep(dur / 20)
    print()

def section(title, c=CY):
    print(f"\n  {c}{'━'*4} {BD}{title}{R}{c} {'━'*(50-len(title))}{R}\n")

def ok(msg):   print(f"\n  {GR}[✔]{R} {W}{msg}{R}")
def err(msg):  print(f"\n  {RE}[✘]{R} {W}{msg}{R}")
def warn(msg): print(f"\n  {YL}[!]{R} {W}{msg}{R}")
def info(msg): print(f"\n  {CY}[i]{R} {W}{msg}{R}")

def prompt(label, c=YL):
    return input(f"\n  {c}  {label}:{R} ").strip()

def choose(c=CY):
    return input(f"\n  {c}▶{R} ").strip()

def norm_phone(n):
    n = n.strip()
    for ch in [" ", "-", "(", ")", ".", "\t"]:
        n = n.replace(ch, "")
    if n and not n.startswith("+"):
        n = "+" + n
    return n

def valid_ip(ip):
    p = ip.split(".")
    return len(p) == 4 and all(x.isdigit() and 0 <= int(x) <= 255 for x in p)

def pip_install(pkg):
    """Install a pip package, trying multiple strategies."""
    r = os.system(
        f"python3 -m pip install {pkg} -q --break-system-packages 2>/dev/null"
        f" || python3 -m pip install {pkg} -q 2>/dev/null"
        f" || pip install {pkg} -q --break-system-packages 2>/dev/null"
        f" || pip3 install {pkg} -q 2>/dev/null"
    )
    return r == 0


# ─────────────────────────────────────────────────────────────
#  PHONEINFOGA DETECTION  (robust recursive search)
#
#  After install via phoneinfoga.sh the repo self-clones, so
#  the script may be nested: ~/PhoneInfoga/PhoneInfoga/phoneinfoga.py
#  We do a proper recursive find to handle all cases.
# ─────────────────────────────────────────────────────────────
def find_phoneinfoga():
    """
    Return (python_binary, script_path) tuple, or None if not found.
    Handles:
      - System PATH command  →  ("phoneinfoga", None)
      - ~/PhoneInfoga/phoneinfoga.py
      - ~/PhoneInfoga/PhoneInfoga/phoneinfoga.py  (nested clone from .sh)
      - Any subfolder of ~  (in case user cloned elsewhere)
    """
    # 1. System-level install
    if shutil.which("phoneinfoga"):
        return ("phoneinfoga", None)

    # 2. Recursive search under home directory (max depth 4)
    home = os.path.expanduser("~")
    for root, dirs, files in os.walk(home):
        # Skip hidden dirs, node_modules, etc.
        dirs[:] = [d for d in dirs if not d.startswith(".") and d != "node_modules"]

        # Stop going too deep
        depth = root.replace(home, "").count(os.sep)
        if depth > 4:
            dirs.clear()
            continue

        if "phoneinfoga.py" in files:
            script = os.path.join(root, "phoneinfoga.py")
            # Quick sanity: verify the file mentions phone/number
            try:
                with open(script, "r", errors="ignore") as f:
                    head = f.read(1024).lower()
                if "phone" in head or "number" in head or "-n" in head:
                    # Decide which python to use
                    py = _best_python(root)
                    return (py, script)
            except Exception:
                pass

    return None

def _best_python(script_dir):
    """
    PhoneInfoga (ExpertAnonymous) uses python2 internally but also
    works with python3 on most modern Termux builds.
    Prefer python3, fall back to python.
    """
    for candidate in ["python3", "python", "python2"]:
        if shutil.which(candidate):
            return candidate
    return "python3"

def run_phoneinfoga(py, script, number):
    """Execute PhoneInfoga safely."""
    if script is None:
        # System command
        os.system(f"phoneinfoga -n {number}")
    else:
        # Run from inside its own directory so relative imports work
        script_dir = os.path.dirname(script)
        os.system(f"cd \"{script_dir}\" && {py} \"{os.path.basename(script)}\" -n {number}")


# ─────────────────────────────────────────────────────────────
#  INSTALLERS
# ─────────────────────────────────────────────────────────────
def install_sherlock():
    print(f"\n  {YL}[~] Installing Sherlock...{R}\n")
    pbar("sherlock-project", 2.0, YL)
    if pip_install("sherlock-project"):
        ok("Sherlock installed.")
    else:
        err("Sherlock install failed. Try: pip install sherlock-project")
    pause()

def install_ip_tracer():
    home = os.path.expanduser("~")
    dst  = os.path.join(home, "IP-Tracer")
    print(f"\n  {LB}[~] Installing IP-Tracer...{R}\n")

    if os.path.isdir(dst):
        warn("Removing old IP-Tracer folder...")
        os.system(f"rm -rf \"{dst}\"")

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

    if shutil.which("trace") or shutil.which("ip-tracer"):
        ok("IP-Tracer is ready.")
    else:
        warn("IP-Tracer installed but may not be in PATH yet.\n"
             "       Try: export PATH=$PATH:~/.local/bin  or restart terminal.")
    pause()

def install_phoneinfoga():
    home = os.path.expanduser("~")
    dst  = os.path.join(home, "PhoneInfoga")
    print(f"\n  {PK}[~] Installing PhoneInfoga (ExpertAnonymous)...{R}\n")

    # Wipe existing to avoid nested double-clone issues
    if os.path.isdir(dst):
        warn("Removing old PhoneInfoga folder to ensure clean install...")
        os.system(f"rm -rf \"{dst}\"")

    # Official silent install method from the README
    steps = [
        ("Updating package list",
         "apt update -y 2>/dev/null || pkg update -y 2>/dev/null; true"),
        ("Installing wget",
         "apt install -y wget 2>/dev/null || pkg install -y wget 2>/dev/null; true"),
        ("Downloading install script",
         f"cd \"{home}\" && wget -q https://raw.githubusercontent.com/ExpertAnonymous/PhoneInfoga/master/phoneinfoga.sh -O phoneinfoga_setup.sh"),
        ("Running install script",
         f"cd \"{home}\" && bash phoneinfoga_setup.sh 2>&1"),
        ("Installing phonenumbers (python lib)",
         "python3 -m pip install phonenumbers -q --break-system-packages 2>/dev/null"
         " || python3 -m pip install phonenumbers -q"),
        ("Cleaning up",
         f"rm -f \"{home}/phoneinfoga_setup.sh\" 2>/dev/null; true"),
    ]

    for i, (lbl, cmd) in enumerate(steps, 1):
        print(f"  {PK}[{i}/{len(steps)}]{R} {lbl}...")
        os.system(cmd)
        time.sleep(0.5)

    result = find_phoneinfoga()
    if result:
        py, path = result
        ok(f"PhoneInfoga is ready!")
        info(f"Found at: {path or 'system PATH'}")
        info(f"Interpreter: {py}")
    else:
        err("Could not locate phoneinfoga.py after install.")
        warn("Try running manually:\n"
             "       git clone https://github.com/ExpertAnonymous/PhoneInfoga ~/PhoneInfoga\n"
             "       cd ~/PhoneInfoga && chmod 777 * && bash phoneinfoga.sh")
    pause()


# ─────────────────────────────────────────────────────────────
#  PHONE QUICK PARSE  (offline, phonenumbers lib)
# ─────────────────────────────────────────────────────────────
def ensure_phonenumbers():
    try:
        import phonenumbers  # noqa
        return True
    except ImportError:
        print(f"\n  {YL}[~] Installing phonenumbers library...{R}")
        if pip_install("phonenumbers"):
            ok("phonenumbers installed.")
            return True
        return False

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
    except Exception as e:
        return {"valid": False, "error": str(e)}

def show_phone_info(info_dict, number):
    if info_dict is None:
        warn("phonenumbers library not available — skipping quick parse.")
        return

    if not info_dict.get("valid"):
        detail = info_dict.get("error", "")
        print(f"""
  {RE}╔════════════════════════════════════════════════════════════╗
  ║  ✘  INVALID NUMBER                                         ║
  ║     {number:<58}║
  ║     Include the country code, e.g.  +971501234567          ║{f'''
  ║     Detail: {detail:<50}║''' if detail else ''}
  ╚════════════════════════════════════════════════════════════╝{R}
""")
        return

    tz = ", ".join(info_dict["timezones"]) if info_dict["timezones"] else "Unknown"
    if len(tz) > 52:
        tz = tz[:49] + "..."

    print(f"""
  {K}╔════════════════════════════════════════════════════════════╗{R}
  {K}║{R}{BD}{PK}           📱  QUICK PARSE RESULTS                        {R}{K}║{R}
  {K}╠════════════════════════════════════════════════════════════╣{R}""")
    row("E.164",          info_dict["e164"],      lc=K, vc=GD)
    row("International",  info_dict["intl"],      lc=K, vc=W)
    row("National",       info_dict["natl"],      lc=K, vc=W)
    row("Country Code",   info_dict["cc"],        lc=K, vc=LG)
    row("Region",         info_dict["region"],    lc=K, vc=CY)
    row("Carrier",        info_dict["carrier"],   lc=K, vc=YL)
    row("Line Type",      info_dict["line_type"], lc=K, vc=W)
    row("Timezone(s)",    tz,                     lc=K, vc=LB)
    print(f"  {K}╚════════════════════════════════════════════════════════════╝{R}")


# ─────────────────────────────────────────────────────────────
#  MENU HELPERS
# ─────────────────────────────────────────────────────────────
_MW = 60  # menu width

def menu_top(title, c=K):
    print(f"  {c}╔{'═'*_MW}╗{R}")
    pad = (_MW - len(title)) // 2
    print(f"  {c}║{R}{' '*pad}{BD}{W}{title}{R}{' '*(_MW - pad - len(title))}{c}║{R}")
    print(f"  {c}╠{'═'*_MW}╣{R}")

def menu_item(key, icon, label, kc=GR, note=""):
    note_str = f"  {DIM}{note}{R}" if note else ""
    line = f"   {kc}[{key}]{R}  {icon}  {W}{label}{R}{note_str}"
    # pad to fill box
    visible = len(f"   [{key}]  {icon}  {label}" + (f"  {note}" if note else ""))
    pad = max(0, _MW - 1 - visible)
    print(f"  {K}║{R}{line}{' '*pad}{K}║{R}")

def menu_sep(c=K):
    print(f"  {c}║{' '*_MW}║{R}")

def menu_bot(c=K):
    print(f"  {c}╚{'═'*_MW}╝{R}\n")


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
{K}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{R}
{OR}         ☠   A D V A N C E D   T O O L K I T   ☠{R}
{K}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{R}
{DIM}    github.com/00xk/Toolz  │  v7.0  │  Linux & Termux{R}
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
{P}         #################-...............::: {P}#**          {R}
{P}        ###################*-.............:   {P}****{R} {A}*******  {R}
{P}        %%%%%%###############*-:::........:   {P}****{R} {A}******#  {R}
{P}             @@%%%%#############%*+::::::::   {P}****{R} {A}******#  {R}
{P}                  %%%%%##########%%##         {P}***********#{R}
{P}                      @%%%########%%#%        {P}#**********#{R}
{P}                         @@%%%#####%%%        {P}%###******#%{R}
{P}                             @%%####%%#          {P}%######   {R}
{P}                                %%%#%%%#                   {R}
{P}                                  @%%@@%                   {R}
{P}                                    @@                     {R}
""")
    print(f"""{PU}  ╔════════════════════════════════════════════════════════╗
  ║          S H E R L O C K   O S I N T                ║
  ║       "When you eliminate the impossible..."         ║
  ╚════════════════════════════════════════════════════════╝{R}
{K}  ┌────────────────────────────────────────────────────────┐{R}
{GR}  │{W}   ✦ 400+ platforms   ✦ Batch mode   ✦ Save to file    {GR}│{R}
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
{LB}               🌐  IP GEOLOCATION & TRACE ENGINE{R}
{K}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{R}
{K}  ┌──────────────────────────────────────────────────────────────┐{R}
{LG}  │{W}   ✦ Country · City · ISP · ASN  ✦  Lat/Lon · Timezone      {LG}│{R}
{K}  └──────────────────────────────────────────────────────────────┘{R}
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
{K}  ┌──────────────────────────────────────────────────────────────┐{R}
{PK}  │{W}   ✦ Carrier · Region · Line type  ✦  Timezone              {PK}│{R}
{PK}  │{W}   ✦ PhoneInfoga deep OSINT engine (all countries)          {PK}│{R}
{K}  └──────────────────────────────────────────────────────────────┘{R}
""")


# ─────────────────────────────────────────────────────────────
#  MODULE: SHERLOCK
# ─────────────────────────────────────────────────────────────
def mod_sherlock():
    if not shutil.which("sherlock"):
        warn("Sherlock not installed — installing now...")
        install_sherlock()
        if not shutil.which("sherlock"):
            err("Installation failed. Returning to main menu.")
            pause(); return

    while True:
        clr(); logo_sherlock()
        menu_top("SHERLOCK  —  USERNAME HUNT", PU)
        menu_item("1", "🔍", "Single username scan")
        menu_item("2", "📂", "Batch scan from file")
        menu_item("3", "💾", "Scan and save results to file")
        menu_sep()
        menu_item("0", "✖ ", "Back", kc=RE)
        menu_bot()
        ch = choose(PU)

        if ch == "1":
            u = prompt("Target username")
            if not u: continue
            section(f"Scanning → {u}", PU)
            print(f"  {K}┌──────────────────────────────────────────────────────┐{R}")
            print(f"  {K}│{R}  {DIM}Username  :{R}  {YL}{u}{R}")
            print(f"  {K}│{R}  {DIM}Engine    :{R}  {W}Sherlock  ·  400+ platforms{R}")
            print(f"  {K}└──────────────────────────────────────────────────────┘{R}")
            spinner("Initializing scan", 1.0, PU)
            print(); ln(PU); print()
            os.system(f"sherlock \"{u}\"")
            print(); ln(PU); pause()

        elif ch == "2":
            path = prompt("File path (one username per line)")
            if not path: continue
            if not os.path.isfile(path):
                err(f"File not found: {path}"); pause(); continue
            with open(path) as f:
                users = [l.strip() for l in f if l.strip()]
            if not users:
                warn("File is empty."); pause(); continue
            info(f"Loaded {len(users)} username(s) — starting batch scan...")
            time.sleep(0.8)
            for i, u in enumerate(users, 1):
                section(f"Target {i}/{len(users)}  →  {u}", PU)
                os.system(f"sherlock \"{u}\"")
                print()
            ok(f"Batch complete — {len(users)} target(s) scanned.")
            pause()

        elif ch == "3":
            u = prompt("Username to scan")
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
        warn("IP-Tracer not installed — installing now...")
        install_ip_tracer()
        if not get_ip_cmd():
            err("Installation failed. Try restarting your terminal.")
            pause(); return

    while True:
        clr(); logo_ip()
        cmd = get_ip_cmd()
        menu_top("IP-TRACER  —  GEOLOCATION", LB)
        menu_item("1", "🏠", "Trace my own IP address")
        menu_item("2", "🎯", "Trace a target IP address")
        menu_item("3", "📂", "Batch trace IPs from file")
        menu_sep()
        menu_item("0", "✖ ", "Back", kc=RE)
        menu_bot()
        ch = choose(LB)

        if ch == "1":
            spinner("Fetching your public IP info", 1.2, LB)
            print(); ln(LB); print()
            os.system(f"{cmd} -m")
            print(); ln(LB); pause()

        elif ch == "2":
            ip = prompt("Target IP address")
            if not ip: continue
            if not valid_ip(ip):
                err("Invalid IP format. Use:  xxx.xxx.xxx.xxx"); pause(); continue
            section(f"Tracing → {ip}", LB)
            print(f"  {K}┌──────────────────────────────────────────────────────┐{R}")
            print(f"  {K}│{R}  {DIM}Target    :{R}  {YL}{ip}{R}")
            print(f"  {K}│{R}  {DIM}Engine    :{R}  {W}IP-Tracer via ip-api.com{R}")
            print(f"  {K}└──────────────────────────────────────────────────────┘{R}")
            spinner(f"Tracing {ip}", 1.5, LB)
            print(); ln(LB); print()
            os.system(f"{cmd} -t {ip}")
            print(); ln(LB); pause()

        elif ch == "3":
            path = prompt("File path (one IP per line)")
            if not path: continue
            if not os.path.isfile(path):
                err(f"File not found: {path}"); pause(); continue
            with open(path) as f:
                ips = [l.strip() for l in f if l.strip()]
            if not ips:
                warn("File is empty."); pause(); continue
            info(f"Loaded {len(ips)} IP address(es) — starting batch trace...")
            time.sleep(0.6)
            skipped = 0
            for i, ip in enumerate(ips, 1):
                if not valid_ip(ip):
                    warn(f"Skipping invalid entry: {ip}")
                    skipped += 1
                    continue
                section(f"Target {i}/{len(ips)}  →  {ip}", LB)
                os.system(f"{cmd} -t {ip}")
                print(); time.sleep(0.4)
            ok(f"Batch complete — {len(ips)-skipped} traced, {skipped} skipped.")
            pause()

        elif ch == "0":
            break
        else:
            err("Invalid option."); time.sleep(0.8)


# ─────────────────────────────────────────────────────────────
#  MODULE: PHONE OSINT
# ─────────────────────────────────────────────────────────────
def _pif_status_line():
    """Return a colored status string for PhoneInfoga."""
    result = find_phoneinfoga()
    if result:
        py, path = result
        loc = path if path else "system PATH"
        return f"{GR}[✔] Installed{R}  {DIM}{loc}{R}", result
    return f"{RE}[✘] Not installed  — use option [5] to install{R}", None

def mod_phone():
    while True:
        clr(); logo_phone()

        # Always re-detect on every loop so status is live
        status_str, pif_result = _pif_status_line()
        pif_ok = pif_result is not None

        print(f"  {K}┌─  PhoneInfoga Status {'─'*38}┐{R}")
        print(f"  {K}│{R}  {status_str}")
        print(f"  {K}└{'─'*59}┘{R}")

        menu_top("PHONE OSINT  —  NUMBER INTELLIGENCE", PK)
        menu_item("1", "⚡", "Quick scan    (offline · instant results)")
        menu_item("2", "🔬", "Deep scan     (PhoneInfoga · full OSINT)")
        menu_item("3", "🔭", "Full scan     (quick + deep combined)")
        menu_item("4", "📂", "Batch scan    (file of numbers)")
        menu_sep()
        menu_item("5", "⚙ ", "Install / Reinstall PhoneInfoga", kc=GD)
        menu_item("0", "✖ ", "Back", kc=RE)
        menu_bot()
        ch = choose(PK)

        # ── 1. Quick scan ────────────────────────────────────
        if ch == "1":
            n = norm_phone(prompt("Phone number  e.g. +971501234567"))
            if not n: continue
            spinner("Parsing number offline", 0.8, PK)
            show_phone_info(phone_parse(n), n)
            pause()

        # ── 2. Deep scan ─────────────────────────────────────
        elif ch == "2":
            if not pif_ok:
                err("PhoneInfoga is not installed.")
                warn("Select option [5] to install it.")
                pause(); continue

            n = norm_phone(prompt("Phone number  e.g. +971501234567"))
            if not n: continue

            py, script = pif_result
            section(f"Deep Scan  →  {n}", PK)
            print(f"  {K}┌──────────────────────────────────────────────────────┐{R}")
            print(f"  {K}│{R}  {DIM}Number    :{R}  {GD}{n}{R}")
            print(f"  {K}│{R}  {DIM}Engine    :{R}  {W}PhoneInfoga · search fingerprinting{R}")
            print(f"  {K}│{R}  {DIM}Interpret :{R}  {DIM}{py}{R}")
            print(f"  {K}│{R}  {DIM}Script    :{R}  {DIM}{script or 'system PATH'}{R}")
            print(f"  {K}└──────────────────────────────────────────────────────┘{R}")
            spinner("Launching PhoneInfoga deep scan", 1.5, PK)
            print(); ln(PK); print()
            run_phoneinfoga(py, script, n)
            print(); ln(PK); pause()

        # ── 3. Full scan ─────────────────────────────────────
        elif ch == "3":
            n = norm_phone(prompt("Phone number  e.g. +971501234567"))
            if not n: continue

            section("Phase 1  —  Quick Parse  (offline)", PK)
            spinner("Parsing number", 0.8, PK)
            parsed = phone_parse(n)
            show_phone_info(parsed, n)

            if parsed and not parsed.get("valid"):
                err("Invalid number — aborting full scan."); pause(); continue

            if pif_ok:
                py, script = pif_result
                section("Phase 2  —  PhoneInfoga Deep Scan", PK)
                spinner("Launching PhoneInfoga", 1.2, PK)
                print(); ln(PK); print()
                run_phoneinfoga(py, script, n)
                print(); ln(PK)
            else:
                warn("PhoneInfoga not installed — Phase 2 skipped.")
                info("Use option [5] to install PhoneInfoga.")

            pause()

        # ── 4. Batch ─────────────────────────────────────────
        elif ch == "4":
            path = prompt("File path  (one number per line)")
            if not path: continue
            if not os.path.isfile(path):
                err(f"File not found: {path}"); pause(); continue
            with open(path) as f:
                nums = [norm_phone(l) for l in f if l.strip()]
            if not nums:
                warn("File is empty."); pause(); continue
            info(f"Loaded {len(nums)} number(s) — starting batch scan...")
            time.sleep(0.6)
            for i, n in enumerate(nums, 1):
                section(f"Target {i}/{len(nums)}  →  {n}", PK)
                parsed = phone_parse(n)
                show_phone_info(parsed, n)
                if pif_ok and parsed and parsed.get("valid"):
                    py, script = pif_result
                    print(f"\n  {DIM}Running PhoneInfoga deep scan...{R}\n")
                    run_phoneinfoga(py, script, n)
                ln(PK); print(); time.sleep(0.3)
            ok(f"Batch complete — {len(nums)} number(s) processed.")
            pause()

        # ── 5. Install ───────────────────────────────────────
        elif ch == "5":
            install_phoneinfoga()

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
        (f"  {CY}[2/3] Pulling latest from GitHub...{R}",
         lambda: os.system(f"cd \"{home}\" && git clone https://github.com/00xk/Toolz.git -q")),
        (f"  {GR}[3/3] Finalizing...{R}",
         lambda: time.sleep(0.5)),
    ]
    for msg, fn in steps:
        print(msg); fn(); time.sleep(0.8)

    ok("Toolz updated to the latest version!")
    time.sleep(1.5)
    os.system(f"cd \"{tool_dir}\" && python3 toolz.py")
    sys.exit(0)


# ─────────────────────────────────────────────────────────────
#  MAIN
# ─────────────────────────────────────────────────────────────
def main():
    while True:
        clr()
        logo_main()
        menu_top("M A I N   M E N U")
        menu_sep()
        menu_item("1", "🔍", "Sherlock OSINT    —  Username Hunt",         kc=PU)
        menu_item("2", "🌐", "IP Tracer         —  Geolocation",           kc=LB)
        menu_item("3", "📱", "Phone OSINT       —  Number Intelligence",   kc=PK)
        menu_item("4", "🔄", "Update Tool       —  Pull Latest Version",   kc=GD)
        menu_sep()
        menu_item("0", "✖ ", "Exit", kc=RE)
        menu_bot()

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
