#!/usr/bin/env python

import sys

def urlme(filename):
    print "![{0}](/assets/imgur-Agaln/{0})".format(filename)

fileto = sys.argv[1]

f = open(fileto, 'r')

for x in f.readlines():
    files = x.strip().split()
    for fi in files:
        urlme(fi)

#print f.readlines
