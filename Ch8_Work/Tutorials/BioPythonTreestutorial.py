#  this comes from https://github.com/kozo2/biopython-notebook/blob/nbsphinx/notebooks/13%20-%20Phylogenetics%20with%20Bio.Phylo.ipynb


# Imports
import Bio
import copy
from io import StringIO

from Bio import Phylo
from Bio.Phylo.Applications import PhymlCommandline
from Bio.Phylo.PAML import codeml
from Bio.Phylo.PhyloXML import Phylogeny


# Tree Simple
tree = Phylo.read(r"C:\Users\Mikaela\Desktop\F20\CIS699\CIS699\CIS699\Ch8_Work\simple.dnd", "newick")
print(tree)                     # Prints the node tree structure.
Phylo.draw_ascii(tree)          # Draws the tree in the console output
tree.rooted = True              # Creates the colorless tree graphic
Phylo.draw(tree)                # Colorless tree printed in a new window

# Below is a convenient tree method:
tree = tree.as_phyloxml()
tree = Phylogeny.from_tree(tree)

# Color assignment
tree.root.color = (128, 128, 128)
# tree.root.color = "#808080"        # This is one alternative
# tree.root.color = "gray"           # This is another

# 
mrca = tree.common_ancestor({"name": "E"}, {"name": "F"})
mrca.color = "salmon"

# If we happened to know exactly where a certain clade is in the tree, in terms of nested list entries,
# we can jump directly to that position in the tree by indexing it. Here, the index [0,1] refers to the second child of the first child of the root.
tree.clade[0, 1].color = "blue"
Phylo.draw(tree) #Colored tree


# The read function parses a single tree in the given file and returns it.
# Careful; it will raise an error if the file contains more than one tree, or no trees.
#from Bio import Phylo
tree = Phylo.read(r"C:\Users\Mikaela\Desktop\F20\CIS699\CIS699\CIS699\Ch8_Work\int_node_lables.nwk", "newick")
# print(tree)


# To handle multiple (or an unknown number of) trees, use the parse function iterates through each of the trees in the given file:
trees = Phylo.parse(r"C:\Users\Mikaela\Desktop\F20\CIS699\CIS699\CIS699\Ch8_Work\phyloxml_examples.xml", "phyloxml")
trees = list(trees)
# for tree in trees:
    # print(tree)


# Write a tree or iterable of trees back to file with the write function:
tree1 = trees[0]
Phylo.write(tree1, "data/tree1.nwk", "newick")

# To use strings as input or output instead of actual files, use StringIO as you would with SeqIO and AlignIO:
handle = StringIO("(((A,B),(C,D)),(E,F,G));")
tree = Phylo.read(handle, "newick")

#-------------------------------------------------------------------------------------------------
# View and export trees

# The simplest way to get an overview of a Tree object is to print it:
tree = Phylo.read(r"C:\Users\Mikaela\Desktop\F20\CIS699\CIS699\CIS699\Ch8_Work\example.xml", "phyloxml")
# print(tree)
# Phylo.draw_ascii(tree)

# The draw function draws a more attractive image using the matplotlib library.
# See the API documentation for details on the arguments it accepts to customize the output.
Phylo.draw(tree, branch_labels=lambda c: c.branch_length)