#!/usr/bin/env python3

import urllib.request
import json
from  sys import argv

#Filters out incorrect command line arguments
if len(argv) != 2 and len(argv) != 3:
        print("Commands:\n  countries     Lists available countries\n  attributes    Lists attributes\nUsage:\n  ./covid19 <country> <attribute>\n  ./covid19 <command>")
        exit()

if len(argv) == 2 and argv[1] != "countries" and argv[1] != "attributes":
        print("Commands:\n  countries     Lists available countries\n  attributes    Lists attributes\nUsage:\n  ./covid19 <country> <attribute>\n  ./covid19 <command>")
        exit()

#Opens the covid19 API (https://covid19api.com/)
API_URL = "https://api.covid19api.com/summary"
with urllib.request.urlopen(API_URL) as response:
        JSON = response.read()
        data = json.loads(JSON)

        #Executes the commands
        if argv[1].lower == "countries":
                print("global")
                for i in data["Countries"]:
                        country = i["Slug"]
                        print(country)
        elif argv[1].lower == "attributes":
                for i in data["Global"]:
                        print(i)

        elif argv[1].lower() == "global":
                print(data["Global"][sys.argv[2]])
        else:
                country = argv[1]
                attribute = argv[2]

                #Iterates over the data until it finds the requested country's segment
                for i in data["Countries"]:
                        if i["Slug"].lower() == country.lower() and attribute in i:
                                print(attribute, ": ", i[attribute], sep="")
                                exit()

                print("Incorrect country or attribute")

