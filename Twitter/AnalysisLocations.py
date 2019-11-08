from __future__ import division
import math
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

print ("Reading list of locations...")
rows = {}
for cat in headings:
    file = "Datasets\\" + cat + "locations.txt"
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
        location = rows[cat][i]
        blob = TextBlob(location)
        words = blob.ngrams(n=1)
        twograms = blob.ngrams(n=2)
        threegrams = blob.ngrams(n=3)
        for i in range(len(words)):
            if words[i][0] in vars()[cat1]:
                vars()[cat1][words[i][0]] += 1
            else:
                vars()[cat1][words[i][0]] = 1
        for i in range(len(twograms)):
            if twograms[i][0] in vars()[cat1]:
                vars()[cat1][twograms[i][0]] += 1
            else:
                vars()[cat1][twograms[i][0]] = 1
        for i in range(len(threegrams)):
            if threegrams[i][0] in vars()[cat1]:
                vars()[cat1][threegrams[i][0]] += 1
            else:
                vars()[cat1][threegrams[i][0]] = 1
    
for cat in headings:
    print "\n"
    print "Visualising textblobs for",cat
    cat1 = cat[1:len(cat)]
    vars()[cat1 + "highvol"] = {}
    objects = []
    xsum = 0
    for i in vars()[cat1]:
        xsum = xsum + vars()[cat1][i]
    average = xsum / len(vars()[cat1])
    print "Average number of occurances of an ngram", average
    for i in vars()[cat1]:
        if vars()[cat1][i] > math.ceil(average):
            objects.append(i)
            y_pos = np.arange(len(objects))
            vars()[cat1 + "highvol"][i] = vars()[cat1][i]
    plt.barh(y_pos, vars()[cat1 + "highvol"].values())
    plt.yticks(y_pos,objects,fontsize = 7)
    plt.title("High-frequency ngrams in " + cat1 + "'s followers' locations") 
    plt.xlabel("Number of occurances")
    plt.ylabel("Ngrams")
    plt.savefig("Pictures\\locations\\"+cat1+"_wordcount.png")
    plt.close()
