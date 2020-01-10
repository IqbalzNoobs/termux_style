# -*- coding: UTF-8 -*-
# Author: Iqbal Dev
# Team: Life Of Programmer

import os
import sys
import time


# warna
d = "\033[90;1m"
m = "\033[91;1m"
h = "\033[92;1m"
k = "\033[93;1m"
b = "\033[94;1m"
p = "\033[95;1m"
a = "\033[96;1m"
s = "\033[97;1m"


def runntxt(noob):
    for lol in noob + '\n':
        sys.stdout.write(lol)
        sys.stdout.flush()
        time.sleep(10. / 600)
def banner():
    os.system("clear")
    os.system("toilet -f standard 'Trmx Style' -F gay")
#    print m+"+--------------------------------------+"
    os.system("echo '|  Author: Iqbal Dev   ' | lolcat")
    os.system("echo '|  Team: Life Of Programmer' | lolcat")
    os.system("echo '|  Instagram: Iqbaldev' | lolcat")
    os.system("echo '|  Facebook: Iqbal Dev  ' | lolcat")
    print m+"+------------------------------------------------+ "
    print h+"   [\033[97m1\033[92m] \033[96mEyes Gay",h+"      [\033[97m6\033[92m] \033[96mName Lolcat"
    print h+"   [\033[97m2\033[92m] \033[96mEyes Lolcat",h+"   [\033[97m7\033[92m] \033[96mName Gay"
    print h+"   [\033[97m3\033[92m] \033[96mTrain Lolcat",h+"  [\033[97m8\033[92m] \033[96mNeofetch Lolcat"
    print h+"   [\033[97m4\033[92m] \033[96mTrain Gay",h+"     [\033[97m9\033[92m] \033[96mNeofetch Gay"
    print " "
    print m+"   [\033[93m5\033[91m] \033[97mInstall Paketnya Dulu Bro..!"
    print m+"+------------------------------------------------+ "
def pilih():
  try:
 
    print k+"╭────\033[92m[ \033[96mPilih Opsinya.! \033[92m]"
    pil = raw_input("\033[93m╰────➲\033[97m ")
    if pil in ['1'] or pil == 'gay':
        eyes_gay()
    elif pil in ['2'] or pil == 'lolcat':
        eyes_lolcat()
    elif pil in ['3'] or pil == 'train lolcat':
        train_lolcat()
    elif pil in ['4'] or pil == 'train gay':
        train_gay()
    elif pil in ['5'] or pil == 'install':
        install()
    elif pil in ['6'] or pil == 'name lolcat':
        name_lolcat()
    elif pil in ['7'] or pil == 'name gay':
        name_gay()
    elif pil in ['8'] or pil == 'neofetch lol':
        neofetch_lol()
    elif pil in ['9'] or pil == 'neofetch gay':
        neofetch_gay()
    else:
        print m+'pilih yg bener cuk...'
        glob()
  
  except KeyboardInterrupt:
    print d+"Keluar dari program..."
    sys.exit()  
''' 
  except NameError:
    print "pilih cuy.."
    glob()
  except SyntaxError:
    print " Masukkan pilihannya cuk.."
    glob()

'''
def main():
    banner()
    pilih()
def glob():
    pilih()

def install():
    os.system("pkg install ruby cowsay toilet figlet sl")
    os.system("pkg install neofetch")
    os.system("gem install lolcat")
    main()
