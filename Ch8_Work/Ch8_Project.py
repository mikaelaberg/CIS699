# 	• Finish from 8.4-8.5 -----------------DONE-----------------
# 	• Project Idea:
# 	• Clustering side topic to learn
# 		○ When data is unlabeled, what do we do and observe their characteristic
# 	• Hierarchical clustering
# 		○ Distance metric (think of the phylonogy tree)
# 		○ Microarrays ??
# 	• Find a data set of interest to myself, how to measure it maybe the measurements are there or duplicate a figure I've seen. Can be genomic/ Phylogenetic
# 	• Representing this information in the tree
#	• Dendo - gram tree
# 		○ Plot the tree.
# 	• Python programs for visualization:
# 	• Graph Vis/ Networkx/Plotly/igraph/matplotlib tree plot(decision tree in csykit learn)
# COVID data set to use and compare the SARS strains or other plagues???

# Use the dendrogram to try and find values of clusters of species
# then once that is obtained use that data for a type of decision tree??


#can I use this type of clustering to do a type of idenficiation for paralogs vs orhtologs???

# Links:
    # https://biopython.org/docs/1.75/api/Bio.Cluster.html
    # https://biopython.org/wiki/Phylo
    # https://github.com/shubhamjha97/hierarchical-clustering
    # https://www.tutorialspoint.com/biopython/biopython_cluster_analysis.htm
    # https://www-ncbi-nlm-nih-gov.ezproxy.gvsu.edu/proteinclusters
    # https://biopython-tutorial.readthedocs.io/en/latest/notebooks/13%20-%20Phylogenetics%20with%20Bio.Phylo.html


#  this comes from https://github.com/kozo2/biopython-notebook/blob/nbsphinx/notebooks/13%20-%20Phylogenetics%20with%20Bio.Phylo.ipynb

import Bio
import copy
from io import StringIO

from Bio import Phylo
from Bio.Phylo.Applications import PhymlCommandline
from Bio.Phylo.PAML import codeml
from Bio.Phylo.PhyloXML import Phylogeny

tree = Phylo.read(r"C:\Users\Mikaela\Desktop\F20\CIS699\CIS699\CIS699\Ch8_Work\simple.dnd", "newick")

print(tree)
Phylo.draw_ascii(tree)

tree.rooted = True
Phylo.draw(tree)  # Colorless tree

tree = tree.as_phyloxml()
tree = Phylogeny.from_tree(tree)
tree.root.color = (128, 128, 128)
tree.root.color = "#808080"        # This is one alternative
tree.root.color = "gray"           # This is another
mrca = tree.common_ancestor({"name": "E"}, {"name": "F"})
mrca.color = "salmon"
tree.clade[0, 1].color = "blue"

Phylo.draw(tree) #Colored tree

#from Bio import Phylo
tree = Phylo.read(r"C:\Users\Mikaela\Desktop\F20\CIS699\CIS699\CIS699\Ch8_Work\int_node_lables.nwk", "newick")
# print(tree)

trees = Phylo.parse(r"C:\Users\Mikaela\Desktop\F20\CIS699\CIS699\CIS699\Ch8_Work\phyloxml_examples.xml", "phyloxml")
# trees = list(trees)
# for tree in trees:
#     print(tree)

tree = Phylo.read(r"C:\Users\Mikaela\Desktop\F20\CIS699\CIS699\CIS699\Ch8_Work\example.xml", "phyloxml")
# print(tree)

# Phylo.draw_ascii(tree)
# Phylo.draw(tree, branch_labels=lambda c: c.branch_length)

#Sadly we need to monkey patch...
# import networkx
# from networkx.drawing import nx_agraph
# networkx.graphviz_layout = nx_agraph.graphviz_layout

# Phylo.draw_graphviz(tree, prog='dot')

# https://www.kaggle.com/rafay12/cancer-dna-patients-dataset
