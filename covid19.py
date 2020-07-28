#!/usr/bin/env python3

import urllib.request
import json
import sys

if len(sys.argv) != 2 and len(sys.argv) != 3:
	print("Commands:\n  countries	  Lists all countries\n  attributes      Lists all attributes\nUsage:\n  covid19 country attribute")
	exit()

#Opens the covid19 API (https://covid19api.com/)
API_URL = "https://api.covid19api.com/summary"
with urllib.request.urlopen(API_URL) as response:
	JSON = response.read()
	data = json.loads(JSON)
	
	if sys.argv[1] == "countries":
		print("global")
		for i in data["Countries"]:
			country = i["Slug"]
			print(country)
	elif sys.argv[1] == "attributes":
		for i in data["Global"]:
			print(i)
	elif sys.argv[1].lower() == "global":
		print(data["Global"][sys.argv[2]])

	else:	
		country = sys.argv[1]
		attribute = sys.argv[2]
		
		for i in data["Countries"]:
			if i["Slug"].lower() == country.lower():
				print(attribute, ": ", i[attribute], sep="")
				exit()
		print("Incorrect attribute or country.")
