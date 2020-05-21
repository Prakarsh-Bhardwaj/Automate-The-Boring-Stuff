# Downloads the last 5 latest comics form xkcd!!
# Uses multithreading to reduce the runtime to 1/4 of the original runtime!
# Works!!! :) 

import requests , time , threading
import bs4 , re , os

def startidf():
    res = requests.get("https://xkcd.com")
    xsoup = bs4.BeautifulSoup(res.text, "lxml")
    linktype = re.compile(r"https://xkcd.com/\d+")
    link = linktype.search(xsoup.select("#middleContainer")[0].getText()).group()
    id = int("".join([x for y in link if y.isnumeric() for x in y]))
    return id

def imgf(url,imgurl):
    res = requests.get(url)
    xsoup = bs4.BeautifulSoup(res.text, "lxml")
    imgurl.append((xsoup.select("#comic > img")))

def imagefinder():
    imgurl = []
    imglinks = []
    id = startidf()
    threads = []
    for _ in range(4):
        threads.append(threading.Thread(target=imgf , args = ["https://xkcd.com/" + str(id) , imgurl]))
        threads[-1].start()
        id -= 1
    for x in threads:
        x.join()                               
    for img in imgurl:
        imglinks.append(img[0].get("src"))
    return imglinks                         

def downloader(imurl , i):
    obj = requests.get("https:" + imurl)
    for x in obj.iter_content(10**10):
        f = open("t{}.png".format(i) , "wb")
        f.write(x)
        f.close()

starttime = time.time()
imglinks = imagefinder()
os.chdir("./xkcd/")
threads = []
for l in imglinks:
    threads.append(threading.Thread(target=downloader , args=(l , len(threads))))
    threads[-1].start()
for thread in threads:
    thread.join()
endtime = time.time()
print("Download time: " + str(endtime - starttime))