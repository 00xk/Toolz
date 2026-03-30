#!/usr/bin/env python3
import os, time, shutil, sys

# COLORS
RED="\033[1;31m"; GREEN="\033[1;32m"; YELLOW="\033[1;33m"
CYAN="\033[1;36m"; WHITE="\033[1;37m"; PURPLE="\033[1;35m"
GRAY="\033[1;90m"; RESET="\033[0m"

def clear(): os.system("clear")

# ================= LOGO =================
def logo():
    print(f"""{RED}
████████╗ ██████╗  ██████╗ ██╗     ███████╗
╚══██╔══╝██╔═══██╗██╔═══██╗██║     ╚══███╔╝
   ██║   ██║   ██║██║   ██║██║       ███╔╝
   ██║   ██║   ██║██║   ██║██║      ███╔╝
   ██║   ╚██████╔╝╚██████╔╝███████╗███████╗
   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝{RESET}

{CYAN}☠ Advanced OSINT Toolkit ☠{RESET}
""")

# ================= SAFE INSTALL =================
def install(pkg):
    os.system(f"python3 -m pip install {pkg} -q")

# ================= PHONE HELPERS =================
def detect_device_info(info):
    carrier = (info.get("carrier") or "").lower()
    if "etisalat" in carrier or "vodafone" in carrier:
        return "🤖 Android (likely)"
    return "❓ Unknown"

def advanced_phone_analysis(info):
    line = info.get("line_type","")
    voip = "Yes" if "voip" in line.lower() else "No"
    risk = "🟢 Low" if "mobile" in line.lower() else "🟡 Medium"
    return voip, risk

def social_scan(num):
    num = num.replace("+","")
    print(f"\n{CYAN}SOCIAL:{RESET}")
    print(f" WhatsApp → https://wa.me/{num}")
    print(f" Telegram → https://t.me/{num}")

# ================= PHONE =================
def phone():
    try:
        import phonenumbers
        from phonenumbers import geocoder, carrier, number_type
    except:
        install("phonenumbers")
        return

    while True:
        clear()
        print(f"{CYAN}PHONE OSINT{RESET}")
        print("[1] Scan number")
        print("[0] Back")

        c=input(">> ")

        if c=="1":
            n=input("Number (+...): ")

            try:
                num=phonenumbers.parse(n)
                if not phonenumbers.is_valid_number(num):
                    print("Invalid")
                    input()
                    continue

                region=geocoder.description_for_number(num,"en")
                carr=carrier.name_for_number(num,"en")
                line=str(number_type(num))

                info={
                    "region":region,
                    "carrier":carr,
                    "line_type":line
                }

                device=detect_device_info(info)
                voip,risk=advanced_phone_analysis(info)

                print(f"""
Number: {n}
Region: {region}
Carrier: {carr}
Type: {line}
Device: {device}
VoIP: {voip}
Risk: {risk}
""")

                social_scan(n)

            except Exception as e:
                print("Error:",e)

            input("\nEnter...")

        else: break

# ================= SHERLOCK =================
def sherlock():
    if shutil.which("sherlock") is None:
        install("sherlock-project")

    u=input("Username: ")
    os.system(f"sherlock {u}")
    input("Enter...")

# ================= SMS =================
def sms():
    try:
        from twilio.rest import Client
    except:
        install("twilio")
        try:
            from twilio.rest import Client
        except:
            print("Install failed")
            input()
            return

    sid=input("SID: ")
    token=input("TOKEN: ")
    fromn=input("FROM: ")
    to=input("TO: ")
    msg=input("MSG: ")

    try:
        c=Client(sid,token)
        m=c.messages.create(body=msg,from_=fromn,to=to)
        print("Sent:",m.sid)
    except Exception as e:
        print("Error:",e)

    input("Enter...")

# ================= UPDATE =================
def update():
    home=os.path.expanduser("~")
    tool=os.path.join(home,"Toolz")

    os.system(f"rm -rf {tool}")
    os.system(f"cd {home} && git clone https://github.com/00xk/Toolz.git")
    os.system(f"cd {tool} && python3 toolz.py")
    exit()

# ================= MENU =================
def menu():
    print("""
[1] Sherlock
[2] Phone OSINT
[3] SMS Sender
[4] Update
[0] Exit
""")

# ================= MAIN =================
def main():
    while True:
        clear(); logo(); menu()
        c=input(">> ")

        if c=="1": sherlock()
        elif c=="2": phone()
        elif c=="3": sms()
        elif c=="4": update()
        elif c=="0": break
        else:
            print("Invalid")
            time.sleep(1)

if __name__=="__main__":
    main()
