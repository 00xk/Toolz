#!/usr/bin/env python3
# ╔══════════════════════════════════════════════════════════════╗
# ║                  T O O L Z  v5.0                            ║
# ║         Advanced OSINT & Utility Toolkit                    ║
# ║         Linux & Termux  |  github.com/00xk/Toolz            ║
# ╚══════════════════════════════════════════════════════════════╝

import os, sys, time, shutil, json

# ─────────────────────────────────────────────
#  COLORS
# ─────────────────────────────────────────────
R   = "\033[0m"
BD  = "\033[1m"
DIM = "\033[2m"
K   = "\033[1;90m"   # dark gray
W   = "\033[1;37m"   # white
RE  = "\033[1;31m"   # red
GR  = "\033[1;32m"   # green
YL  = "\033[1;33m"   # yellow
CY  = "\033[1;36m"   # cyan
PU  = "\033[1;35m"   # purple
OR  = "\033[38;5;208m"  # orange
LB  = "\033[38;5;39m"   # light blue
LG  = "\033[38;5;82m"   # light green
PK  = "\033[38;5;213m"  # pink
GD  = "\033[38;5;220m"  # gold
TL  = "\033[38;5;45m"   # teal


# ─────────────────────────────────────────────
#  UTILITIES
# ─────────────────────────────────────────────
def clr():
    os.system("clear")

def pause(msg="Press Enter to continue..."):
    input(f"\n  {DIM}{msg}{R}")

def ln(color=K, ch="─", w=54):
    print(f"  {color}{ch*w}{R}")

def hdr(title, color=CY):
    ln(color, "═")
    pad = (54 - len(title)) // 2
    print(f"  {color}║{R}{' '*pad}{BD}{W}{title}{R}{' '*(54-pad-len(title))}{color}║{R}")
    ln(color, "═")
    print()

def tag(label, value, lc=K, vc=W, width=14):
    print(f"  {lc}│{R}  {DIM}{label:<{width}}{R}  {vc}{value}{R}")

def spinner(label, dur=1.5, c=CY):
    fr = ["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏"]
    t = time.time() + dur; i = 0
    while time.time() < t:
        sys.stdout.write(f"\r  {c}{fr[i%10]}{R}  {W}{label}...{R}")
        sys.stdout.flush(); time.sleep(0.08); i += 1
    sys.stdout.write("\r" + " "*60 + "\r")

def pbar(label, dur=1.5, c=CY):
    for i in range(21):
        b = "█"*int(30*i/20) + "░"*(30-int(30*i/20))
        sys.stdout.write(f"\r  {c}[{b}]{R} {W}{5*i:3d}%{R}  {DIM}{label}{R}")
        sys.stdout.flush(); time.sleep(dur/20)
    print()

def norm_phone(n):
    """Ensure phone number starts with +"""
    n = n.strip().replace(" ","").replace("-","").replace("(","").replace(")","")
    if n and not n.startswith("+"):
        n = "+" + n
    return n

def valid_ip(ip):
    parts = ip.split(".")
    return len(parts)==4 and all(p.isdigit() and 0<=int(p)<=255 for p in parts)


# ─────────────────────────────────────────────
#  DEPENDENCY HELPERS
# ─────────────────────────────────────────────
def pip_install(pkg, label=None):
    label = label or pkg
    print(f"\n  {YL}[~] Installing {label}...{R}")
    ret = os.system(f"python3 -m pip install {pkg} -q --break-system-packages 2>/dev/null || python3 -m pip install {pkg} -q")
    if ret == 0:
        print(f"  {GR}[✔] {label} installed.{R}")
    else:
        print(f"  {RE}[✘] Failed to install {label}.{R}")
    return ret == 0

def ensure_requests():
    try:
        import requests; return True
    except ImportError:
        return pip_install("requests", "requests")

def ensure_phonenumbers():
    try:
        import phonenumbers; return True
    except ImportError:
        return pip_install("phonenumbers", "phonenumbers")


# ─────────────────────────────────────────────
#  INSTALL TOOLS
# ─────────────────────────────────────────────
def install_sherlock():
    print(f"\n  {YL}[~] Installing Sherlock...{R}\n")
    pbar("sherlock-project", 2.0, YL)
    ok = os.system("python3 -m pip install sherlock-project -q --break-system-packages 2>/dev/null || python3 -m pip install sherlock-project -q") == 0
    print(f"\n  {GR if ok else RE}[{'✔' if ok else '✘'}] Sherlock {'installed' if ok else 'failed'}.{R}")
    if not ok: pause()

