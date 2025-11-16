import os
import subprocess
import time
import sys
import random
from colorama import Fore, Style, init
init(autoreset=True)

def show_ascii():
    RED = "\033[91m"
    RESET = "\033[0m"

    ascii_art = f"""{RED}


                     ▒███████▒  █████   ██▀███   ██▓ ██▓███   ██▓███  ▓█████  ██▀███  
                     ▒ ▒ ▒ ▄▀░▒██▓  ██▒▓██ ▒ ██▒▓██▒▓██░  ██▒▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒
                     ░ ▒ ▄▀▒░ ▒██▒  ██░▓██ ░▄█ ▒▒██▒▓██░ ██▓▒▓██░ ██▓▒▒███   ▓██ ░▄█ ▒
                       ▄▀▒   ░░██  █▀ ░▒██▀▀█▄  ░██░▒██▄█▓▒ ▒▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄  
                     ▒███████▒░▒███▒█▄ ░██▓ ▒██▒░██░▒██▒ ░  ░▒██▒ ░  ░░▒████▒░██▓ ▒██▒
                     ░▒▒ ▓░▒░▒░░ ▒▒░ ▒ ░ ▒▓ ░▒▓░░▓  ▒▓▒░ ░  ░▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
                     ░░▒ ▒ ░ ▒ ░ ▒░  ░   ░▒ ░ ▒░ ▒ ░░▒ ░     ░▒ ░      ░ ░  ░  ░▒ ░ ▒░
                     ░ ░ ░ ░ ░   ░   ░   ░░   ░  ▒ ░░░       ░░          ░     ░░   ░ 
                       ░ ░        ░       ░      ░                       ░  ░   ░     
                     ░                                                                


{RESET}"""

    print(ascii_art)


def run_command(command):
    print("\n" + Fore.RED + "[" + Style.RESET_ALL + "+" + Fore.RED + "]" + Style.RESET_ALL + "Start:".join(command))
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Fehler beim Ausführen des Befehls: {e}")
    input("\n" + Fore.RED + "[" + Style.RESET_ALL + "+" + Fore.RED + "]" + Style.RESET_ALL + "Scan complete. Press [Enter] to return to the main menu...")

def amass_menu():
    os.system("clear")
    show_ascii()
    valid = True
    print(Fore.RED.ljust(34) + "┌----------------------┐")
    print(Fore.RED + "┌----------------------------│" + Style.RESET_ALL + "---AMASS-CATEGORIES---" + Fore.RED + "│" + "-------------┐")
    print(Fore.RED + "│".ljust(29) + "└----------------------┘".ljust(37) + "│")
    print(Fore.RED + "├" + "[" +  Style.RESET_ALL + "1" + Fore.RED + "]" + Style.RESET_ALL +"-Subdomain Enumeration")
    print(Fore.RED + "├" + "[" + Style.RESET_ALL + "2" + Fore.RED + "]" + Style.RESET_ALL + "-Information-Gathering")
    print(Fore.RED + "├" + "[" + Style.RESET_ALL + "3" + Fore.RED + "]" + Style.RESET_ALL + "-View local database")
    print(Fore.RED + "├" + "[" + Style.RESET_ALL + "4" + Fore.RED + "]" + Style.RESET_ALL + "-Visualization in graph form")
    print(Fore.RED + "├" + "[" + Style.RESET_ALL + "5" + Fore.RED + "]" + Style.RESET_ALL + "-Custom")
    print(Fore.RED + "├" + "[" + Style.RESET_ALL + "0" + Fore.RED + "]" + Style.RESET_ALL + "-Back to the Main Menu")

    print("\n" * 3)
    choice = input(Fore.RED + "[" + Style.RESET_ALL + "+" + Fore.RED + "]" + Style.RESET_ALL + "Choose Category: ")

    if choice == "1":
        domain = input(Fore.RED + "[" + Style.RESET_ALL + "+" + Fore.RED + "]" + Style.RESET_ALL + "Target-Domain: ")
        run_command(["amass", "enum", "-d", domain])

    elif choice == "2":
        domain = input(Fore.RED + "[" + Style.RESET_ALL + "+" + Fore.RED + "]" + Style.RESET_ALL + "Target-Domain: ")
        run_command(["amass", "intel", "-d", domain, "-whois"])
    elif choice == "3":
        domain = input(Fore.RED + "[" + Style.RESET_ALL + "+" + Fore.RED + "]" + Style.RESET_ALL + "Target-Domain: ")
        run_command(["amass", "db", "-show", domain])
    elif choice == "4":
        domain = input(Fore.RED + "[" + Style.RESET_ALL + "+" + Fore.RED + "]" + Style.RESET_ALL + "Target-Domain: ")
        run_command(["amass", "viz", "-d3", "-dir", "~/.config/amass/"])
    elif choice == "5":
        args = input(Fore.RED + "[" + Style.RESET_ALL + "+" + Fore.RED + "]" + Style.RESET_ALL + "AMASS-args: ")
        run_command(["amass"] + args.split())

    elif choice == "0":
        input("\n" + Fore.RED + "[" + Style.RESET_ALL + "+" + Fore.RED + "]" + Style.RESET_ALL + "Press [Enter] to return to the main menu...")
        return


    else:
        print(Fore.RED + "[" + Style.RESET_ALL + "+" + Fore.RED + "]" + Style.RESET_ALL + "Invalid selection.")

