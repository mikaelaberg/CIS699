#imports:
import numpy as np
import pandas as pd

import Bio
import copy
from io import StringIO

from Bio import Phylo
from Bio.Phylo.Applications import PhymlCommandline
from Bio.Phylo.PAML import codeml
from Bio.Phylo.PhyloXML import Phylogeny

#reading the file:
raw_file = pd.read_csv(r"C:\Users\Mikaela\Desktop\F20\CIS699\CIS699\CIS699\Ch8_Work\DNA_Dataset_Normalized.csv")
# data is from https://www.kaggle.com/rafay12/cancer-dna-patients-dataset

print(raw_file.head(3))


