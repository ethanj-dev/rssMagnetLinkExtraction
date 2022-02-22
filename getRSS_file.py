import os
import feedparser
from pathlib import Path

def main():
    rss_folder = "./rss/"
    Path(rss_folder).mkdir(parents=True, exist_ok=True)

    option = ["standalone", "aio"]
    currentOption = option[1]

    if currentOption == option[0]:
        feed_url = "YOUR/RSS/FILE/PATH"
        magnet_link = extractLinks(feed_url)
        save(magnet_link, filename)
    else:
        magnetLinks =[]
        for filename in os.listdir(rss_folder):
            magnetLinks +=extractLinks(rss_folder + filename)
        save(magnetLinks, "AIO.rss")

def extractLinks(feed_url):
    rss = feedparser.parse(feed_url)

    link = []
    magnet_link = []

    magnet_start = "magnet:?xt=urn:btih:"
    magnet_announce=""
    # You will need to have annoucement link to the magnet_announce variable.


    for idx in range(len(rss.entries)):
        link.insert(idx, rss.entries[idx].link)

        magnet_id = rss.entries[idx].nyaa_infohash
        magnet = magnet_start + magnet_id + magnet_announce
        magnet_link.insert(idx, magnet)

    return magnet_link

def save(magnet_link, filename):
    origin_name = filename.split(".")[0] + str(".txt")
    with open(origin_name, 'w') as f:
        for length in range(len(magnet_link)):
            f.write(str(magnet_link[length]) + "\n")

if __name__ == "__main__":
    main()
