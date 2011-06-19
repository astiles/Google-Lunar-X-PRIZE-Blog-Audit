import feedparser

d = feedparser.parse("http://www.googlelunarxprize.org/lunar/teams/rss")

feed = d['feed']['title']
print feed

# If the entry has a June date, then print the team name and title
# Later add counters for number of entries for each team

date = d['feed']
for item in d['entries']:
    time = item.modified_parsed
    print time.tm_mon
    if time.tm_mon == 6
        print o hai




    