def eyes_lolcat():
    os.system("clear")
    os.system("cowsay -f eyes 'EyesLolcat' | lolcat")
    os.system("toilet -f standard 'Eyes Lolcat' | lolcat")
    print a+"+---------------------------+",k+" "
    name = str(raw_input(' [?]\033[97m Nama Pengguna:\033[92m '))
    print a+"+---------------------------+",h+" "
    prompt = str(raw_input(' [?]\033[95m Nama Prompt:\033[93m '))
    print a+"+------------------------+"
    print d+" Loading......"
    time.sleep(1.5)
    iqbalz = open("bash.bashrc", "w")
    iqbalz.write("PS1='")
    iqbalz.write("\n\e[0;32m╭────\e[0;31m[\e[0m root\e[0;32m⚔\e[0m"+prompt+"#\e[0;33m \w \e[0;31m]\e[0;32m")
    iqbalz.write("\n╰────➲ '")
    iqbalz.write("\nclear")
    iqbalz.write("\ncowsay -f eyes '"+name)
    iqbalz.write("' | lolcat")
    iqbalz.write("\ntoilet -f standard '"+name)
    iqbalz.write("' | lolcat")
    iqbalz.write("\necho ' User: "+name)
    iqbalz.write("' | lolcat")
    iqbalz.write("\ndate | lolcat")
    iqbalz.close()
    os.system("rm $HOME/../usr/etc/bash.bashrc")
    os.system("cp -f bash.bashrc $HOME/../usr/etc")
    os.system("clear")
    os.system("cowsay -f eyes ' Eyes Lolcat' | lolcat")
    os.system("toilet -f standard 'Eyes Lolcat' | lolcat")
    os.system("echo '           Powered By: Orang Ganteng' | lolcat ")
    print ' '
    runntxt(a+"                √  S U C C E S ✓")
    runntxt(h+"          ✓  Silahkan Buka Sesi Baru ✓")
    print " "
   
def eyes_gay():
    os.system('clear')
    os.system("cowsay -f eyes 'EyesGay' | lolcat")
    os.system("toilet -f standard ' Eyes Gay' -F gay")
    print a+"+---------------------------+",k+" "
    name = str(raw_input(' [?]\033[97m Nama Pengguna:\033[92m '))
    print a+"+---------------------------+",h+" "
    prompt = str(raw_input(' [?]\033[95m Nama Prompt:\033[93m '))
    print a+"+------------------------+"
    print d+" Loading......"
    time.sleep(1.5)
    iqbalz = open("bash.bashrc", "w")
    iqbalz.write("PS1='")
    iqbalz.write("\n\e[0;32m╭────\e[0;31m[\e[0m root\e[0;32m⚔\e[0m"+prompt+"#\e[0;33m \w \e[0;31m]\e[0;32m")
    iqbalz.write("\n╰────➲ '")
    iqbalz.write("\nclear")
    iqbalz.write("\ncowsay -f eyes '"+name)
    iqbalz.write("' | lolcat")
    iqbalz.write("\ntoilet -f standard '"+name)
    iqbalz.write("' -F gay")
    iqbalz.write("\ndate | lolcat")
    iqbalz.close()
    os.system("rm $HOME/../usr/etc/bash.bashrc")
    os.system("cp -f bash.bashrc $HOME/../usr/etc")
    os.system('clear')
    os.system('clear')
    os.system("cowsay -f eyes 'Cowsay' | lolcat")
    os.system("toilet -f standard '   Eyes Gay' -F gay")
    os.system("echo '           Powered By: Orang Ganteng' | lolcat")
    print ' '
    runntxt(a+"                √  S U C C E S ✓")
    runntxt(h+"          ✓  Silahkan Buka Sesi Baru ✓")
    print " "

def train_lolcat():
    os.system('clear')
    os.system("sl")
    os.system("toilet -f standard 'TrainLolcat' | lolcat")
    print a+"+---------------------------+",k+" "
    name = str(raw_input(' [?]\033[97m Nama Pengguna:\033[92m '))
    print a+"+---------------------------+",h+" "
    prompt = str(raw_input(' [?]\033[95m Nama Prompt:\033[93m '))
    print a+"+------------------------+"
    print d+" Loading......"
    time.sleep(1.5)
    iqbalz = open("bash.bashrc", "w")
    iqbalz.write("PS1='")
    iqbalz.write("\n\e[0;32m╭────\e[0;31m[\e[0m root\e[0;32m⚔\e[0m"+prompt+"#\e[0;33m \w \e[0;31m]\e[0;32m")
    iqbalz.write("\n╰────➲ '")
    iqbalz.write("\nclear")
    iqbalz.write("\nsl")
    iqbalz.write("\nclear")
    iqbalz.write("\ntoilet -f standard '"+name)
    iqbalz.write("' | lolcat")
    iqbalz.write("\necho ' User: "+name)
    iqbalz.write("' | lolcat")
    iqbalz.write("\ndate | lolcat")
    iqbalz.close()
    os.system("rm $HOME/../usr/etc/bash.bashrc")
    os.system("cp -f bash.bashrc $HOME/../usr/etc")
    os.system("clear")
    os.system("sl")
    os.system("toilet -f standard 'TrainLolcat' | lolcat")
    os.system("echo '           Powered By: Orang Ganteng' | lolcat ")
    print ' '
    runntxt(a+"                √  S U C C E S ✓")
    runntxt(h+"          ✓  Silahkan Buka Sesi Baru ✓")
    print " "

