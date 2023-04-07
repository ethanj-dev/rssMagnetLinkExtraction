import os
from pathlib import Path
from bs4 import BeautifulSoup
import requests as re
from shutil import move

rootUrl = "https://nyaa.si"
urlList = ["/?f=0&c=0_0&q=erai"]
maxPageLen = 9
originName = ""
saveDir = os.path.join(os.getcwd(), "torrent_files")

Path(saveDir).mkdir(parents=True, exist_ok=True)

for urls in urlList:
    for pages in range(maxPageLen):
        url = rootUrl + urls + "&p={}".format(pages+1)
        response = re.get(url)

        soup = BeautifulSoup(response.content, "html.parser")

        for link in soup.find_all("a"):
            href = link.get("href")

            if href and "/view/" in href:
                if link.get("title") is not None:
                    originName = link.get("title")

            if href and "/download/" in href:
                filename = os.path.join(saveDir, href.split("/")[-1])
                response = re.get(rootUrl + href)

                print("Downloading filename : {} - {}".format(originName, filename))
                with open(filename, "wb") as f:
                    f.write(response.content)

                renameFile = originName + ".torrent"
                move(filename, os.path.join(saveDir, renameFile))
