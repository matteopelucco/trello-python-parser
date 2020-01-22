#!/usr/bin/python

import logging, os, io, sys, getopt, time, datetime
import urllib.request, json, yaml, re

# settings
json_file = 'trello.json' # the json file to parse
output_file = "output.md" # output markdown
commentVisibilityDays = 30
commentIsFreshDays = 7

# open json
with open(json_file) as data_file:
    data = json.load(data_file)

open(output_file, 'w').close()

# globals
lists = data["lists"]
cards = data["cards"]
actions = data["actions"]

# some funcs
def nick(fullName):
    if fullName == "Matteo Pelucco":
        return "PELM"
    return fullName

def write(*args, **kwargs):
    with open(output_file, 'a') as file:
        print(*args, **kwargs, file=file)

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
    
    return sorted(cardComments, key=lambda k: k['date'], reverse=True) 

write ("##### exported by Trello Parser on {date} #####".format(date=str(datetime.datetime.now())))
write ("##### source code and instructions available here: https://github.com/matteopelucco/trello-python-parser #####")
for list in lists: 
    if not list["closed"]:
        write("\n---")
        write("### " + list["name"])
        write("---")
        for card in cards:
            if (card["idList"] == list["id"] and not card["closed"]):

                # description
                cardDescription = "";
                
                if "desc" in card and card["desc"]: 
                    cardDescription = " - `" + card["desc"] + "`"
                    
                write("- " + card["name"] + cardDescription)

                comments = collectComments(card)
                for comment in comments:
                    if comment["isFresh"]:
                        write ("  - [{author} - {date}] {text}".format(author=comment["author"], date=comment["date"], text=comment["text"]))
                    else:
                        write ("  - <span style=\"color:blue; font-weight:bold;\"> [{author} - {date}] {text}</span>".format(author=comment["author"], date=comment["date"], text=comment["text"]))