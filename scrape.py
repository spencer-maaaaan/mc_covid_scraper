"""
scrapes the marietta college covid dashboard daily to record the amount of covid cases on campus
"""
from bs4 import BeautifulSoup
import requests
import datetime
import csv

URL = "https://www.marietta.edu/covid-19-cases-reporting"

# getting the request and souping
r = requests.get(URL)
soup = BeautifulSoup(r.text, "lxml")

# grabbing the current semester, in the first div of "container-inline-block column-2" class
this_semester = soup.find("div", attrs={"class": "container-inline-block column-2"})

# getting the numbers
active, quarantined = [int(h2.text) for h2 in this_semester.find_all("h2")]

# generating timestamp
timestamp = datetime.datetime.now()
timestamp = timestamp.strftime("%Y-%m-%d %I:%M:%S")

# writing out to csv
with open("log.csv", "a") as of:
    writer = csv.writer(of)
    writer.writerow([timestamp, active, quarantined])