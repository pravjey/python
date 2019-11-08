from __future__ import division
import json
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from textblob import TextBlob

headings = ["@DiploMog",
           "@HMCabinetCat",
           "@Number10cat",
           "@PalmerstonFOCat",
           "@PalmerstonCat",
           "@TreasuryMog",
           "@HMTreasuryCat"]

print ("Reading list of tweets...")
rows = {}
for cat in headings:
    file = "Datasets\\" + cat + "tweets.txt"
    with open(file) as f:
        data = json.loads(f.read())
    rows[cat] = data

print ("Reading stopwords...")
# https://en.wikipedia.org/wiki/Stop_words,
# https://www.textfixer.com/tutorials/common-english-words.txt
file = "Datasets\\stopwords.txt"
with open(file) as f:
    stopwords = f.read()
stopwords = stopwords.split(",")

for cat in headings:
    print "Calculating textblobs for",cat
    cat1 = cat[1:len(cat)]
    vars()[cat1] = {}
    for i in range(len(rows[cat])):
        tweet = rows[cat][i]
        blob = TextBlob(tweet)
        words = blob.ngrams(n=1)
        twograms = blob.ngrams(n=2)
        threegrams = blob.ngrams(n=3)
        for i in range(len(words)):
            if words[i][0] in stopwords or words[i][0][0:4] == "t.co":
                continue
            elif words[i][0][0:4] == "http" or words[i][0][0:5] == "https":
                continue
            elif words[i][0][0] == "@" or words[i][0] == "????":
                continue
            elif words[i][0] in vars()[cat1]:
                vars()[cat1][words[i][0]] += 1
            else:
                vars()[cat1][words[i][0]] = 1
        for i in range(len(twograms)):
            if twograms[i][0] in stopwords or twograms[i][0][0:4] == "t.co":
                continue
            elif twograms[i][0][0:4] == "http" or twograms[i][0][0:5] == "https":
                continue
            elif twograms[i][0] in vars()[cat1]:
                vars()[cat1][twograms[i][0]] += 1
            else:
                vars()[cat1][twograms[i][0]] = 1
        for i in range(len(threegrams)):
            if threegrams[i][0] in stopwords or threegrams[i][0][0:4] == "t.co":
                continue
            elif threegrams[i][0][0:4] == "http" or threegrams[i][0][0:5] == "https":
                continue
            elif threegrams[i][0] in vars()[cat1]:
                vars()[cat1][threegrams[i][0]] += 1
            else:
                vars()[cat1][threegrams[i][0]] = 1
    
for cat in headings:
    print "Visualising textblobs for",cat
    cat1 = cat[1:len(cat)]
    vars()[cat1 + "highvol"] = {}
    objects = []
    for i in vars()[cat1]:
        if vars()[cat1][i] > 15:
            objects.append(i)
            y_pos = np.arange(len(objects))
            vars()[cat1 + "highvol"][i] = vars()[cat1][i]
    plt.barh(y_pos, vars()[cat1 + "highvol"].values())
    plt.yticks(y_pos,objects,fontsize = 7)
    plt.title("High-frequency ngrams in " + cat1 + "'s tweets") 
    plt.xlabel("Number of occurances")
    plt.ylabel("Ngrams")
    plt.savefig("Pictures\\tweets\\"+cat1+"_wordcount.png")
    plt.close()