def install_ip_tracer():
    home = os.path.expanduser("~")
    dst  = os.path.join(home, "IP-Tracer")
    print(f"\n  {YL}[~] Installing IP-Tracer...{R}\n")
    cmds = [
        ("Clone repo",       f"git clone https://github.com/rajkumardusad/IP-Tracer.git {dst} -q"),
        ("Set permissions",  f"chmod +x {dst}/install"),
        ("Run installer",    f"cd {dst} && sh install 2>/dev/null"),
    ]
    for i,(lbl,cmd) in enumerate(cmds,1):
        print(f"  {CY}[{i}/{len(cmds)}] {lbl}...{R}")
        os.system(cmd); time.sleep(0.4)
    found = shutil.which("trace") or shutil.which("ip-tracer")
    print(f"\n  {GR if found else YL}[{'✔' if found else '~'}] IP-Tracer {'ready' if found else 'installed — restart terminal if trace not found'}.{R}")
    pause()

def install_phoneinfoga():
    home = os.path.expanduser("~")
    dst  = os.path.join(home, "PhoneInfoga")
    print(f"\n  {PK}[~] Installing PhoneInfoga...{R}\n")
    cmds = [
        ("Clone repo",      f"git clone https://github.com/ExpertAnonymous/PhoneInfoga.git {dst} -q"),
        ("Permissions",     f"chmod +x {dst}/phoneinfoga.py 2>/dev/null; true"),
        ("Python deps",     f"cd {dst} && python3 -m pip install -r requirements.txt -q 2>/dev/null; true"),
        ("phonenumbers lib",f"python3 -m pip install phonenumbers -q --break-system-packages 2>/dev/null || python3 -m pip install phonenumbers -q"),
    ]
    for i,(lbl,cmd) in enumerate(cmds,1):
        print(f"  {PK}[{i}/{len(cmds)}] {lbl}...{R}")
        os.system(cmd); time.sleep(0.4)
    print(f"\n  {GR}[✔] PhoneInfoga installed.{R}")
    pause()


# ─────────────────────────────────────────────
#  PHONE QUICK PARSE  (offline)
# ─────────────────────────────────────────────
def phone_parse(number):
    """Returns dict with parsed info or None on error."""
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
            PhoneNumberType.FIXED_LINE_OR_MOBILE: "📱☎ Mobile/Landline",
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
            "region":    geocoder.description_for_number(p,"en") or "Unknown",
            "carrier":   carrier.name_for_number(p,"en") or "Unknown",
            "line_type": TYPE_MAP.get(number_type(p), "❓ Unknown"),
            "timezones": tzs,
        }
    except Exception:
        return {"valid": False}

def show_phone_info(info, number):
    if info is None:
        print(f"\n  {YL}[~] phonenumbers lib unavailable — skipping quick parse.{R}\n")
        return
    if not info.get("valid"):
        print(f"\n  {RE}╔══════════════════════════════════════════════════════╗{R}")
        print(f"  {RE}║  [✘] INVALID NUMBER: {number:<34}║{R}")
        print(f"  {RE}║      Include country code  e.g. +971501234567        ║{R}")
        print(f"  {RE}╚══════════════════════════════════════════════════════╝{R}\n")
        return
    tz = ", ".join(info["timezones"]) if info["timezones"] else "Unknown"
    print(f"\n  {K}╔══════════════════════════════════════════════════════╗{R}")
    print(f"  {K}║{R}{BD}{PK}         📱  QUICK PARSE RESULTS                     {R}{K}║{R}")
    print(f"  {K}╠══════════════════════════════════════════════════════╣{R}")
    tag("E.164",        info["e164"],     lc=K, vc=GD)
    tag("International",info["intl"],     lc=K, vc=W)
    tag("National",     info["natl"],     lc=K, vc=W)
    tag("Country Code", info["cc"],       lc=K, vc=LG)
    tag("Region",       info["region"],   lc=K, vc=CY)
    tag("Carrier",      info["carrier"],  lc=K, vc=YL)
    tag("Line Type",    info["line_type"],lc=K, vc=W)
    tag("Timezone(s)",  tz[:48],          lc=K, vc=LB)
    print(f"  {K}╚══════════════════════════════════════════════════════╝{R}\n")


