import datetime
from colorama import init, Fore, Back, Style
import os, webbrowser
import os

#intro
date = datetime.datetime.now()
print("Date =", date)
print(Fore.GREEN+ " ")
print("Terminal is start")
print("   _________       __                       ")
print("  /   _____/____ _/  |_ __ _________  ____  ")
print("  \_____  \\__  \\   __\  |  \_  __ \/    \   ")
print("  /        \/ __ \|  | |  |  /|  | \/   |  \ ")
print(" /_______  (____  /__| |____/ |__|  |___|  / ")
print("         \/     \/                       \/  ")


print("    _________.__           .__  .__   ")
print("  /   _____/|  |__   ____ |  | |  |   ")
print("  \_____  \ |  |  \_/ __ \|  | |  |  ")
print("  /        \|   Y  \  ___/|  |_|  |__ ")
print(" /_______  /|___|  /\___  >____/____/ ")
print("         \/      \/     \/           ")




print(Fore.BLUE + "┌──(Saturn🌌shell)")
while True:
    shell = input("└─$ ")
    
    #help
    if shell == 'cco' :
     print(" ")
   #google

    if shell == "google":
     print(Fore.GREEN + "google>>>")
     webbrowser.open_new("https://google.com")
     print(Fore.BLUE + "┌──(Saturn🌌shell)")

     #google -s

    if shell == "google -s":
      sg = input()
      webbrowser.open_new("https://www.google.com/search?q=" + sg)
      print(Fore.GREEN + "google " + Fore.RED + sg + " >>>")
      print(Fore.BLUE + "┌──(Saturn🌌shell)")



     #marine
    if shell == "marine":
        print(Fore.GREEN + "marine-traffic>>>")
        webbrowser.open_new("https://marinetraffic.com")
        print(Fore.BLUE + "┌──(Saturn🌌shell)")

    #plane
    if shell == "plane":
      print(Fore.GREEN + "flightradar24 >>>")
      webbrowser.open_new("https://www.flightradar24.com/")
      print(Fore.BLUE + "┌──(Saturn🌌shell)")
     
    #youtube
    if shell == "youtube":
      print(Fore.GREEN + "youtube >>>")
      webbrowser.open_new("https://www.youtube.com/")
      print(Fore.BLUE + "┌──(Saturn🌌shell)")

    #youtube -s
    if shell == "youtube -s":
     sy = input()
     webbrowser.open_new("https://www.youtube.com/results?search_query=" + sy)
     print(Fore.GREEN + "youtube " + Fore.RED + sy + " >>>")
     print(Fore.BLUE + "┌──(Saturn🌌shell)")

    #dbrescearch
    if shell == "db":
      print(Fore.GREEN + "DBresearch script start >>>")
      print(Fore.RED + "  ")
      os.system('sh dbstart.sh')
      print(Fore.BLUE + "┌──(Saturn🌌shell)")

    #st
    if shell == "st":
      print(Fore.GREEN + "Storm-Breaker script start >>>")
      print(Fore.RED + "  ")
      os.system('sh st.sh')
      print(Fore.BLUE + "┌──(Saturn🌌shell)")

    #pysher
    if shell == "pyphisher":
      print(Fore.GREEN + "pyphisher script start >>>")
      print(Fore.RED + "  ")
      os.system('sh pyphisher.sh')
      print(Fore.BLUE + "┌──(Saturn🌌shell)")

    #pyshing
    if shell == "phishing":
      print(Fore.GREEN + "pyphisher script start >>>")
      print(Fore.RED + "  ")
      os.system('sh pyphisher.sh')
      print(Fore.BLUE + "┌──(Saturn🌌shell)")
    
    #clear
    if shell == "clear":
      os.system('clear')
      print(Fore.BLUE + "┌──(Saturn🌌shell)")

    #msf
    if shell == "msf":
      print(Fore.GREEN + "metasploit start >>>")
      print(Fore.RED + "  ")
      os.system('sh msfconectwin.sh')
      print(Fore.BLUE + "┌──(Saturn🌌shell)")

    if shell == "msf -h":
      print(Fore.GREEN + "metasploit help start >>>")
      print(Fore.RED + "  ")
      os.system('nano /home/kali/system/shell/comandwin.txt')
      print(Fore.BLUE + "┌──(Saturn🌌shell)")


    
    

   

    