def nmap_menu():
    os.system("clear")
    show_ascii()
    args = ""
    valid = True
    print(Fore.RED.ljust(33) + "┌---------------------┐")
    print(Fore.RED + "┌---------------------------" + "│" + Style.RESET_ALL + "---NMAP-CATEGORIES---" + Fore.RED + "│-----------------┐")
    print(Fore.RED + "│".ljust(28) + "└---------------------┘".ljust(40) + "│")
    print(Fore.RED + "├" + "[" + Style.RESET_ALL + "1" + Fore.RED + "]" + Style.RESET_ALL + "-Simple port scan")
    print(Fore.RED + "├" + "[" + Style.RESET_ALL + "2" + Fore.RED + "]" + Style.RESET_ALL + "-OS detection")
    print(Fore.RED + "├" + "[" + Style.RESET_ALL + "3" + Fore.RED + "]" + Style.RESET_ALL + "-Ping Sweep")
    print(Fore.RED + "├" + "[" + Style.RESET_ALL + "4" + Fore.RED + "]" + Style.RESET_ALL + "-Version scan")
    print(Fore.RED + "├" + "[" + Style.RESET_ALL + "5" + Fore.RED + "]" + Style.RESET_ALL + "-Combine all options")
    print(Fore.RED + "├" + "[" + Style.RESET_ALL + "6" + Fore.RED + "]" + Style.RESET_ALL + "-Custom")
    print(Fore.RED + "├" + "[" + Style.RESET_ALL + "0" + Fore.RED + "]" + Style.RESET_ALL + "-Back to the main menu")

    print("\n" * 3)
    choice = input(Fore.RED + "[" + Style.RESET_ALL + "+" + Fore.RED + "]" + Style.RESET_ALL + "Select category:")

    if choice == "0":
        input("\n" + Fore.RED + "[" + Style.RESET_ALL + "+" + Fore.RED + "]" + Style.RESET_ALL + "Press [Enter] to return to the main menu...")
        return


    elif choice in["1", "2", "3", "4"]:
        target = input(Fore.RED + "[" + Style.RESET_ALL + "+" + Fore.RED + "]" + Style.RESET_ALL + "Target-IP/Domain: ")
    elif choice == "1":
        run_command(["nmap", target])
    elif choice == "2":
        run_command(["nmap", "-O", target])
    elif choice == "3":
        run_command(["nmap", "-sn", target])
    elif choice == "4":
        run_command(["nmap", "-sV", target])
    elif choice == "5":
        os.system("clear")
        show_ascii()
        print(Fore.RED.ljust(29) + "┌-------------------------┐")
        print(Fore.RED + "┌-----------------------│" + Style.RESET_ALL + "---Available options---" + Fore.RED + "│----------------┐")
        print(Fore.RED + "│".ljust(24) + "└-------------------------┘".ljust(43) + "│")
        print(Fore.RED + "├" + "[" + Style.RESET_ALL + "1" + Fore.RED + "]" + Style.RESET_ALL + "-sS (SYN-Scan)")
        print(Fore.RED + "├" + "[" + Style.RESET_ALL + "2" + Fore.RED + "]" + Style.RESET_ALL + "-sT (TCP Connect)")
        print(Fore.RED + "├" + "[" + Style.RESET_ALL + "3" + Fore.RED + "]" + Style.RESET_ALL + "-sU (UDP Scan)")
        print(Fore.RED + "├" + "[" + Style.RESET_ALL + "4" + Fore.RED + "]" + Style.RESET_ALL + "-p (Specify ports)")
        print(Fore.RED + "├" + "[" + Style.RESET_ALL + "5" + Fore.RED + "]" + Style.RESET_ALL + "-A (Everything: OS, versions, scripts)")
        print(Fore.RED + "├" + "[" + Style.RESET_ALL + "6" + Fore.RED + "]" + Style.RESET_ALL + "-Pn (Disable ping)")
        print(Fore.RED + "├" + "[" + Style.RESET_ALL + "7" + Fore.RED + "]" + Style.RESET_ALL + "--script (NSE-Scripts)")
        print(Fore.RED + "├" + "[" + Style.RESET_ALL + "0" + Fore.RED + "]" + Style.RESET_ALL + "Back to the main Menu")
        print("\n" * 3)
        sub_choices = input(Fore.RED + "[" + Style.RESET_ALL + "+" + Fore.RED + "]" + Style.RESET_ALL + "Options: ").split()

        if "0" in sub_choices:
            print(Fore.RED + "[" + Style.RESET_ALL + "+" + Fore.RED + "]" + Style.RESET_ALL + "Back to the main menu.")
            return

        target = input(Fore.RED + "[" + Style.RESET_ALL + "+" + Fore.RED + "]" + Style.RESET_ALL + "target IP/Domain: ")
        args = []
        valid = True
        for sc in sub_choices :
            if sc == "1":
                args.append("-sS")
            elif sc == "2":
                args.append("-sT")
            elif sc == "3":
                args.append("-sU")
            elif sc == "4":
                ports = input("Ports: ")
                args.extend(["-p", ports])
            elif sc == "5":
                args.append("-A")
            elif sc == "6":
                args.append("-Pn")
            elif sc == "7":
                script = input(Fore.RED + "[" + Style.RESET_ALL + "+" + Fore.RED + "]" + Style.RESET_ALL + "Script (e.g., default, vuln):")
                args.extend(["--script", script])
            else:
                print(Fore.RED + "[" + Style.RESET_ALL + "+" + Fore.RED + "]" + Style.RESET_ALL + "Invalid command:", sc)
                valid = False
                break
    if valid:
        args = args.split() if isinstance(args, str) else args
        run_command(["nmap"] + args + [target])

