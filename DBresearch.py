import time
from turtle import clear
import webbrowser
print('Enter your name:)')
x = input()
time.sleep(1.0)
print("name select is:")
time.sleep(1.0)
print(x)
time.sleep(1.0)
print("start database research")
time.sleep(2.0)
youtube = 'https://www.youtube.com/results?search_query=' + x 
google = 'https://www.google.com/search?q=' + x 
ddg = 'https://duckduckgo.com/?q=' + x 
instagram = 'https://www.instagram.com/explore/search/keyword/?q=' + x 
twitter = 'https://twitter.com/search?q=' + x 
linkedin = 'https://www.linkedin.com/search/results/all/?keywords=' + x + "&origin=GLOBAL_SEARCH_HEADER&sid=Uhh"
crt = 'https://crt.sh/?q=' + x 
opencorporates = 'https://opencorporates.com/companies?jurisdiction_code=&' + x + "=c&utf8=✓"
occrp = 'https://data.occrp.org/search?q=' + x 
whatsmyname= 'https://whatsmyname.app/'
print("   _____       __")
print("  / ___/____ _/ /___  ___________")
print("  \__ \/ __ `/ __/ / / / ___/ __ \ ")
print(" ___/ / /_/ / /_/ /_/ / /  / / / /")
print("/____/\__,_/\__/\__,_/_/  /_/ /_/")
print("youtube ->")
webbrowser.open(youtube)
time.sleep(0.7)
print("google ->")
webbrowser.open(google)
time.sleep(0.7)
print("Duck Duck Go ->")
webbrowser.open(ddg)
time.sleep(1.0)
print("---------------------------")
print("--social--")
print("---------------------------")
time.sleep(1.0)
print("Instagram ->")
webbrowser.open(instagram)
time.sleep(0.7)
print("Twitter ->")
webbrowser.open(twitter)
time.sleep(0.7)
print("linkedin ->")
webbrowser.open(linkedin)
time.sleep(1.0)
print("---------------------------")
print("*---DeepWeb---*")
print("---------------------------")
time.sleep(1.0)
print("crt.sh ->")
webbrowser.open(crt)
time.sleep(0.7)
print("opencorporates ->")
webbrowser.open(opencorporates)
time.sleep(0.7)
print("occrp ->")
webbrowser.open(occrp)
time.sleep(0.7)
print("whatsmyname ->")
webbrowser.open(whatsmyname)
time.sleep(0.7)
print("---------------------------")
exit