#!/bin/env/ python3
import sys
import requests
import csv
import colorama
from colorama import Fore,Style

# Check status code
apiGet = requests.get("https://randomuser.me/api/")
if apiGet.status_code == 200:
 print(Fore.GREEN + "Status code: " + str(apiGet.status_code) + "\n" + Style.RESET_ALL)
if apiGet.status_code == 301:
 print(Fore.YELLOW + "Status code: " + str(apiGet.status_code) + "\n" + Style.RESET_ALL)
if apiGet.status_code == 404:
 print(Fore.RED + "Status code: " + str(apiGet.status_code) + "\n" + Style.RESET_ALL)
 sys.exit()
api = apiGet.json()

# Filter data with loops
print(Fore.CYAN + "Filter with loops!" + Style.RESET_ALL+"\n")
r = "results"
for a in api[r][0]:
 for b in api[r][0][a]:
  if b == "first":
   f = api[r][0][a][b]
  if b == "last":
   l = api[r][0][a][b]
  if a == "location" and b == "street":
   s = api[r][0][a][b]["name"]
  if a == "location" and b == "street":
   n = api[r][0][a][b]["number"]
  if b == "username":
   u = api[r][0][a][b]
  if a == "email":
   e = api[r][0][a]
  if b == "password":
   p = api[r][0][a][b]
print("Personal info\n" + "Firstname: " + f + "\nLastname: " + l + "\nStreetname: " + s + "\nStreetNr: " + str(n) + "\n\nCredentials\nUsername: " + u + "\nEmail: " + e + "\nPassword: " + p)

# Filter data with ID
print(Fore.CYAN + "\n\nFilter with ID!" + Style.RESET_ALL)
username = api["results"][0]["login"]["username"]
password = api["results"][0]["login"]["password"]
print("\nUsername: " + username + "\nPassword: " + password)
