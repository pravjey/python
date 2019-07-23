import tweepy
from twython import Twython
import tweetpony
from TwitterAPI import TwitterAPI

import time
import matplotlib.pyplot as plt
import pandas as pd

twitterlib = ["Tweepy", "Twython", "TweetPony", "TwitterAPI"]
twittersec = []
followerslen = []
friendslen = []
u = "@realDonaldTrump"
n = 200



# Calculate time for Tweepy

start = time.time()

tweepy_consumer_key = "cr9wJjmmT2CcGXqjsx7aWvsbA"
tweepy_consumer_secret = "QAjnpYxS59MEil5IEpJJzGP0WqDajklMcXxcxiaJLh9doBuQ6g"
tweepy_access_token = "897909419996041218-z27A8n2L6UcmUPuRbZhQBcpAAEk1Jxj"
tweepy_access_token_secret = "iOVhZJSMxV5XPwlePFNwqiPYUEj8QOFCXOAFcM50Q9dDC"

auth = tweepy.OAuthHandler(tweepy_consumer_key, tweepy_consumer_secret)
auth.set_access_token(tweepy_access_token, tweepy_access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit_notify=True) 

friends = api.friends(id=u,count=n)
followers = api.followers(id=u,count=n)

end = time.time()

twittersec.append(end - start)
friendslen.append(len(friends))
followerslen.append(len(followers))


# Calculate time for Twython

start = time.time()

twython_consumerkey = '2IiwQDV5c4OeUEA8PI0aqvg5g'
twython_consumersecret = 'RqEDv68Brt3JKVetWAeNFUObP5VeeRloBbQ0V9eqRFCerbas1I'

twitter = Twython(twython_consumerkey, twython_consumersecret, oauth_version=2)
twython_accesstoken = twitter.obtain_access_token()

twitter = Twython(twython_consumerkey, access_token=twython_accesstoken)

friends = twitter.get_friends_list(screen_name=u,count=n)
followers = twitter.get_followers_list(screen_name=u,count=n)

end = time.time()

twittersec.append(end - start)
friendslen.append(len(friends))
followerslen.append(len(followers))


# Calculating time for TweetPony

start = time.time()

api = tweetpony.API(consumer_key = "s08vLRIM5VnqCUqFVYTaV3ET9",
                    consumer_secret = "q4N5vB5KQrakhjAcWAk8dKOeTn4896cURoAg33A37UjGG2jJxf",
                    access_token = "897909419996041218-FIxS4NDoYbgrorjbxns9hYadZDiLg3J",
                    access_token_secret = "4p4RMc15bPp5Mknywkc1dY5HbbsJDwSnOGkcw4KLSFyQz")

followers = api.followers(screen_name = u, count=n)
friends = api.friends(screen_name = u, count=n)

end = time.time()

twittersec.append(end - start)
friendslen.append(len(friends))
followerslen.append(len(followers))


# Calculating time for TwitterAPI

start = time.time()

consumer_key = "7bFghx8idOToeNK8YCc1OrwQ5"
consumer_secret = "2GNYr9LBJJXJ3pfJKSlME4H6dXRYUt2kXXSnyRTQedS182Cirs"
access_token = "897909419996041218-VrQAbZABKWP91W5W3cyp6d5j5VSYeJX"
access_token_secret = "v6I9ev1C6FNJLzZFlOnPg7MfYex8KvBP4FuyK7xLq6Es5"

api = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)

followers = api.request('followers/list', {'screen_name':u, 'count':n})
friends = api.request('friends/list', {'screen_name':u, 'count':n})
        
end = time.time()

followernum = 0
friendnum = 0
for item in followers.get_iterator():
    if 'screen_name' in item:
        followernum +=1
for item in friends.get_iterator():
    if 'screen_name' in item:
        friendnum +=1

twittersec.append(end - start)
friendslen.append(friendnum)
followerslen.append(followernum)


# Plotting bar chart


print(twitterlib)
print(twittersec)
print(friendslen)
print(followerslen)

plt.bar(twitterlib, twittersec)
plt.xlabel("Twitter Library")
plt.ylabel("Time to access data (seconds)")
plt.show()

plt.bar(twitterlib, friendslen)
plt.xlabel("Twitter Library")
plt.ylabel("Number of friends accessed")
plt.show()

plt.bar(twitterlib, followerslen)
plt.xlabel("Twitter Library")
plt.ylabel("Number of followers accessed")
plt.show()

