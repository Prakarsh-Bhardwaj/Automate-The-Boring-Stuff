# Downloads the last 5 latest comics form xkcd!!
# Uses multithreading to reduce the runtime to 1/2 of the original runtime!

import requests , time , threading
import bs4 , re , os

def imagefinder():
    imgurl = []
    imglinks = []
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
    return imglinks

def downloader(imurl , i):
    obj = requests.get("https:" + imurl)
    for x in obj.iter_content(10**10):
        f = open("fs{}.png".format(i) , "wb")
        f.write(x)
        f.close()

starttime = time.time()
imglinks = imagefinder()
os.chdir("./xkcd/")
i , threads = 0 , []
for l in imglinks:
    threads.append(threading.Thread(target=downloader , args=(l,i)))
    threads[-1].start()
    i += 1
for thread in threads:
    thread.join()
endtime = time.time()
print("Download time: " + str(endtime - starttime))