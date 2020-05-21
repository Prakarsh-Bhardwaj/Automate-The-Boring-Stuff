# Python program which automatically open top 5 results from google related to the search query
# Usage - python autotabs.py <search query> -- to use with command line arguments.
# python autotabs.py -- to give input at runtime.

import webbrowser , requests , bs4
import sys , time

print("Konichiwa!!")
if(len(sys.argv) > 1):
    print("Search query taken!!")
    data = sys.argv[1:]
else:
    data = input("Enter search query: ").split()
#https://www.google.com/search?q=python+is+good&gbv=1&sei=PH_FXcDNE_DWz7sP1a-NaA -- google results without javascript.
query = "https://www.google.com/search?q=" + "+".join(data) + "&gbv=1&sei=PH_FXcDNE_DWz7sP1a-NaA"
print("loading...")
rdata = requests.get(query)
try:
    rdata.raise_for_status()
except:
    print("Query not found!!")

ssoup = bs4.BeautifulSoup(rdata.text , "lxml")
slist = ssoup.select(".kCrYT a")
for i in range(min(5,len(slist))):
    webbrowser.open("https://google.com" + slist[i].get("href"))