def sqlmap_menu():
    os.system("clear")
    show_ascii()
    print(Fore.RED.ljust(33) + "┌-----------------------┐")
    print(Fore.RED + "┌---------------------------" + "│" + Style.RESET_ALL + "---SQLMAP-CATEGORIES---" + Fore.RED + "│-----------------┐")
    print(Fore.RED + "│".ljust(28) + "└-----------------------┘".ljust(42) + "│")
    print(Fore.RED + "├" + "[" + Style.RESET_ALL + "1" + Fore.RED + "]" + Style.RESET_ALL + "-Simple test")
    print(Fore.RED + "├" + "[" + Style.RESET_ALL + "2" + Fore.RED + "]" + Style.RESET_ALL + "-DB-Dump")
    print(Fore.RED + "├" + "[" + Style.RESET_ALL + "3" + Fore.RED + "]" + Style.RESET_ALL + "-Custom")
    print(Fore.RED + "├" + "[" + Style.RESET_ALL + "0" + Fore.RED + "]" + Style.RESET_ALL + "-Back to the main menu")

    print("\n" * 3)
    choice = input(Fore.RED + "[" + Style.RESET_ALL + "+" + Fore.RED + "]" + Style.RESET_ALL + "Select category:")

    if choice == "0":
       input("\n" + Fore.RED + "[" + Style.RESET_ALL + "+" + Fore.RED + "]" + Style.RESET_ALL + "Press [Enter] to return to the main menu...")
       return
    elif choice in ["1", "2", "3"]:
       url = input(Fore.RED + "[" + Style.RESET_ALL + "+" + Fore.RED + "]" + Style.RESET_ALL + "Target-URL: ")
       if url == "":
           input(Fore.RED + "[" + Style.RESET_ALL + "+" + Fore.RED + "]" + Style.RESET_ALL + "No URL entered. Press Enter...")
           return
    if choice == "1":
       run_command(["sqlmap", "-u", url, "--batch"])
    elif choice == "2":
       run_command(["sqlmap", "-u", url, "--dump", "--batch"])
    elif choice == "3":
       args = input("SQLMap-Args: ")
       run_command(["sqlmap"] + args.split() + ["-u", url])
    elif choice == "0":
       return
    else:
        print(Fore.RED + "[" + Style.RESET_ALL + "+" + Fore.RED + "]" + Style.RESET_ALL + "Unknown Choice")

