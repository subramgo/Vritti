# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 22:48:53 2011

@author: gopi
"""

import nltk

class wordproperties(object):
    def __init__(self):
        """
        """
        self.englishstopwords = nltk.corpus.stopwords.words('english')
        self.englishvocab = set(w.lower for w in nltk.corpus.words.words())
        
    def isStopWord(self,word):
        if word.lower() in self.englishstopwords:
            return True
            
            
    def getUnsualWords(self,words):
        textvocab = set(w.lower() for w in words if w.isalpha())
        return sorted(textvocab.difference(self.englishvocab))
        