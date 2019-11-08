import tweepy
import pandas as pd
import matplotlib.pyplot as plt

# Obtain access to Twitter's Application Programming Interace

tweepy_consumer_key = "cr9wJjmmT2CcGXqjsx7aWvsbA"
tweepy_consumer_secret = "QAjnpYxS59MEil5IEpJJzGP0WqDajklMcXxcxiaJLh9doBuQ6g"
tweepy_access_token = "897909419996041218-z27A8n2L6UcmUPuRbZhQBcpAAEk1Jxj"
tweepy_access_token_secret = "iOVhZJSMxV5XPwlePFNwqiPYUEj8QOFCXOAFcM50Q9dDC"

auth = tweepy.OAuthHandler(tweepy_consumer_key, tweepy_consumer_secret)
auth.set_access_token(tweepy_access_token, tweepy_access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit_notify=True)


# Extracting data about Government cat. Output produced to screen and CSV file.

govCats = ["@DiploMog",
           "@HMCabinetCat",
           "@Number10cat",
           "@PalmerstonFOCat",
           "@PalmerstonCat",
           "@TreasuryMog",
           "@HMTreasuryCat"]

countdf = pd.DataFrame(columns = ["Gov cat","Followers","Friends","Tweets","Likes","Joined"])

for cat in govCats:
    cat1 = cat[1:len(cat)] # omits '@' character from the username
    user = api.get_user(cat1)
    countdf = countdf.append({"Gov cat": user.screen_name,
                              "Followers": user.followers_count,
                              "Friends": user.friends_count,
                              "Tweets": user.statuses_count,
                              "Likes": user.favourites_count,
                              "Joined": user.created_at},
                             ignore_index=True)

countdf = countdf.sort_values("Followers")

export_csv = countdf.to_csv(r"basicdata.csv", index = None, header = True)

print countdf


# Calculating the mean, median and standard deviation for data for the number
# of followers, number of friends and the number of tweets and likes made.
# Output produced to screen and CSV file.

headings = ["Followers",
            "Friends",
            "Tweets",
            "Likes"]

dfMean = []
dfMedian = []
dfDiff = []
dfStd = []

for column in headings:
    countdf[column] = countdf[column].astype(float)
    dfMean.append(countdf[column].mean(axis = 0))
    dfMedian.append(countdf[column].median(axis = 0))
    dfStd.append(countdf[column].std(axis = 0))

statsdf = pd.DataFrame({"Attribute": headings,
                        "Mean": dfMean,
                        "Median": dfMedian,
                        "St. Dev": dfStd})

export_csv = statsdf.to_csv(r"basicstats.csv", index = None, header = True)

print statsdf


# Number of tweets converted to numeric, in order to produce scatterplots
# showing relationship to duration of twitter page.

countdf["Joined"] = pd.to_numeric(countdf.Joined)

print "Producing Tweets versus Followers..."
countdf.plot(kind="scatter", x="Tweets", y="Followers", color="red")
plt.savefig("TweetsFollowers.png")
print "Producing Tweets versus Friends..."
countdf.plot(kind="scatter", x="Tweets", y="Friends", color="blue")
plt.savefig("TweetsFriends.png")
print "Producing Tweets versus Likes..."
countdf.plot(kind="scatter", x="Tweets", y="Likes", color="green")
plt.savefig("TweetsLikes.png")
print "Producing Tweets versus Joined..."
countdf.plot(kind="scatter", x="Tweets", y="Joined", color="black")
plt.savefig("TweetsJoined.png")

print "Producing Joined versus Followers..."
countdf.plot(kind="scatter", x="Joined", y="Followers", color="red")
plt.savefig("JoinedFollowers.png")
print "Producing Joined versus Friends..."
countdf.plot(kind="scatter", x="Joined", y="Friends", color="blue")
plt.savefig("JoinedFriends.png")
print "Producing Joined versus Likes..."
countdf.plot(kind="scatter", x="Joined", y="Likes", color="green")
plt.savefig("JoinedLikes.png")
print "Producing Joined versus Tweets..."
countdf.plot(kind="scatter", x="Joined", y="Tweets", color="black")
plt.savefig("JoinedTweets.png")


# Relationship between number of followers, friends and likes.

print "Producing Followers versus Friends..."
countdf.plot(kind="scatter", x="Followers", y="Friends", color="red")
plt.savefig("FollowersFriend.png")
print "Producing Followers versus Likes..."
countdf.plot(kind="scatter", x="Followers", y="Likes", color="blue")
plt.savefig("FollowersLikes.png")
print "Producing Friends versus Likes..."
countdf.plot(kind="scatter", x="Friends", y="Likes", color="green")
plt.savefig("FriendsLikes.png")
    
print "End Scatterplots"





    






