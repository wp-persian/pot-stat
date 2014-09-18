#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#
# Contributer(s): Mani M. (manionline.org)

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
    if len(sys.argv) == 1:
        print("Usage: python pot-stat.py potfile1.pot potfile2.pot ...")
        exit(1)

    msgid = re.compile("msgid \"(.*)\"")
    wc = WordCounter()

    prev_msgs = 0
    prev_tokens = 0
    for filename in sys.argv[1:]:
        with open(filename) as lines:
            for l in lines:
                match = msgid.split(l)
                if len(match) == 3:
                    wc.update(match[1])
            
        print("%s: %s messages, %s tokens" % (filename, wc.update_counter - prev_msgs, len(wc.words) - prev_tokens), file=sys.stderr)
        prev_tokens = len(wc.words)
        prev_msgs = wc.update_counter

    print("Total: %s messages, %s tokens" % (wc.update_counter, len(wc.words)), file=sys.stderr)
    wc.toCSV()

if __name__ == "__main__":
    main()

