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

#-----------------PART A----------------------------------------------------

import copy
from io import StringIO

from Bio import Phylo
from Bio.Phylo.Applications import PhymlCommandline
from Bio.Phylo.PAML import codeml
from Bio.Phylo.PhyloXML import Phylogeny

# %matplotlib inline

tree = Phylo.read("data/simple.dnd", "newick")