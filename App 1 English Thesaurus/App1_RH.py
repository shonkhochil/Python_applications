# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 17:51:07 2020

@author: dr.rakibulhasan@gmail.com
"""

# import os
# os.listdir()

import json
df = json.load(open('data.json'))

# To get matches between words
from difflib import SequenceMatcher
print(SequenceMatcher(None, "rainn", "rain").ratio())

# Select a cutoffs for matches
from difflib import get_close_matches
get_close_matches("rainn", ["train", "help", "rain", "money"])
get_close_matches("rainn", df.keys(), cutoff=0.5)


# Program to find the definition of a word
def translation(w):
    w = w.lower()
    if w in df:
        return df[w]
    elif len(get_close_matches(w, df.keys())) > 0:
        yn = "Did you mean %s instead? Enter Y if Yes or N if No" % get_close_matches(w, df.keys())[0]
        if  yn == "Y":
            return df[get_close_matches(w, df.keys())[0]]
        elif yn == "N":
            return "This word does not exist. Please try a different word"
        else:
            return "We did not understand your entry."
    else:
        return "This Word does not exist. Please try a different word"

# Optimize Program -- Making User Friendly
w = input("Enter word: ")
output = translation(w)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)