# ─────────────────────────────────────────────
#  SMS SENDER  (Textbelt API)
# ─────────────────────────────────────────────
# Free key  = "textbelt"  →  1 free SMS per day, international (E.164)
# Paid key  = user-supplied from textbelt.com  →  unlimited
# ─────────────────────────────────────────────
_SMS_KEY_FILE = os.path.join(os.path.expanduser("~"), ".toolz_sms_key")

def load_sms_key():
    if os.path.isfile(_SMS_KEY_FILE):
        with open(_SMS_KEY_FILE) as f:
            k = f.read().strip()
            if k: return k
    return "textbelt"

def save_sms_key(key):
    with open(_SMS_KEY_FILE, "w") as f:
        f.write(key.strip())

def sms_quota(key):
    """Check remaining quota for a paid key."""
    if not ensure_requests(): return None
    try:
        import requests
        r = requests.get(f"https://textbelt.com/quota/{key}", timeout=8)
        d = r.json()
        return d.get("quotaRemaining")
    except Exception:
        return None

def send_sms(to, message, key="textbelt"):
    """
    Send SMS via Textbelt.
    Returns (success: bool, text_id: str|None, error: str|None)
    """
    if not ensure_requests():
        return False, None, "requests library not available"
    try:
        import requests
        resp = requests.post(
            "https://textbelt.com/text",
            data={"phone": to, "message": message, "key": key},
            timeout=15,
        )
        d = resp.json()
        if d.get("success"):
            return True, str(d.get("textId","")), None
        else:
            err = d.get("error") or d.get("message") or "Unknown error"
            return False, None, err
    except Exception as e:
        return False, None, str(e)

def sms_status(text_id):
    """Check delivery status of a sent SMS."""
    if not ensure_requests(): return "Unknown"
    try:
        import requests
        r = requests.get(f"https://textbelt.com/status/{text_id}", timeout=8)
        return r.json().get("status","Unknown")
    except Exception:
        return "Unknown"


