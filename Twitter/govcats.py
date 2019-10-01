import tweepy
import pandas as pd

# Obtain access to Twitter's Application Programming Interace

tweepy_consumer_key = "..."
tweepy_consumer_secret = "..."
tweepy_access_token = "..."
tweepy_access_token_secret = "..."

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
