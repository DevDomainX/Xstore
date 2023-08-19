#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from banner  import banner
from colorama import init, Fore, Style,  Back
init()
print(Style.BRIGHT+Fore.GREEN+"""
 Created by: 1LugarParaProgramar
 lenguaje:  python3
 Created: 18 De Gosto  2023\n""")


def download(name, commands):
	print('\n###### Intalling ... {}'.format(name))
	os.system('apt update && apt upgrade')
	os.system("pip install colorama")
	for i in commands:
		os.system(i)
	print('###### Intalling *_*')
	
while True:
    print(banner(),"\n")
    print("\n (( 1 )) > Nmap\n","(( 2 )) > Red Hawk\n","(( 3 )) > D-Tect\n","(( 4 )) > sqlmap\n",
			"(( 5 )) > Infoga\n","(( 6 )) > ReconDog\n","(( 7 )) > AndroZenmap\n","(( 8 )) > sqlmate\n", "(( 9 )) > AstraNmap\n",
			"(( 10 )) > WTF\n","(( 11 )) > Easymap\n","(( 12 )) > BlackBox\n","(( 13 )) > XD3v\n","(( 14 )) > Crips\n","(( 15 )) > SIR\n", "(( 16 )) > EvilURL\n","(( 17 )) > Striker\n","(( 18 )) > Xshell\n","(( 19 )) > OWScan\n","(( 20 )) > OSIF\n", "(( 21 )) > Intalling librerie\n",  "(( 0 )) > Exit Script \n")
    opcion = input("Xstore> ")
    if opcion == "01" or opcion == "1":
	       download("Nmap", ('apt install nmap'))
    elif opcion == "02" or opcion == "2":
		    download("RED HAWK", ('apt install git php','git clone https://github.com/Tuhinshubhra/RED_HAWK', 'mv RED_HAWK ~'))
    elif opcion == "03" or opcion == "3":
			    download("D-Tect",('apt install python2 git','git clone https://github.com/shawarkhanethicalhacker/D-TECT', 'mv D-TECT ~'))
    elif opcion == "04" or opcion == "4":
			    download("sqlmap",('apt install git python2','git clone https://github.com/sqlmapproject/sqlmap','mv sqlmap ~'))
    elif opcion == "05" or opcion == "5":
		    	download("Infoga",('apt install python2 git','pip2 install requests urllib3 urlparse','git clone https://github.com/m4ll0k/Infoga','mv Infoga ~'))
    elif opcion == "06" or opcion == "6":
		    	download("ReconDog",('apt install python2 git','git clone https://github.com/UltimateHackers/ReconDog','mv ReconDog ~'))
    elif opcion == "07" or opcion == "7":
			    download("AndroZenmap",('apt install nmap curl','curl -O http://override.waper.co/files/androzenmap.txt','mkdir ~/AndroZenmap','mv androzenmap.txt ~/AndroZenmap/androzenmap.sh'))
    elif opcion== "08" or opcion == "8":
		        download("sqlmate",('apt install python2 git','pip2 install mechanize bs4 HTMLparser argparse requests urlparse2','git clone https://github.com/UltimateHackers/sqlmate','mv sqlmate ~'))			
    elif opcion== "09" or opcion == "9":
		    	download("AstraNmap",('apt install git nmap','git clone https://github.com/Gameye98/AstraNmap','mv AstraNmap ~'))
    elif opcion == "10":
		    	download("WTF",('apt install git python2','pip2 bs4 requests HTMLParser urlparse mechanize argparse','git clone https://github.com/Xi4u7/wtf','mv wtf ~'))
    elif opcion == "11":
		    	download("Easymap",('apt install php git','git clone https://github.com/Cvar1984/Easymap','mv Easymap ~','cd ~/Easymap && sh install.sh'))
    elif opcion == "12":
		    	download("BlackBox",('apt install python2 git && pip2 install optparse passlib','git clone https://github.com/jothatron/blackbox','mv blackbox ~'))
    elif opcion == "13":
		    	download("XD3v",('apt install curl','curl -k -O https://gist.github.com/Gameye98/92035588bd0228df6fb7fa77a5f26bc2/raw/f8e73cd3d9f2a72bd536087bb6ba7bc8baef7d1d/xd3v.sh','mv xd3v.sh ~/../usr/bin/xd3v && chmod +x ~/../usr/bin/xd3v'))
    elif opcion == "14":
		    	download("Crips",("apt install git python2 openssl curl libcurl wget","git clone https://github.com/Manisso/Crips","mv Crips ~"))
    elif opcion == "15":
			    download("SIR",("apt install python2 git","pip2 install bs4 urllib2","git clone https://github.com/AeonDave/sir.git","mv sir ~"))
    elif opcion == "16":
		    	download("EvilURL",("apt install git python2 python3","git clone https://github.com/UndeadSec/EvilURL","mv EvilURL ~"))
    elif opcion == "17":
		    	download("Striker",('apt install git python2','git clone https://github.com/UltimateHackers/Striker','mv Striker ~','cd ~/Striker && pip2 install -r requirements.txt'))
    elif opcion == "18":
			    download("Xshell",("apt install lynx python2 figlet ruby php nano w3m","git clone https://github.com/Ubaii/Xshell","mv Xshell ~"))
    elif opcion == "19":
			    download("OWScan",('apt install git php','git clone https://github.com/Gameye98/OWScan','mv OWScan ~'))
    elif opcion == "20":
		    	download("OSIF",('apt install git python2','pip2 install requests','git clone https://github.com/ciku370/OSIF','mv OSIF ~'))
    elif opcion == "21":
        download("colorama",('pip  install colorama'))
    elif opcion == "00" or opcion== "0":
        print("Gracias por usar mi script")
        break