# ─────────────────────────────────────────────
#  SMS MODULE  (standalone section inside phone_tracer)
# ─────────────────────────────────────────────
def sms_module():
    key = load_sms_key()
    while True:
        clr()
        print(f"""
{TL}  ╔══════════════════════════════════════════════════════╗
  ║          📨  S M S   S E N D E R                    ║
  ║          Free & Anonymous  ·  International          ║
  ╚══════════════════════════════════════════════════════╝{R}

{K}  ┌─  Current API Key ──────────────────────────────────┐{R}
{TL}  │{R}  {DIM}Key :{R}  {GD if key!='textbelt' else YL}{key if len(key)<=32 else key[:28]+'....'}{R}
{TL}  │{R}  {DIM}Type:{R}  {GR if key!='textbelt' else YL}{'Paid (unlimited)' if key!='textbelt' else 'Free  (1 SMS/day)'}{R}
{K}  └──────────────────────────────────────────────────────┘{R}

{K}  ┌─  Options ──────────────────────────────────────────┐{R}
  {TL}[1]{W}   ➤  Send SMS to a number                      {K}│{R}
  {TL}[2]{W}   ➤  Check delivery status of last SMS         {K}│{R}
  {TL}[3]{W}   ➤  Check API quota                           {K}│{R}
  {GD}[4]{W}   ➤  Set paid API key  (textbelt.com)          {K}│{R}
  {YL}[5]{W}   ➤  Reset to free key                         {K}│{R}
  {RE}[0]{W}   ➤  Back                                      {K}│{R}
{K}  └──────────────────────────────────────────────────────┘{R}
""")
        ch = input(f"  {TL}▶{R} ").strip()

        # ── Send SMS ──
        if ch == "1":
            print(f"\n  {K}─────────────────────────────────────────────{R}")
            print(f"  {TL}[i]{R} {DIM}Use E.164 format  e.g.  +971501234567{R}")
            print(f"  {K}─────────────────────────────────────────────{R}\n")
            to = norm_phone(input(f"  {YL}Recipient number  :{R} "))
            if not to:
                continue

            # Validate loosely
            if len(to) < 7 or not to[1:].isdigit():
                print(f"\n  {RE}[✘] Invalid number format.  Use +<countrycode><number>{R}")
                pause(); continue

            print(f"\n  {DIM}Type your message below.  Max 160 chars for standard SMS.{R}")
            print(f"  {DIM}Press Enter twice to finish.{R}\n")
            lines = []
            while True:
                line = input(f"  {W}│ {R}")
                if line == "" and lines:
                    break
                lines.append(line)
            msg = " ".join(lines).strip()
            if not msg:
                print(f"\n  {RE}[✘] Empty message.{R}"); pause(); continue

            char_color = GR if len(msg) <= 160 else YL
            print(f"\n  {K}╔══════════════════════════════════════════════════════╗{R}")
            print(f"  {K}║{R}  {DIM}To     :{R}  {GD}{to}{R}")
            print(f"  {K}║{R}  {DIM}Message:{R}  {W}{msg[:50]}{'...' if len(msg)>50 else ''}{R}")
            print(f"  {K}║{R}  {DIM}Length :{R}  {char_color}{len(msg)} chars{R}")
            print(f"  {K}║{R}  {DIM}Key    :{R}  {GR if key!='textbelt' else YL}{'Paid' if key!='textbelt' else 'Free (1/day)'}{R}")
            print(f"  {K}╚══════════════════════════════════════════════════════╝{R}")

            confirm = input(f"\n  {YL}Send?  [y/N]{R} ").strip().lower()
            if confirm != "y":
                print(f"  {DIM}Cancelled.{R}"); pause(); continue

            spinner("Sending SMS via Textbelt", 2.0, TL)
            ok, tid, err = send_sms(to, msg, key)

            if ok:
                print(f"\n  {GR}╔══════════════════════════════════════════════════════╗{R}")
                print(f"  {GR}║  [✔] SMS SENT SUCCESSFULLY                           ║{R}")
                print(f"  {GR}║{R}  {DIM}Text ID  :{R}  {CY}{tid}{R}")
                print(f"  {GR}║{R}  {DIM}To       :{R}  {W}{to}{R}")
                print(f"  {GR}╚══════════════════════════════════════════════════════╝{R}")
                # Save last text_id for status check
                with open(os.path.join(os.path.expanduser("~"), ".toolz_last_tid"), "w") as f:
                    f.write(tid)
            else:
                print(f"\n  {RE}╔══════════════════════════════════════════════════════╗{R}")
                print(f"  {RE}║  [✘] SEND FAILED                                     ║{R}")
                print(f"  {RE}║{R}  {DIM}Reason:{R}  {YL}{str(err)[:48]}{R}")
                if "quota" in str(err).lower() or "limit" in str(err).lower():
                    print(f"  {RE}║{R}  {DIM}Tip   :{R}  {DIM}Free key allows 1 SMS/day. Get paid key at textbelt.com{R}")
                print(f"  {RE}╚══════════════════════════════════════════════════════╝{R}")
            pause()

        # ── Status check ──
        elif ch == "2":
            tid_file = os.path.join(os.path.expanduser("~"), ".toolz_last_tid")
            tid = ""
            if os.path.isfile(tid_file):
                with open(tid_file) as f: tid = f.read().strip()
            if not tid:
                print(f"\n  {YL}[~] No recent SMS text ID found. Send an SMS first.{R}")
                pause(); continue
            spinner("Checking delivery status", 1.5, TL)
            status = sms_status(tid)
            STATUS_COLOR = {
                "DELIVERED": GR, "SENT": CY, "SENDING": YL,
                "FAILED": RE, "UNKNOWN": K,
            }
            sc = STATUS_COLOR.get(status, K)
            print(f"\n  {K}┌────────────────────────────────────────┐{R}")
            print(f"  {K}│{R}  {DIM}Text ID :{R}  {CY}{tid}{R}")
            print(f"  {K}│{R}  {DIM}Status  :{R}  {sc}{BD}{status}{R}")
            print(f"  {K}└────────────────────────────────────────┘{R}")
            pause()

        # ── Quota check ──
        elif ch == "3":
            if key == "textbelt":
                print(f"\n  {YL}[~] Free key allows 1 SMS per day.{R}")
                print(f"  {DIM}    Get a paid key at https://textbelt.com{R}")
            else:
                spinner("Checking quota", 1.0, TL)
                q = sms_quota(key)
                if q is not None:
                    qc = GR if q>10 else YL if q>0 else RE
                    print(f"\n  {K}┌──────────────────────────────┐{R}")
                    print(f"  {K}│{R}  {DIM}Quota remaining:{R}  {qc}{BD}{q} SMS{R}")
                    print(f"  {K}└──────────────────────────────┘{R}")
                else:
                    print(f"\n  {RE}[✘] Could not fetch quota. Check your key.{R}")
            pause()

        # ── Set paid key ──
        elif ch == "4":
            print(f"\n  {DIM}Get your API key at https://textbelt.com{R}")
            new_key = input(f"  {GD}Enter paid API key:{R} ").strip()
            if new_key:
                save_sms_key(new_key)
                key = new_key
                print(f"\n  {GR}[✔] Key saved.{R}")
            else:
                print(f"\n  {YL}[~] No key entered.{R}")
            pause()

        # ── Reset to free key ──
        elif ch == "5":
            save_sms_key("textbelt")
            key = "textbelt"
            print(f"\n  {YL}[✔] Reset to free key (1 SMS/day).{R}")
            pause()

        elif ch == "0":
            break
        else:
            print(f"\n  {RE}[✘] Invalid option.{R}"); time.sleep(0.8)


