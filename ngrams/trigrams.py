# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 00:52:14 2011

@author: gopi
"""

from __future__ import division
from nltk import *
from misc.dpatterns.chainofcommands import Command

class trigrams(Command):
    """
    Command object to generate trigram of the given search result. Usually preceeded
    by search command object and followed by weightage object (OddsRatio). Leverages
    nltk libraries to generate trigrams

    """
    def __init__(self):
        """
        """
        
    def process(self,context):
        self.discoverTrigrams(context)
        self.discoverCollocations(context)
        self.context = context

    def discoverCollocations(self,context):
        searchResult = context.searchResults
        scorer = TrigramAssocMeasures.likelihood_ratio
        word_filter = lambda w: (len(w) < 3) or (not w.isalpha()) or (w.lower()  in nltk.corpus.stopwords.words('english'))
        allTokens =[]
        for r in searchResult:
            allTokens.extend(nltk.word_tokenize(r[1]))
        finder = nltk.collocations.TrigramCollocationFinder.from_words(allTokens)
        finder.apply_freq_filter(3)
        finder.apply_word_filter(word_filter)
        trigrams =[' '.join(tup) for tup in finder.nbest(scorer,10)]
        context.gramassociation = trigrams    
    
    def discoverTrigrams(self,context):
           searchResult = context.searchResults
           word_filter = lambda w: (len(w) > 3) and w.isalpha() and (w.lower() not in nltk.corpus.stopwords.words('english'))
           allwords =[]    
           for r in searchResult:
               tokens = nltk.word_tokenize(r[1])
               c_tokens = filter(word_filter,tokens)
               allwords.extend(c_tokens)
           allwords = set(allwords)    
           trigramtuples = nltk.trigrams(allwords)
           trigramList =[]
           for tup in trigramtuples:
               trigramList.append(' '.join(tup))
           context.termList = trigramList        
        