def hydra_menu():
    os.system("clear")
    show_ascii()
    print(Fore.RED.ljust(28) + "┌----------------------┐")
    print(Fore.RED + "┌----------------------" + "│" + Style.RESET_ALL + "---HYDRA-CATEGORIES---" + Fore.RED + "│" + "-----------------┐")
    print(Fore.RED + "│".ljust(23) + "└----------------------┘".ljust(41) + "│")
    print(Fore.RED + "├" + "[" + Style.RESET_ALL + "1" + Fore.RED + "]" + Style.RESET_ALL + "-SSH Brute-Force")
    print(Fore.RED + "├" + "[" + Style.RESET_ALL + "2" + Fore.RED + "]" + Style.RESET_ALL + "-HTTP-Login")
    print(Fore.RED + "├" + "[" + Style.RESET_ALL + "3" + Fore.RED + "]" + Style.RESET_ALL + "-FTP-Login")
    print(Fore.RED + "├" + "[" + Style.RESET_ALL + "4" + Fore.RED + "]" + Style.RESET_ALL + "-RDP-Login")
    print(Fore.RED + "├" + "[" + Style.RESET_ALL + "5" + Fore.RED + "]" + Style.RESET_ALL + "-MySQL-Login")
    print(Fore.RED + "├" + "[" + Style.RESET_ALL + "6" + Fore.RED + "]" + Style.RESET_ALL + "-Custom")
    print(Fore.RED + "├" + "[" + Style.RESET_ALL + "0" + Fore.RED + "]" + Style.RESET_ALL + "-Back to the main menu")

    print("\n" * 3)
    choice = input(Fore.RED + "[" + Style.RESET_ALL + "+" + Fore.RED + "]" + Style.RESET_ALL + "Select category:")

    if choice == "0":
       input("\n" + Fore.RED + "[" + Style.RESET_ALL + "+" + Fore.RED + "]" + Style.RESET_ALL + "Press [Enter] to return to the main menu...")
       return

    target_needed =  ["1", "2", "3", "4", "5"]
    if choice in target_needed:
        target = input(Fore.RED + "[" + Style.RESET_ALL + "+" + Fore.RED + "]" + Style.RESET_ALL + "Target-IP: ")
        if not target:
           print("\n" + Fore.RED + "[" + Style.RESET_ALL + "+" + Fore.RED + "]" + Style.RESET_ALL + "No IP address entered. Press Enter...")
           return



    elif choice == "1":
           run_command(["hydra", "-L", "user.txt", "-P", "pass.txt", "ssh://" + target])
    elif choice == "2":
           run_command(["hydra", "-L", "user.txt", "-P", "pass.txt", f"http-get://{target}/login"])
    elif choice == "3":
           run_command(["hydra", "-L", "user.txt", "-P", "pass.txt", target, "ftp"])
    elif choice == "4":
           run_command(["hydra", "-L", "user.txt", "-P", "pass.txt", target, "rdp"])
    elif choice == "5":
           run_command(["hydra", "-L", "user.txt", "-P", "pass.txt", target, "mysql"])
    elif choice == "6":
           args = input("Hydra-Args: ")
           run_command(["hydra"] + args.split())
    else:
        print(Fore.RED + "[" + Style.RESET_ALL + "+" + Fore.RED + "]" + Style.RESET_ALL +  "Unknown Choice.")






