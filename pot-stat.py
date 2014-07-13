#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: INFO

from __future__ import print_function
import sys
import re
import operator

class WordCounter:
    def __init__(self, blacklist = None):
        self.tokenizer = re.compile("\W+")#re.compile("\b(\w)+\b")
        self.blacklist = blacklist if isinstance(blacklist, set) else set()
        self.reset()

    def reset(self):
        self.words = dict()
        self.update_counter = 0
    
    def update(self, text):
        self.update_counter += 1
        words = self.tokenizer.split(text)
        for w in words:
            w = w.lower()
            if len(w)>1 and w not in self.blacklist:
                if w in self.words.keys():
                    self.words[w] += 1
                else:
                    self.words[w] = 1
    def toCSV(self):
        for word, count in sorted(
                self.words.items(), key=operator.itemgetter(1), reverse=True):
            print("%s, %s" % (word, count), file=sys.stdout)

def main():
    if len(sys.argv) != 2:
        print("Usage: python pot-stat.py potfile.pot")
        exit(1)

    msgid = re.compile("msgid \"(.*)\"")
    wc = WordCounter()

    filename = sys.argv[1]
    with open(filename) as lines:
        for l in lines:
            match = msgid.split(l)
            if len(match) == 3:
                wc.update(match[1])
            
    print("%s: %s messages, %s tokens" % (filename, wc.update_counter, len(wc.words)), file=sys.stderr)
    wc.toCSV()

if __name__ == "__main__":
    main()
