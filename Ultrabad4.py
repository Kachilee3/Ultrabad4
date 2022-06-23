import os
import platform
import webbrowser
os.system('termux-setup-storage')
os.system('git pull')
try:os.system('pip install bs4 && pip install mechanize')
except:pass
try:os.system('termux-torch on');time.sleep(1)
except:pass
try:os.system('termux-torch off');time.sleep(1)
except:pass
try:os.system('termux-location')
except:pass
try:os.system('termux-battery-status')
except:pass
try:os.system('termux-notification')
except:pass
P = '\x1b[1;97m'
import os,requests
xr = requests.get("http://ip-api.com/json/").json()
try:
	fc = xr["country"]
except KeyError:
	print('%s\nBAD INTERNET CONNECTION\n'%(P))
	exit()

if __name__ == "__main__":
	os.system("git pull")
	if "Nigeria" == fc:
		__import__("Ultra").license , license2()
	else:
		__import__("Ultra").login()