def john_menu():
    os.system("clear")
    show_ascii()
    print(Fore.RED.ljust(31) + "┌---------------------┐")
    print(Fore.RED + "┌-------------------------" + "│" + Style.RESET_ALL + "---John-the-Ripper---" + Fore.RED + "│" + "-------------------┐")
    print(Fore.RED + "│".ljust(26) + "└---------------------┘".ljust(42) + "│")
    print(Fore.RED + "├" + "[" + Style.RESET_ALL + "1" + Fore.RED + "]" + Style.RESET_ALL + "-Cracking a password hash")
    print(Fore.RED + "├" + "[" + Style.RESET_ALL + "2" + Fore.RED + "]" + Style.RESET_ALL + "-Custom")
    print(Fore.RED + "├" + "[" + Style.RESET_ALL + "0" + Fore.RED + "]" + Style.RESET_ALL + "-Back to the main menu")

    print("\n" * 3)
    choice = input(Fore.RED + "[" + Style.RESET_ALL + "+" + Fore.RED + "]" + Style.RESET_ALL + "Choose Category: ")
    if choice == "0":
       input("\n" + Fore.RED + "[" + Style.RESET_ALL + "+" + Fore.RED + "]" + Style.RESET_ALL + "Press [Enter] to return to the main menu...")
       return
    elif choice == "1":
       file = input("Path to the hash file:")
       run_command(["john", file])
    elif choice == "2":
       args = input("John-Args: ")
       run_command(["john"] + args.split())
    else:
        print(Fore.RED + "[" + Style.RESET_ALL + "+" + Fore.RED + "]" + Style.RESET_ALL + "Unknown Choice.")