# ═══════════════════════════════════════════════
#  LOGOS
# ═══════════════════════════════════════════════
def logo_main():
    print(f"""{RE}
  ████████╗ ██████╗  ██████╗ ██╗     ███████╗
  ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ╚══███╔╝
     ██║   ██║   ██║██║   ██║██║       ███╔╝ 
     ██║   ██║   ██║██║   ██║██║      ███╔╝  
     ██║   ╚██████╔╝╚██████╔╝███████╗███████╗
     ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝{R}
{K}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{R}
{OR}       ☠   A D V A N C E D   T O O L K I T   ☠{R}
{K}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{R}
{DIM}       github.com/00xk/Toolz  │  v5.0  │  Linux & Termux{R}
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
    print(f"""{PU}  ╔══════════════════════════════════════════════════════╗
  ║         S H E R L O C K   O S I N T              ║
  ║      "When you eliminate the impossible..."       ║
  ╚══════════════════════════════════════════════════╝{R}
{K}  ┌──────────────────────────────────────────────────────┐{R}
{GR}  │{W}  ✦ 400+ platforms  ✦ Batch mode  ✦ Export to file  {GR}│{R}
{K}  └──────────────────────────────────────────────────────┘{R}
""")

def logo_ip():
    print(f"""
{LB}  ██╗██████╗     ████████╗██████╗  █████╗  ██████╗███████╗██████╗
  ██║██╔══██╗    ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗
  ██║██████╔╝       ██║   ██████╔╝███████║██║     █████╗  ██████╔╝
  ██║██╔═══╝        ██║   ██╔══██╗██╔══██║██║     ██╔══╝  ██╔══██╗
  ██║██║            ██║   ██║  ██║██║  ██║╚██████╗███████╗██║  ██║
  ╚═╝╚═╝            ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚══════╝╚═╝  ╚═╝{R}
{K}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{R}
{LB}            🌐  IP GEOLOCATION & TRACE ENGINE{R}
{K}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{R}
{K}  ┌──────────────────────────────────────────────────────────┐{R}
{LG}  │{W}  ✦ Country · City · ISP  ✦ ASN  ✦ Lat/Lon · Timezone  {LG}│{R}
{K}  └──────────────────────────────────────────────────────────┘{R}
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
{K}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{R}
{PK}        📱  MOBILE NUMBER OSINT + SMS ENGINE{R}
{K}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{R}
{K}  ┌──────────────────────────────────────────────────────┐{R}
{PK}  │{W}  ✦ Carrier · Region · Line type  ✦ Deep OSINT scan  {PK}│{R}
{PK}  │{W}  ✦ Anonymous SMS sender via Textbelt API            {PK}│{R}
{K}  └──────────────────────────────────────────────────────┘{R}
""")


# ═══════════════════════════════════════════════
#  MODULE: SHERLOCK
# ═══════════════════════════════════════════════
def mod_sherlock():
    if not shutil.which("sherlock"):
        install_sherlock()

    while True:
        clr(); logo_sherlock()
        print(f"""{K}  ┌─  Mode ───────────────────────────────────────────────┐{R}
  {GR}[1]{W}   ➤  Single username scan                        {K}│{R}
  {GR}[2]{W}   ➤  Batch scan from file                        {K}│{R}
  {GR}[3]{W}   ➤  Scan & save results to .txt                 {K}│{R}
  {RE}[0]{W}   ➤  Back                                        {K}│{R}
{K}  └──────────────────────────────────────────────────────┘{R}
""")
        ch = input(f"  {PU}▶{R} ").strip()

        if ch == "1":
            u = input(f"\n  {YL}Target username:{R} ").strip()
            if not u: continue
            print(f"\n  {K}┌──────────────────────────────────────────────────┐{R}")
            print(f"  {K}│{R}  {DIM}Target :{R}  {YL}{u}{R}")
            print(f"  {K}│{R}  {DIM}Engine :{R}  {W}Sherlock  ·  400+ platforms{R}")
            print(f"  {K}└──────────────────────────────────────────────────┘{R}")
            spinner("Scanning", 1.0, PU)
            print(f"\n  {GR}[✔] Results:\n{R}"); ln(PU); print()
            os.system(f"sherlock {u}")
            print(); ln(PU); pause()

        elif ch == "2":
            path = input(f"\n  {YL}File path (one username per line):{R} ").strip()
            if not os.path.exists(path):
                print(f"\n  {RE}[✘] Not found: {path}{R}"); pause(); continue
            with open(path) as f:
                users = [l.strip() for l in f if l.strip()]
            print(f"\n  {CY}[+] {len(users)} target(s) loaded{R}\n"); time.sleep(0.5)
            for i,u in enumerate(users,1):
                print(f"\n  {PU}══[ {i}/{len(users)} ]══ {YL}{u}{PU} {'═'*20}{R}")
                os.system(f"sherlock {u}"); print()
            pause(f"[✔] Batch complete. Press Enter...")

        elif ch == "3":
            u = input(f"\n  {YL}Username:{R} ").strip()
            if not u: continue
            out = f"{u}_sherlock.txt"
            spinner("Scanning & exporting", 1.5, PU)
            os.system(f"sherlock {u} --output {out}")
            print(f"\n  {GR}[✔] Saved →{R}  {CY}{out}{R}"); pause()

        elif ch == "0": break
        else: print(f"\n  {RE}[✘] Invalid.{R}"); time.sleep(0.8)


# ═══════════════════════════════════════════════
#  MODULE: IP TRACER
# ═══════════════════════════════════════════════
def mod_ip():
    cmd = next((c for c in ["trace","ip-tracer"] if shutil.which(c)), None)

    if not cmd:
        clr(); logo_ip()
        print(f"  {YL}[!] IP-Tracer not installed.{R}\n")
        print(f"  {GR}[1]{W} Auto-install    {RE}[0]{W} Back{R}\n")
        if input(f"  {LB}▶{R} ").strip() == "1":
            install_ip_tracer()
            cmd = next((c for c in ["trace","ip-tracer"] if shutil.which(c)), None)
        if not cmd: return

    while True:
        clr(); logo_ip()
        print(f"""{K}  ┌─  Mode ───────────────────────────────────────────────┐{R}
  {GR}[1]{W}   ➤  Trace my own IP                            {K}│{R}
  {GR}[2]{W}   ➤  Trace target IP address                    {K}│{R}
  {GR}[3]{W}   ➤  Batch trace from file                      {K}│{R}
  {RE}[0]{W}   ➤  Back                                        {K}│{R}
{K}  └──────────────────────────────────────────────────────┘{R}
""")
        ch = input(f"  {LB}▶{R} ").strip()

        if ch == "1":
            spinner("Fetching your IP", 1.2, LB)
            print(f"\n  {LG}[✔] Result:\n{R}"); ln(LB); print()
            os.system(f"{cmd} -m")
            print(); ln(LB); pause()

        elif ch == "2":
            ip = input(f"\n  {YL}Target IP:{R} ").strip()
            if not ip: continue
            if not valid_ip(ip):
                print(f"\n  {RE}[✘] Invalid IP. Format: xxx.xxx.xxx.xxx{R}"); pause(); continue
            print(f"\n  {K}┌──────────────────────────────────────────────────┐{R}")
            print(f"  {K}│{R}  {DIM}Target :{R}  {YL}{ip}{R}")
            print(f"  {K}│{R}  {DIM}Engine :{R}  {W}IP-Tracer  ·  ip-api.com{R}")
            print(f"  {K}└──────────────────────────────────────────────────┘{R}")
            spinner(f"Tracing {ip}", 1.5, LB)
            print(f"\n  {LG}[✔] Result:\n{R}"); ln(LB); print()
            os.system(f"{cmd} -t {ip}")
            print(); ln(LB); pause()

        elif ch == "3":
            path = input(f"\n  {YL}File path (one IP per line):{R} ").strip()
            if not os.path.exists(path):
                print(f"\n  {RE}[✘] Not found: {path}{R}"); pause(); continue
            with open(path) as f:
                ips = [l.strip() for l in f if l.strip()]
            print(f"\n  {CY}[+] {len(ips)} IP(s) loaded{R}\n"); time.sleep(0.4)
            for i,ip in enumerate(ips,1):
                print(f"\n  {LB}══[ {i}/{len(ips)} ]══ {YL}{ip}{LB} {'═'*20}{R}")
                os.system(f"{cmd} -t {ip}"); print(); time.sleep(0.4)
            pause("[✔] Batch complete. Press Enter...")

        elif ch == "0": break
        else: print(f"\n  {RE}[✘] Invalid.{R}"); time.sleep(0.8)


# ═══════════════════════════════════════════════
#  MODULE: PHONE OSINT + SMS
# ═══════════════════════════════════════════════
def mod_phone():
    home   = os.path.expanduser("~")
    pif_py = os.path.join(home, "PhoneInfoga", "phoneinfoga.py")

    while True:
        clr(); logo_phone()
        pif_ok = os.path.isfile(pif_py)
        pif_status = f"{GR}Installed{R}" if pif_ok else f"{RE}Not installed{R}"

        print(f"""{K}  ┌─  Mode ───────────────────────────────────────────────┐{R}
  {PK}[1]{W}   ➤  Quick scan    (offline · instant)           {K}│{R}
  {PK}[2]{W}   ➤  Deep scan     (PhoneInfoga)  [{pif_status}{W}]    {K}│{R}
  {PK}[3]{W}   ➤  Full scan     (quick + deep combined)       {K}│{R}
  {PK}[4]{W}   ➤  Batch scan    (file of numbers)             {K}│{R}
  {TL}[5]{W}   ➤  Send SMS      (anonymous · international)   {K}│{R}
  {GD}[6]{W}   ➤  Install / Reinstall PhoneInfoga             {K}│{R}
  {RE}[0]{W}   ➤  Back                                        {K}│{R}
{K}  └──────────────────────────────────────────────────────┘{R}
""")
        ch = input(f"  {PK}▶{R} ").strip()

        # ── Quick scan ──
        if ch == "1":
            n = norm_phone(input(f"\n  {YL}Number (e.g. +971501234567):{R} "))
            if not n: continue
            spinner("Parsing number", 0.8, PK)
            show_phone_info(phone_parse(n), n)
            pause()

        # ── Deep scan ──
        elif ch == "2":
            if not pif_ok:
                print(f"\n  {YL}[!] PhoneInfoga not installed. Use option [6].{R}"); pause(); continue
            n = norm_phone(input(f"\n  {YL}Number (e.g. +971501234567):{R} "))
            if not n: continue
            print(f"\n  {K}┌──────────────────────────────────────────────────┐{R}")
            print(f"  {K}│{R}  {DIM}Target :{R}  {GD}{n}{R}")
            print(f"  {K}│{R}  {DIM}Engine :{R}  {W}PhoneInfoga · Search fingerprinting{R}")
            print(f"  {K}└──────────────────────────────────────────────────┘{R}")
            spinner("Deep scanning", 1.5, PK)
            print(f"\n  {LG}[✔] Results:\n{R}"); ln(PK); print()
            os.system(f"python3 {pif_py} -n {n}")
            print(); ln(PK); pause()

        # ── Full scan ──
        elif ch == "3":
            n = norm_phone(input(f"\n  {YL}Number (e.g. +971501234567):{R} "))
            if not n: continue
            spinner("Quick parse", 0.8, PK)
            info = phone_parse(n)
            show_phone_info(info, n)
            if info and not info.get("valid"):
                pause(); continue
            if pif_ok:
                print(f"  {PK}[ Phase 2 ]  PhoneInfoga deep scan...{R}\n")
                spinner("Deep scanning", 1.2, PK)
                print(f"\n  {LG}[✔] Results:\n{R}"); ln(PK); print()
                os.system(f"python3 {pif_py} -n {n}")
                print(); ln(PK)
            else:
                print(f"  {YL}[~] PhoneInfoga not installed — skipping deep scan. Use [6].{R}")
            pause()

        # ── Batch ──
        elif ch == "4":
            path = input(f"\n  {YL}File path (one number per line):{R} ").strip()
            if not os.path.exists(path):
                print(f"\n  {RE}[✘] Not found: {path}{R}"); pause(); continue
            with open(path) as f:
                nums = [norm_phone(l) for l in f if l.strip()]
            print(f"\n  {CY}[+] {len(nums)} number(s) loaded{R}\n"); time.sleep(0.4)
            for i,n in enumerate(nums,1):
                print(f"\n  {PK}══[ {i}/{len(nums)} ]══ {GD}{n}{PK} {'═'*15}{R}")
                show_phone_info(phone_parse(n), n)
                if pif_ok:
                    os.system(f"python3 {pif_py} -n {n}")
                ln(PK); print(); time.sleep(0.3)
            pause("[✔] Batch done. Press Enter...")

        # ── SMS Sender ──
        elif ch == "5":
            sms_module()

        # ── Install PhoneInfoga ──
        elif ch == "6":
            install_phoneinfoga()
            pif_ok = os.path.isfile(pif_py)

        elif ch == "0": break
        else: print(f"\n  {RE}[✘] Invalid.{R}"); time.sleep(0.8)


# ═══════════════════════════════════════════════
#  MODULE: UPDATE
# ═══════════════════════════════════════════════
def mod_update():
    clr()
    print(f"""
  {PU}╔══════════════════════════════════════════════════╗
  ║            F O R C E   U P D A T E              ║
  ╚══════════════════════════════════════════════════╝{R}
""")
    home = os.path.expanduser("~")
    tool_dir = os.path.join(home, "Toolz")
    steps = [
        (f"  {YL}[1/3] Removing old version...{R}",
         lambda: os.system(f"rm -rf {tool_dir}") if os.path.exists(tool_dir) else None),
        (f"  {CY}[2/3] Cloning latest version...{R}",
         lambda: os.system(f"cd {home} && git clone https://github.com/00xk/Toolz.git -q")),
        (f"  {GR}[3/3] Finalizing...{R}", lambda: None),
    ]
    for msg,fn in steps:
        print(msg); fn(); time.sleep(0.9)
    print(f"\n  {GR}[✔] Updated to latest version!{R}\n")
    time.sleep(1.5)
    os.system(f"cd {tool_dir} && python3 toolz.py")
    sys.exit(0)


# ═══════════════════════════════════════════════
#  MAIN MENU
# ═══════════════════════════════════════════════
def main_menu():
    print(f"""{K}  ╔═══════════════════════════════════════════════════════╗
  ║               M A I N   M E N U                    ║
  ╠═══════════════════════════════════════════════════════╣
  ║                                                     ║
  ║   {GR}[1]{W}   🔍  Sherlock OSINT    Username Hunt         {K}║
  ║   {LB}[2]{W}   🌐  IP Tracer         Geolocation           {K}║
  ║   {PK}[3]{W}   📱  Phone OSINT       Number Intel + SMS    {K}║
  ║   {PU}[4]{W}   🔄  Update Tool       Pull Latest           {K}║
  ║   {RE}[0]{W}   ✖   Exit                                    {K}║
  ║                                                     ║
  ╚═══════════════════════════════════════════════════════╝{R}
""")

def main():
    while True:
        clr(); logo_main(); main_menu()
        ch = input(f"  {CY}▶{R} ").strip()
        if   ch == "1": mod_sherlock()
        elif ch == "2": mod_ip()
        elif ch == "3": mod_phone()
        elif ch == "4": mod_update()
        elif ch == "0":
            clr()
            print(f"\n  {CY}Stay curious. Stay ethical.{R}  {DIM}Goodbye 👋{R}\n")
            sys.exit(0)
        else:
            print(f"\n  {RE}[✘] Invalid — choose 0 to 4.{R}"); time.sleep(0.9)

if __name__ == "__main__":
    main()
