# Usage - python mcb.py save "keyword" - to save the contents of chipboard under that keyword.
#         python mcb.py list - to list all keywords and copies them.
#         python mcb.py "keyword" - to copy contents of the given keyword.
#         python mcb.py delete - deletes all the keywords.
#         python mcb.py delete "keyword" - deletes a particular keyword.

import sys
import pyperclip
import shelve

def check(a):
    if a[1] == "save":
        shelf[a[2]] = pyperclip.paste()
        print("Copied content saved as " + a[2])
    elif a[1] == "list":
        pyperclip.copy(" ".join(shelf.keys()))
        print("\n".join(shelf.keys()))
    elif a[1] in shelf.keys():
        pyperclip.copy(shelf[a[1]])
        print("Contnet of save " + a[1] + " copied")
    elif a[1] == "delete" and len(a) == 2:
        for x in shelf.keys():
            del shelf[x]
        print("All keywords deleted")
    elif a[1] == "delete" and len(a) > 2:
        del shelf[a[2]]
        print("Keyword deleted")
    else:
        print("Gomenasai , nothing copied by that keyword")

shelf = shelve.open("data")
check(sys.argv)
shelf.close()