#***********************************************************************
# This program gives the details by scraping top 100 countries by area
# worldwide and writing them to outputfile.csv file
import sys
import requests
import time
import random
write_file = open("outputfile.csv","w")           #open the outputfile.csv file
top_countries_by_area= []                         #list for storing country names

url = "http://www.geoba.se/population.php?aw=world"
    
html = requests.get(url).text.split('\n')
    
for line in html:
    found = line.find('href="country.php?cc=')
        
    if found > 0:
        line = line[found:]
        
        pos = line.find('">')

        top_countries_by_area.append(line[pos+2:-9])
    
time.sleep(random.randint(0,3))
for l in top_countries_by_area:
    write_file.write(l + '\n')                   #printing country names
