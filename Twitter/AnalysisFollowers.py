import pandas as pd
import json
import networkx as nx
import matplotlib.pyplot as plt
import operator

headings = ["@DiploMog",
           "@HMCabinetCat",
           "@Number10cat",
           "@PalmerstonFOCat",
           "@PalmerstonCat",
           "@TreasuryMog",
           "@HMTreasuryCat"]


# Read followers data from text file into dictionary and convert into
# pandas DataFrame

print "Reading followers data..."

rows = {}
for cat in headings:
    file = "Datasets\\" + cat + "followers.txt"
    with open(file) as f:
        data = json.loads(f.read())
    rows[cat] = data


# Read friends data from text file into dictionary and convert into
# pandas DataFrame

rows1 = {}
for cat in headings:
    file = "Datasets\\" + cat + "friends.txt"
    with open(file) as f:
        data = json.loads(f.read())
    rows1[cat] = data


# Assuming each government cat is at the centre of its own network and some users
# follow more than one government cat, create a global network of all government
# cats with followers and friends to identify connecting users.

catGraph = nx.DiGraph()
for cat in rows:
    catGraph.add_node(cat)
    for follower in rows[cat]:
        catGraph.add_node(follower)
        catGraph.add_edge(follower,cat)
for cat in rows1:
    for friend in rows1[cat]:
        if friend not in catGraph:
            catGraph.add_node(friend)
        catGraph.add_edge(cat,friend)

print "Number of users in global network:", catGraph.number_of_nodes()
print "Number of connections in global netwwork:", catGraph.number_of_edges()
print "\n"

num = range(100)
degreedf = pd.DataFrame()

# Calculate number of nodes with n degrees
degree = []
for n in num:
    count = 0
    for node in catGraph.degree():
        if node[1] == n:
            count += 1
    degree.append(count)


# Calculate number of nodes with n in-degrees
in_degree = []
for n in num:
    count = 0
    for node in catGraph.in_degree():
        if node[1] == n:
            count += 1
    in_degree.append(count)


# Calculate number of nodes with n out-degrees
out_degree = []
for n in num:
    count = 0
    for node in catGraph.out_degree():
        if node[1] == n:
            count += 1
    out_degree.append(count)


# Store data about node degrees in a Dataframe and save in CSV file
degreedf = pd.DataFrame({ "Degree": num,
                          "Degree nodes": degree,
                          "In-Degree nodes": in_degree,
                          "Out-Degree nodes": out_degree})
export_csv = degreedf.to_csv(r"CSV\\" + "degree.csv", index = None, header = True)


#Plot global network of government cats, followers and friends and save as picture file
nx.draw(catGraph)
plt.show()
plt.savefig("Pictures\\" + "catNetwork.png")
plt.close()


important_degree = []
important_indegree = []
important_outdegree = []
print "\n","most important users by degree" 
for node in catGraph.degree():
    if node[1] == 4 or node[1] == 5 or node[1] == 6:
        important_degree.append(node[0])
        print node[0]
print "\n","most important users by in-degree"
for node in catGraph.in_degree():
    if node[1] == 2 or node[1] == 3 or node[1] == 4:
        important_indegree.append(node[0])
        print node[0]
print "\n","most important users by out-degree"        
for node in catGraph.out_degree():
    if node[1] == 4 or node[1] == 5 or node[1] == 6 or node[1] == 8 or node[1] == 19 or node[1] == 30:
        important_outdegree.append(node[0])
        print node[0]

print "\n","most important users"
important_common = important_indegree and important_outdegree
for node in important_common:
    print node
file = "CSV\\" + "importantNodes.txt"
with open(file,"w") as f:
    json.dump(important_common,f)


    

