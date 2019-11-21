import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pylab as plt

parties = ["Conservatives",
           "UKLabour",
           "LibDems",
           "theSNP",
           "TheGreenParty",
           "brexitparty_uk",
           "Plaid_Cymru"]

for party in parties:
    filename = party + ".txt"
    file = open(filename,"r")
    vars()[party + "list"] = file.readlines()    

for party in parties:
    vars()[party + "dict"] = {}
    for i in vars()[party + "list"]:
        a = i.split(",")
        a[0] = a[0][0:10]
        if a[1][len(a[1])-1] == "\n":
            a[1] = a[1][0:(len(a[1])-1)]
        else:
            a[1] = a[1][0:(len(a[1]))]
        a[1] = int(a[1])
        vars()[party + "dict"][a[0]] = a[1]


for party in parties:
    vars()[party + "list"] = sorted(vars()[party + "dict"].items())
    vars()[party + "df"] = pd.DataFrame.from_dict(vars()[party + "dict"], orient="index")
    x,y = zip(*vars()[party + "list"])
    plt.plot(x,y, label = party)
    plt.xlabel("Date")
    plt.ylabel("Number of followers")
    plt.title("Number of Twitter followers over time")
    plt.xticks(fontsize=7, rotation=0)
    plt.legend(loc = "upper right")
    
plt.show()

growth = []
for party in parties:
    print party
    print vars()[party + "df"]
    a = int(vars()[party + "df"].max() - vars()[party + "df"].min())
    growth.append(a)

df = pd.DataFrame({"Political Party": parties,
                   "Change in Number of Followers": growth})
df.plot(kind = "bar", x = "Political Party", y = "Change in Number of Followers")
plt.title("Increase in followers since 9/10/2019")
plt.xticks(fontsize=7, rotation=0)
plt.show()
    
