# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 17:31:34 2022

@author: sameed.atta
"""

sentence = input("Enter a sentence: ")
counts = {} # {word: count, ...}
for word in sentence.split():
    if word in counts:

# we have seen this word before
        counts[word] += 1
else:
# this is the first time this word occurs
    counts[word] = 1
print() # display an empty line
for word, count in counts.items():
    if count == 1:
# "1 times" looks weird
        print(word, "appears once in the sentence")
else:
    print(word, "appears", count, "times in the sentence")
