from lxml import html
import requests
import string
from lxml.html import parse
from re import sub
import datetime

# Get current time to denote when sample taken
dt = datetime.datetime.now()

doc = parse('http://www.umggaming.com/tournaments/view/all').getroot()

tournament = doc.cssselect('div.tournament')
tourneyGame = doc.cssselect('div.content a.PG-1')
tourneyGameName = tourneyGame[0]

print tourneyGameName.text_content
print type(tourneyGame[0])

# Grab All tourneys listed and format files into usable format
for i in range(0, len(tournament)):
    # get needed html element sections
    dt = datetime.datetime.now()
    tourneyName = tournament[i].cssselect('div.tournament a')
    tourneyInfo = tournament[i].cssselect('div.info')
    tourneyPlatform = tournament[i].cssselect('div.platforms a')
    # pull data from elements
    str1 = 'Title: ' + tourneyName[0].text_content().replace('\t', '') + '\n'
    str1 = str1 + 'URL: ' + tourneyName[0].attrib['href'] + '\n'
    # str1 = str1 + 'Game: ' + tourneyGame[0].text_content + '\n'
    str1 = str1 + 'Platform: ' + tourneyPlatform[0].attrib['class']
    for el2 in tourneyInfo:
        str1 = str1 + el2.text_content().replace('\t', '')
    str1 = str1 + 'Date Recorded: ' + str(dt.now()) + '\n'
    str1 = str1 + '}\n'

    print '\n'.join([x for x in str1.split("\n") if x.strip() != ''])


# dict list to json {item[0]:item[1] for item in lst} == dict(lst)



