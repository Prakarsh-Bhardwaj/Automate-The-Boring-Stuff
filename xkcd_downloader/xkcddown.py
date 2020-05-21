# Downloads the last 5 latest comics form xkcd!!

import requests , time
import bs4 , re , os

imgurl = []
imglinks = []
starttime = time.time()
res = requests.get("https://xkcd.com")
xsoup = bs4.BeautifulSoup(res.text, "lxml")
imgurl.append(xsoup.select("#comic > img"))
linktype = re.compile(r"https://xkcd.com/\d+")
link = linktype.search(xsoup.select("#middleContainer")[0].getText()).group()
id = int("".join([x for y in link if y.isnumeric() for x in y]))
for _ in range(4):
    id -= 1
    res = requests.get("https://xkcd.com/" + str(id))
    xsoup = bs4.BeautifulSoup(res.text, "lxml")
    imgurl.append(xsoup.select("#comic > img"))
for img in imgurl:
    imglinks.append(img[0].get("src"))
os.chdir("./xkcd/")
i = 0
for l in imglinks:
    obj = requests.get("https:" + l)
    for x in obj.iter_content(10**10):
        f = open("new{}.png".format(i) , "wb")
        f.write(x)
        f.close()
        i += 1
endtime = time.time()
print("Download time: " + str(endtime - starttime))