# -*- coding: utf-8 -*-
# this utf-8 comment tells python to use standard English lang
"""
Created on Sat Mar 26 14:40:13 2016

@author: Bhuti
"""

#bilingual dictionary : Spanish

translations = {
"merry": "feliz",
"christmas": "navidad",
"and": "y",
"happy": "feliz",
"new": "nuevo",
"year": "año", # ñ doesn't exist in python [not english] - change utf-8 can address it
}
# "," after the last entry doesn't make any difference; {} don't require indentation

for english, spanish in translations.items():
    print(english, "translations to:", spanish)
