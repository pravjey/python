import tweepy
import datetime

tweepy_consumer_key = "ACDJueGDMNHhASuIrekBEmFL9"
tweepy_consumer_secret = "2VLoL0euOO6l2XFVfK165Y0E5kEGCusCGdku7Ac51A6zTkivgH"
tweepy_access_token = "897909419996041218-MqbSYmspOewbb4mP4MOpeJdjdPeNrTT"
tweepy_access_token_secret = "szX8w3GbRY7qZXb484ROJdS5RMUlkuCVkYmNdeLrZ0vP2"

auth = tweepy.OAuthHandler(tweepy_consumer_key,  tweepy_consumer_secret)
auth.set_access_token(tweepy_access_token, tweepy_access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit_notify=True)

now = datetime.datetime.now()

parties = ["@Conservatives",
           "@UKLabour",
           "@LibDems",
           "@theSNP",
           "@TheGreenParty",
           "@brexitparty_uk",
           "@Plaid_Cymru"]

for party in parties:
    party1 = party[1:len(party)] 
    user = api.get_user(party)
    file = party1 + ".txt"
    try:
        output = open(file, "r")
    except IOError:
        empty = True
    else:
        empty = False
        output.close()
    output = open(file, "a")
    if not empty:
        output.write("\n")
    output.write(str(now))
    output.write(",")
    output.write(str(user.followers_count))
    output.close()
        

