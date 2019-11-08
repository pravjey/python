import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("CSV\compare.csv")

headings = ["Followers","Friends","Time"]
twitterlib = ["Tweepy","Twython","TweetPony","TwitterAPI"]
FollowersMean = []
FollowersStd = []
FriendsMean = []
FriendsStd = []
TimeMean = []
TimeStd = []


for i in twitterlib:
    for j in headings:
        vars()[i + "DF"] = df[df.Library == i]
        vars()[j + "Mean"].append(vars()[i + "DF"][j].mean())
        vars()[j + "Std"].append(vars()[i + "DF"][j].std())

meandf = pd.DataFrame({"Library": twitterlib,
                        "Followers": FollowersMean,
                        "Friends": FriendsMean,
                        "Time": TimeMean})

stddf = pd.DataFrame({"Library": twitterlib,
                        "Followers": FollowersStd,
                        "Friends": FriendsStd,
                        "Time": TimeStd})

print meandf
print stddf

meandf.plot(kind = "bar", x = "Library", y = "Time")
plt.savefig("TimeMean.png")
stddf.plot(kind = "bar", x = "Library", y = "Time")
plt.savefig("TimeStd.png")