def train_gay():
    os.system('clear')
    os.system("sl")
    os.system("toilet -f standard '  Train Gay' -F gay")
    print a+"+---------------------------+",k+" "
    name = str(raw_input(' [?]\033[97m Nama Pengguna:\033[92m '))
    print a+"+---------------------------+",h+" "
    prompt = str(raw_input(' [?]\033[95m Nama Prompt:\033[93m '))
    print a+"+------------------------+"
    print d+" Loading......"
    time.sleep(1.5)
    iqbalz = open("bash.bashrc", "w")
    iqbalz.write("PS1='")
    iqbalz.write("\n\e[0;32m╭────\e[0;31m[\e[0m root\e[0;32m⚔\e[0m"+prompt+"#\e[0;33m \w \e[0;31m]\e[0;32m")
    iqbalz.write("\n╰────➲ '")
    iqbalz.write("\nclear")
    iqbalz.write("\nsl")
    iqbalz.write("\nclear")
    iqbalz.write("\ntoilet -f standard '"+name)
    iqbalz.write("' -F gay")
    iqbalz.write("\necho ' User: "+name)
    iqbalz.write("' | lolcat")
    iqbalz.write("\ndate | lolcat")
    iqbalz.close()
    os.system("rm $HOME/../usr/etc/bash.bashrc")
    os.system("cp -f bash.bashrc $HOME/../usr/etc")
    os.system("clear")
    os.system("sl")
    os.system("toilet -f standard '  Train Gay' -F gay")
    os.system("echo '           Powered By: Orang Ganteng' | lolcat ")
    print ' '
    runntxt(a+"                √  S U C C E S ✓")
    runntxt(h+"          ✓  Silahkan Buka Sesi Baru ✓")
    print " "

def name_lolcat():
    os.system('clear')   
    os.system("toilet -f standard 'NameLolcat' | lolcat")
    print a+"+---------------------------+",k+" "
    name = str(raw_input(' [?]\033[97m Nama Pengguna:\033[92m '))
    print a+"+---------------------------+",h+" "
    prompt = str(raw_input(' [?]\033[95m Nama Prompt:\033[93m '))
    print a+"+------------------------+"
    print d+" Loading......"
    time.sleep(1.5)
    iqbalz = open("bash.bashrc", "w")
    iqbalz.write("PS1='")
    iqbalz.write("\n\e[0;32m╭────\e[0;31m[\e[0m root\e[0;32m⚔\e[0m"+prompt+"#\e[0;33m \w \e[0;31m]\e[0;32m")
    iqbalz.write("\n╰────➲ '")
    iqbalz.write("\nclear")
    iqbalz.write("\ntoilet -f standard '"+name)
    iqbalz.write("' | lolcat")
    iqbalz.write("\necho ' User: "+name)
    iqbalz.write("' | lolcat")
    iqbalz.write("\ndate | lolcat")
    iqbalz.close()
    os.system("rm $HOME/../usr/etc/bash.bashrc")
    os.system("cp -f bash.bashrc $HOME/../usr/etc")
    os.system("clear")
    os.system("toilet -f standard 'NameLolcat' | lolcat")
    os.system("echo '           Powered By: Orang Ganteng' | lolcat ")
    print ' '
    runntxt(a+"                √  S U C C E S ✓")
    runntxt(h+"          ✓  Silahkan Buka Sesi Baru ✓")
    print " "

