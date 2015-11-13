# -*- coding: utf-8 -*-

import time
import re

tags = {
    "script",
    "iframe",
    "object"
}
evilElements = []
for tag in tags:
    evilElements.append(re.compile(r"<" + tag + r"[^>]*>", re.MULTILINE))
    evilElements.append(re.compile(r"</" + tag + r">", re.MULTILINE))
evilElements.append(re.compile(r"on[^=]*=[\"][^\"]*[\"]", re.MULTILINE))
evilElements.append(re.compile(r"on[^=]*=['][^']*[']", re.MULTILINE))

def getCurrentDate():
    d = time.strftime("%x")
    da = d.split("/")
    date = da[1]+"/"+da[0]+"/"+da[2]
    return date


def avoidHTML(text):
    text = text.replace("<", "&lt;").replace(">", "&gt;")
    return text


def getUtf(text):
    render = unicode(text).encode("utf-8")
    return render


def avoidJavascript(text):
    noMoreEvilTag = False
    while(noMoreEvilTag == False):
        for element in evilElements:
            text = re.sub(element, "", text)
            print(text)
        noMoreEvilTag = True
        for element in evilElements:
            if(re.search(element, text) is not None):
                noMoreEvilTag = False
                break
    return text