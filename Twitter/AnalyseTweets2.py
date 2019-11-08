import networkx as nx
import matplotlib.pyplot as plt

headings = ["@DiploMog",
           "@HMCabinetCat",
           "@Number10cat",
           "@PalmerstonFOCat",
           "@PalmerstonCat",
           "@TreasuryMog",
           "@HMTreasuryCat"]


catGraph = nx.DiGraph()
catGraph.add_node("@DiploMog")
catGraph.add_node("@HMCabinetCat")
catGraph.add_node("@HMTreasuryCat")
catGraph.add_node("@Number10cat")
catGraph.add_node("@PalmerstonCat")
catGraph.add_node("@PalmerstonFOCat")
catGraph.add_node("@TreasuryMog")

catGraph.add_node("@foreignoffice")
catGraph.add_node("@LawrenceDipCat")
catGraph.add_node("@SMcDonaldFCO")
catGraph.add_node("@BDCH")
catGraph.add_node("@Battersea")
catGraph.add_node("@PoliticalPics")
catGraph.add_node("@justin_ng")
catGraph.add_node("@Stoughton_p")
catGraph.add_node("@Number11Dog")
catGraph.add_node("@Zilla_Mon")
catGraph.add_node("@YourCatmagazine")

catGraph.add_edge("@DiploMog","@DiploMog")
catGraph.add_edge("@DiploMog","@foreignoffice")
catGraph.add_edge("@DiploMog","@LawrenceDipCat")
catGraph.add_edge("@DiploMog","@SMcDonaldFCO")
catGraph.add_edge("@DiploMog","@BDCH")
catGraph.add_edge("@DiploMog","@Battersea")
catGraph.add_edge("@HMCabinetCat", "@TreasuryMog")
catGraph.add_edge("@HMCabinetCat", "@HMTreasuryCat")
catGraph.add_edge("@HMCabinetCat", "@DiploMog")
catGraph.add_edge("@HMCabinetCat", "@Number10cat")
catGraph.add_edge("@Number10cat", "@PoliticalPics")
catGraph.add_edge("@Number10cat", "@justin_ng")
catGraph.add_edge("@HMTreasuryCat","@Number10cat")
catGraph.add_edge("@PalmerstonCat","@Number10cat")
catGraph.add_edge("@PalmerstonCat", "@TreasuryMog")
catGraph.add_edge("@PalmerstonCat","@foreignoffice")
catGraph.add_edge("@PalmerstonCat","@YourCatmagazine")
catGraph.add_edge("@PalmerstonCat","@Battersea")
catGraph.add_edge("@PalmerstonFOCat","@Number10cat")
catGraph.add_edge("@PalmerstonFOCat","@PoliticalPics")
catGraph.add_edge("@PalmerstonFOCat","@Stoughton_p")
catGraph.add_edge("@TreasuryMog","@HMCabinetCat")
catGraph.add_edge("@TreasuryMog","@DiploMog")
catGraph.add_edge("@TreasuryMog","@Number10cat")
catGraph.add_edge("@TreasuryMog","@Number11Dog")
catGraph.add_edge("@TreasuryMog","@Zilla_Mon")


print "Number of users in global network:", catGraph.number_of_nodes()
print "Number of connections in global netwwork:", catGraph.number_of_edges()
print "\n"


nx.draw(catGraph,with_labels=True)
plt.show()
plt.savefig("Pictures\\" + "catNetwork2.png")
plt.close()