def ncrack_menu():
    os.system("clear")
    show_ascii()
    print(Fore.RED.ljust(29) + "┌------------┐")
    print(Fore.RED + "┌-----------------------" + "│" + Style.RESET_ALL + "---NCRACK---" + Fore.RED + "│" + "-----------------┐")
    print(Fore.RED + "│".ljust(24) + "└------------┘".ljust(31) + "│")
    print(Fore.RED + "├" + "[" + Style.RESET_ALL + "1" + Fore.RED + "]" + Style.RESET_ALL + "-SSH Brute-Force")
    print(Fore.RED + "├" + "[" + Style.RESET_ALL + "2" + Fore.RED + "]" + Style.RESET_ALL + "-Custom")
    print(Fore.RED + "├" + "[" + Style.RESET_ALL + "0" + Fore.RED + "]" + Style.RESET_ALL + "-Back to the main menu")

    print("\n" * 3)
    choice = input(Fore.RED + "[" + Style.RESET_ALL + "+" + Fore.RED + "]" + Style.RESET_ALL + "-Select category:")

    if choice == "0":
       input("\n" + Fore.RED + "[" + Style.RESET_ALL + "+" + Fore.RED + "]" + Style.RESET_ALL + "Press [Enter] to return to the main menu...")
       return

    elif choice in["1"]:
       target = input(Fore.RED + "[" + Style.RESET_ALL + "+" + Fore.RED + "]" + Style.RESET_ALL + "-Target-IP: ")
       if target == "":
           print("\n" + Fore.RED + "[" + Style.RESET_ALL + "+" + Fore.RED + "]" + Style.RESET_ALL + "No IP address entered. Press Enter...")
           return
    elif choice == "1":
       run_command(["ncrack", "-p", "22", target])
    elif choice == "2":
       args = input("Ncrack-Args: ")
       run_command(["ncrack"] + args.split())
    else:
        print(Fore.RED + "[" + Style.RESET_ALL + "+" + Fore.RED + "]" + Style.RESET_ALL + "Unknown Choice.")

def aircrack_menu():
    os.system("clear")
    show_ascii()
    print(Fore.RED.ljust(31) + "┌-----------------┐")
    print(Fore.RED + "┌-------------------------" + "│" + Style.RESET_ALL + "---AIRCRACK-NG---" + Fore.RED + "│" + "------------------┐")
    print(Fore.RED + "│".ljust(26) + "└-----------------┘".ljust(37) + "│")
    print(Fore.RED + "├" + "[" + Style.RESET_ALL + "1" + Fore.RED + "]" + Style.RESET_ALL + "-Crack .cap file containing wordlist")
    print(Fore.RED + "├" + "[" + Style.RESET_ALL + "2" + Fore.RED + "]" + Style.RESET_ALL + "-Custom")
    print(Fore.RED + "├" + "[" + Style.RESET_ALL + "0" + Fore.RED + "]" + Style.RESET_ALL + "-Back to the main Menu")

    print("\n" * 3)
    choice = input(Fore.RED + "[" + Style.RESET_ALL + "+" + Fore.RED + "]" + Style.RESET_ALL + "Select category: ")

    if choice == "0":
       input("\n" + Fore.RED + "[" + Style.RESET_ALL + "+" + Fore.RED + "]" + Style.RESET_ALL + "Press [Enter] to return to the main menu...")
       return

    elif choice == "1":
       cap = input(Fore.RED + "[" + Style.RESET_ALL + "+" + Fore.RED + "]" + Style.RESET_ALL + "Path to the .cap file: ")
       wordlist = input(Fore.RED + "[" + Style.RESET_ALL + "+" + Fore.RED + "]" + Style.RESET_ALL + "Path to the wordlist:")

       run_command(["aircrack-ng", "-w", wordlist, cap])
    elif choice == "2":
       args = input(Fore.RED + "[" + Style.RESET_ALL + "+" + Fore.RED + "]" + Style.RESET_ALL + "Aircrack-Args: ")
       run_command(["aircrack-ng"] + args.split())
    else:
        print(Fore.RED + "[" + Style.RESET_ALL + "+" + Fore.RED + "]" + Style.RESET_ALL + "Unknown Choice.")

