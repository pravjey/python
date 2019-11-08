import tweepy
import json
import matplotlib.pyplot as plt
import pandas as pd
import time

tweepy_consumer_key = "cr9wJjmmT2CcGXqjsx7aWvsbA"
tweepy_consumer_secret = "QAjnpYxS59MEil5IEpJJzGP0WqDajklMcXxcxiaJLh9doBuQ6g"
tweepy_access_token = "897909419996041218-z27A8n2L6UcmUPuRbZhQBcpAAEk1Jxj"
tweepy_access_token_secret = "iOVhZJSMxV5XPwlePFNwqiPYUEj8QOFCXOAFcM50Q9dDC"

auth = tweepy.OAuthHandler(tweepy_consumer_key, tweepy_consumer_secret)
auth.set_access_token(tweepy_access_token, tweepy_access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit_notify=True)


# Reading list of important followers

print "Reading list of important followers"
print ("\n")
file = "CSV\\importantNodes.txt"
with open(file) as f:
    data = json.loads(f.read())

df = pd.DataFrame(columns = ["Followers", "Friends", "Tweets", "Likes", "Created", "Location"])


for node in data:
    results = api.get_user(id=node)
    df = df.append( {"Screen name": results.screen_name,
                     "Followers": float(results.followers_count),
                     "Friends": float(results.friends_count),
                     "Tweets": float(results.statuses_count),
                     "Likes": float(results.favourites_count),
                     "Created": results.created_at,
                     "Location": results.location,
                     "LocationYes": 1 if results.location != "" else 0,
                     "Description": results.description,
                     "DescriptionYes": 1 if results.description != "" else 0},
                   ignore_index = True)

print "Date and time of creation of account:"
print df["Created"]
print "\n"

print "Number of followers:"
print df["Followers"]
print "\n"

print "Friends:"
print df["Friends"]
print "\n"

print "Tweets:"
print df["Tweets"]
print "\n"

print "Likes:"
print df["Likes"]
print "\n"

df["Created"] = pd.to_numeric(df["Created"])

columns = ["Followers","Friends","Tweets","Likes","Created","LocationYes","DescriptionYes"]

print df.corr() 
export_csv = df.corr().to_csv(r"CSV\\correlation.csv", index = columns, header = True)



fakedf = pd.DataFrame()
fakedf = fakedf.append(df["Screen name"],ignore_index=True)
fakedf = fakedf.append(df["Followers"] / df["Tweets"],ignore_index=True)
fakedf = fakedf.append(df["Friends"] / df["Followers"],ignore_index=True)
fakedf = fakedf.append(df["DescriptionYes"],ignore_index=True)
currentTime = time.time()
currentTime_Days = (((currentTime / 60) / 60) / 24)
created_Days = (((df["Created"] / 60) / 60) / 24)
duration = created_Days - currentTime
fakedf = fakedf.append(df["Tweets"] / duration, ignore_index=True)
fakedf = fakedf.transpose()
print fakedf   
export_csv = fakedf.to_csv(r"CSV\\fakeusers.csv", index = ["Follower to Tweet","Friend to Follower","Description","Tweet to Duration"], header = True)


 


