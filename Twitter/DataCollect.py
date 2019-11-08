import tweepy
import json

tweepy_consumer_key = "ACDJueGDMNHhASuIrekBEmFL9"
tweepy_consumer_secret = "2VLoL0euOO6l2XFVfK165Y0E5kEGCusCGdku7Ac51A6zTkivgH"
tweepy_access_token = "897909419996041218-MqbSYmspOewbb4mP4MOpeJdjdPeNrTT"
tweepy_access_token_secret = "szX8w3GbRY7qZXb484ROJdS5RMUlkuCVkYmNdeLrZ0vP2"

auth = tweepy.OAuthHandler(tweepy_consumer_key, tweepy_consumer_secret)
auth.set_access_token(tweepy_access_token, tweepy_access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit_notify=True)


govCats = ["@DiploMog",
           "@HMCabinetCat",
           "@Number10cat",
           "@PalmerstonFOCat",
           "@PalmerstonCat",
           "@TreasuryMog",
           "@HMTreasuryCat"]

for cat in govCats:
    print "Reading from", cat, "......"
    friends = api.friends(id=cat,count=200)
    followers = api.followers(id=cat,count=200)
    tweets = api.user_timeline(screen_name=cat,count=5000)
    friends_list = []
    for i in friends:
        friends_list.append(i.screen_name)
    followers_list = []
    location_list = []
    description_list = []
    for i in followers:
        followers_list.append(i.screen_name)
        location_list.append(i.location)
        description_list.append(i.description)
    tweets_list = []
    for i in tweets:
        tweets_list.append(i.text)
    friends_file = "Datasets\\" + cat + "friends.txt"
    followers_file = "Datasets\\" + cat + "followers.txt"
    tweets_file = "Datasets\\" + cat + "tweets.txt"
    location_file = "Datasets\\" + cat + "locations.txt"
    description_file = "Datasets\\" + cat + "descriptions.txt"
    with open(friends_file, "w") as f:
        json.dump(friends_list, f)
    with open(followers_file, "w") as f:
        json.dump(followers_list, f)
    with open(tweets_file, "w") as f:
        json.dump(tweets_list, f)
    with open(location_file, "w") as f:
        json.dump(location_list, f)    
    with open(description_file, "w") as f:
        json.dump(description_list, f)


    

    
