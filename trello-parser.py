#!/usr/bin/python

import logging, os, io, sys, getopt, time
import urllib.request, json, yaml, re

# to fill
json_file = 'trello.json' # the json file to parse
file_extension = '.txt' # the file extension you'd like to use

# open json
with open(json_file) as data_file:
    data = json.load(data_file)

lists = data["lists"]
cards = data["cards"]
actions = data["actions"]

for list in lists: 
    print("[L]" + list["name"] + ", id: " + list["id"])
    for card in cards:
        if (card["idList"] == list["id"] and not card["closed"]): 
            print("  [C] " + card["name"] + ", id: " + card["id"])
            for action in actions: 
                if (action["type"] == "commentCard" and action["data"]["card"]["id"] == card["id"]): 
                    print ("    [A]: " + action["data"]["text"])