import urllib2
import json
import sys

show_spoiler = sys.argv[1] if len(sys.argv) > 1 else '.'

response = urllib2.urlopen("https://api.opendota.com/api/proMatches")
data = json.load(response)
radiant_name = data[0]["radiant_name"]
dire_name = data[0]["dire_name"]
league_name = data[0]["league_name"]
radiant_win = data[0]["radiant_win"]

print "______  _____  _____   ___       _____"
print "|  _  \|  _  ||_   _| / _ \     / __  \ "
print "| | | || | | |  | |  / /_\ \    `' / /'"
print "| | | || | | |  | |  |  _  |      / /"
print "| |/ / \ \_/ /  | |  | | | |    ./ /___"
print "|___/   \___/   \_/  \_| |_/    \_____/"
print ""

print "league: " + league_name
print "-------------------------------"
print "radiant team: " + radiant_name
print "-------------------------------"
print "dire team: " + dire_name
print "-------------------------------"

if show_spoiler == "--spoiler":
    if radiant_win == True:
        print "winner: " + radiant_name
    else:
        print "winner: " + dire_name
else:
    print "add --spoiler to show winRar"

