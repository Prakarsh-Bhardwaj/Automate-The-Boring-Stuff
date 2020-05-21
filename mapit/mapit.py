#Takes input address in format ___,____,_____ from command line or keyboard
#and maps it on google maps.

import webbrowser
import sys
import pyperclip

if len(sys.argv) > 1:
    addlist = sys.argv[1].split(",")
else:
    addlist  = pyperclip.paste().split(",")

print(addlist)
address = "https://www.google.com/maps/place/" + ",+".join(addlist) + "/"
print(address)
webbrowser.open(address)