def name_gay():
    os.system('clear')
    os.system("toilet -f standard '  Name Gay' -F gay")
    print a+"+---------------------------+",k+" "
    name = str(raw_input(' [?]\033[97m Nama Pengguna:\033[92m '))
    print a+"+---------------------------+",h+" "
    prompt = str(raw_input(' [?]\033[95m Nama Prompt:\033[93m '))
    print a+"+------------------------+"
    print d+" Loading......"
    time.sleep(1.5)
    iqbalz = open("bash.bashrc", "w")
    iqbalz.write("PS1='")
    iqbalz.write("\n\e[0;32m╭────\e[0;31m[\e[0m root\e[0;32m⚔\e[0m"+prompt+"#\e[0;33m \w \e[0;31m]\e[0;32m")
    iqbalz.write("\n╰────➲ '")
    iqbalz.write("\nclear")
    iqbalz.write("\ntoilet -f standard '"+name)
    iqbalz.write("' -F gay")
    iqbalz.write("\necho ' User: "+name)
    iqbalz.write("' | lolcat")
    iqbalz.write("\ndate | lolcat")
    iqbalz.close()
    os.system("rm $HOME/../usr/etc/bash.bashrc")
    os.system("cp -f bash.bashrc $HOME/../usr/etc")
    os.system("clear")
    os.system("toilet -f standard '  Name Gay' -F gay")
    os.system("echo '           Powered By: Orang Ganteng' | lolcat ")
    print ' '
    runntxt(a+"                √  S U C C E S ✓")
    runntxt(h+"          ✓  Silahkan Buka Sesi Baru ✓")
    print " "

def neofetch_lol():
    os.system('clear')
    os.system("toilet -f standard '      Neof Lol' | lolcat")
    os.system("neofetch")
    print a+"+---------------------------+",k+" "
    name = str(raw_input(' [?]\033[97m Nama Pengguna:\033[92m '))
    print a+"+---------------------------+",h+" "
    prompt = str(raw_input(' [?]\033[95m Nama Prompt:\033[93m '))
    print a+"+------------------------+"
    print d+" Loading......"
    time.sleep(1.5)
    iqbalz = open("bash.bashrc", "w")
    iqbalz.write("PS1='")
    iqbalz.write("\n\e[0;32m╭────\e[0;31m[\e[0m root\e[0;32m⚔\e[0m"+prompt+"#\e[0;33m \w \e[0;31m]\e[0;32m")
    iqbalz.write("\n╰────➲ '")
    iqbalz.write("\nclear")
    iqbalz.write("\ntoilet -f standard '"+name)
    iqbalz.write("' | lolcat")
    iqbalz.write("\nneofetch")
    iqbalz.write("\ndate | lolcat")
    iqbalz.close()
    os.system("rm $HOME/../usr/etc/bash.bashrc")
    os.system("cp -f bash.bashrc $HOME/../usr/etc")
    os.system("clear")
    os.system("neofetch")
    os.system("toilet -f standard '      Neof Lol' | lolcat")
    os.system("echo '           Powered By: Orang Ganteng' | lolcat ")
    print ' '
    runntxt(a+"                √  S U C C E S ✓")
    runntxt(h+"          ✓  Silahkan Buka Sesi Baru ✓")
    print " "


def neofetch_gay():   
    os.system('clear')
    os.system("toilet -f standard '     Neof Gay' -F gay")                 
    os.system("neofetch")
    print a+"+---------------------------+",k+" "
    name = str(raw_input(' [?]\033[97m Nama Pengguna:\033[92m '))
    print a+"+---------------------------+",h+" "
    prompt = str(raw_input(' [?]\033[95m Nama Prompt:\033[93m '))
    print a+"+------------------------+"
    print d+" Loading......"
    time.sleep(1.5)      
    iqbalz = open("bash.bashrc", "w")
    iqbalz.write("PS1='")
    iqbalz.write("\n\e[0;32m╭────\e[0;31m[\e[0m root\e[0;32m⚔\e[0m"+prompt+"#\e[0;33m \w \e[0;31m]\e[0;32m")
    iqbalz.write("\n╰────➲ '")
    iqbalz.write("\nclear")
    iqbalz.write("\ntoilet -f standard '"+name)
    iqbalz.write("' -F gay")
    iqbalz.write("\nneofetch")
    iqbalz.write("\ndate | lolcat")
    iqbalz.close()
    os.system("rm $HOME/../usr/etc/bash.bashrc")
    os.system("cp -f bash.bashrc $HOME/../usr/etc")
    os.system("clear")
    os.system("neofetch")
    os.system("toilet -f standard '     Neof Gay' -F gay")
    os.system("echo '           Powered By: Orang Ganteng' | lolcat ")
    print ' '
    runntxt(a+"                √  S U C C E S ✓")
    runntxt(h+"          ✓  Silahkan Buka Sesi Baru ✓")
    print " "

if __name__=='__main__':
    main()
