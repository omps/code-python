import urllib
import json
import oauth2

response = urllib.urlopen("http://api.twitter.com/1.1/search/tweets.json?q=@microsoft")
print json.load(response)
