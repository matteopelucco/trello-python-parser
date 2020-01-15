#!/usr/bin/python

import logging, os, io, sys, getopt, time, datetime
import urllib.request, json, yaml, re

# settings
json_file = 'trello.json' # the json file to parse
commentVisibilityDays = 30
commentIsFreshDays = 7

# open json
with open(json_file) as data_file:
    data = json.load(data_file)

# globals
lists = data["lists"]
cards = data["cards"]
actions = data["actions"]

# some funcs
def nick(fullName):
    if fullName == "Matteo Pelucco":
        return "PELM"
    return fullName

def collectComments(card): 
    cardComments = []
    for action in actions: 
        if (action["type"] == "commentCard" and action["data"]["card"]["id"] == card["id"]): 
            
            comment = {}

            dateStr = action["date"] #2020-01-09T13:49:10.677Z
            dateObj = datetime.datetime.strptime(dateStr, '%Y-%m-%dT%H:%M:%S.%fZ')
            now = datetime.datetime.now()
            if ((now - dateObj).days > commentVisibilityDays):
                continue
            if ((now - dateObj).days > commentIsFreshDays):
                comment["isFresh"] = True
            else:
                comment["isFresh"] = False

            dateReverse = str(dateObj.year) + "." + str(dateObj.month) + "." + str(dateObj.day)
            comment["date"] = dateReverse

            text = action["data"]["text"]
            comment["text"] = text

            authorStr = action["memberCreator"]["fullName"] #Matteo Pelucco
            authorNickname = nick(authorStr)
            comment["author"] = authorNickname

            cardComments.append(comment)
    return cardComments


for list in lists: 
    print("\n### " + list["name"])
    for card in cards:
        if (card["idList"] == list["id"] and not card["closed"]): 
            print("- " + card["name"])

            comments = collectComments(card)
            for comment in comments:
                if comment["isFresh"]:
                    print ("  - [{author} - {date}] {text}".format(author=comment["author"], date=comment["date"], text=comment["text"]))
                else:
                    print ("  - <span style=\"color:blue\">_NEW_ [{author} - {date}] {text}</span>".format(author=comment["author"], date=comment["date"], text=comment["text"]))