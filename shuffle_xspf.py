#!/usr/bin/env python2
from lxml import etree
import pydoc
import argparse
import sys
import random
parser = argparse.ArgumentParser(usage="shuffle_xspf playlist.xspf > shuffle_output.xspf")
parser.add_argument("source_playlist", help="the playlist you want to output a shuffled version of")
args = parser.parse_args()
e = ""
with open(sys.argv[1]) as f:
	e = etree.fromstring(f.read(), parser=etree.XMLParser())
newe1 = list(e[1])
random.shuffle(newe1)
for element in newe1:
	e[1].insert(0, element)
print(len(e[1]))
print(etree.tostring(e))
