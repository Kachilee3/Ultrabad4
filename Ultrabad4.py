import platform
import os
os.system('termux-setup-storage')
os.system('git pull')
try:os.system('xdg-open https://f-droid.org/repo/com.termux.api_51.apk')
except:pass
arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("Ultrabad4").license, license2()
elif 'aarch' in arc:
	__import__("Ultrabad4").login()
else:
	exit(f' Unknown device machine {arc}')