def wireshark_menu():
    os.system("clear")
    show_ascii()
    print(Fore.RED.ljust(34) + "┌---------------┐")
    print(Fore.RED + "┌----------------------------" + "│" + Style.RESET_ALL + "---WIRESHARK---" + Fore.RED + "│" + "------------------┐")
    print(Fore.RED + "│".ljust(29) + "└---------------┘".ljust(35) + "│")
    print(Fore.RED + "├" + "[" + Style.RESET_ALL + "1" + Fore.RED + "]" + Style.RESET_ALL + "-Wireshark GUI")
    print(Fore.RED + "├" + "[" + Style.RESET_ALL + "2" + Fore.RED + "]" + Style.RESET_ALL + "-User-defined (tshark)")
    print(Fore.RED + "├" + "[" + Style.RESET_ALL + "0" + Fore.RED + "]" + Style.RESET_ALL + "-Back to the main menu")
    print("\n" * 3)
    choice = input(Fore.RED + "[" + Style.RESET_ALL + "+" + Fore.RED + "]" + Style.RESET_ALL + "Choose category: ")

    if choice == "0":
        input("\n" + Fore.RED + "[" + Style.RESET_ALL + "+" + Fore.RED + "]" + Style.RESET_ALL + "Press [Enter] to return to the main menu...")


    elif choice == "1":
       run_command(["wireshark"])
    elif choice == "2":
       args = input("tshark-Args: ")
       run_command(["tshark"] + args.split())
    else:
        print("Unknown Choice.")


def main_menu():
    os.system("clear")
    show_ascii()
    print(Fore.RED.ljust(17) + "┌" + "-----------------------" + "┐")
    print(Fore.RED + "┌-----------" + "│" + Style.RESET_ALL + "---BASIC-LINUX-TOOLS---" + Fore.RED + "│")
    print(Fore.RED + "│".ljust(12) + "└" + "-----------------------" + "┘")
    print(Fore.RED + "├" + "[" + Style.RESET_ALL + "1" + Fore.RED + "]" + Style.RESET_ALL + "-AMASS")
    print(Fore.RED + "├" + "[" + Style.RESET_ALL + "2" + Fore.RED + "]" + Style.RESET_ALL + "-Nmap")
    print(Fore.RED + "├" + "[" + Style.RESET_ALL + "3" + Fore.RED + "]" + Style.RESET_ALL + "-SQLMAP")
    print(Fore.RED + "├" + "[" + Style.RESET_ALL + "4" + Fore.RED + "]" + Style.RESET_ALL + "-HYDRA")
    print(Fore.RED + "├" + "[" + Style.RESET_ALL + "5" + Fore.RED + "]" + Style.RESET_ALL + "-JOHN-THE-RIPPER")
    print(Fore.RED + "├" + "[" + Style.RESET_ALL + "6" + Fore.RED + "]" + Style.RESET_ALL + "-NCRACK")
    print(Fore.RED + "├" + "[" + Style.RESET_ALL + "7" + Fore.RED + "]" + Style.RESET_ALL + "-AIRCRACK-NG")
    print(Fore.RED + "├" + "[" + Style.RESET_ALL + "8" + Fore.RED + "]" + Style.RESET_ALL + "-WIRESHARK")
    print(Fore.RED + "└" + "[" + Style.RESET_ALL + "9" + Fore.RED + "]" + Style.RESET_ALL + "-Quit")

    print("\n" * 3)
    choice = input(Fore.RED + "[" + Style.RESET_ALL + "+" + Fore.RED + "]" + Style.RESET_ALL + "Select Tool: ")

    if choice == "1":
       amass_menu()
    elif choice == "2":
       nmap_menu()
    elif choice == "3":
       sqlmap_menu()
    elif choice == "4":
        hydra_menu()
    elif choice == "5":
       john_menu()
    elif choice == "6":
       ncrack_menu()
    elif choice == "7":
       aircrack_menu()
    elif choice == "8":
       wireshark_menu()
    elif choice == "9":
       print(Fore.RED + "[" + Style.RESET_ALL + "+" + Fore.RED + "]" + Style.RESET_ALL + "Quitting...")
       exit()
    else:
        print("Unknown Choice.")



def main():
    try:
        show_ascii()
        while True:
            main_menu()
    except KeyboardInterrupt:
        print("\n" + Fore.RED + "[" + Style.RESET_ALL + "+" + Fore.RED + "]" + Style.RESET_ALL + "ZQ-RIPPER was terminated by pressing CTRL+C.")
        exit()


if __name__=="__main__":
    main()


