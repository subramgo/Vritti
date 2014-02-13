# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 23:01:34 2011

@author: gopi
"""

from __future__ import division
from nltk import *
from misc.dpatterns.chainofcommands import Command

class bigrams(Command):
    """
    Command object to generate bigram of the given search result. Usually preceeded
    by search command object and followed by weightage object (OddsRatio). Leverages
    nltk libraries to generate bigrams
    
    """
    def __init__(self):
        """
        """
        self.maxDoc =50
        
    def process(self,context):
        #self.discoverBigrams(context)
        self.discoverCollocations(context)
        self.context = context
    
    def discoverCollocations(self,context):
        searchResult = context.searchResults
        scorer = BigramAssocMeasures.likelihood_ratio
        word_filter = lambda w: (len(w) < 3) or (not w.isalpha()) or (w.lower()  in nltk.corpus.stopwords.words('english'))
        allTokens =[]
        for r in searchResult:
            allTokens.extend(nltk.word_tokenize(r[1]))
        finder = nltk.collocations.BigramCollocationFinder.from_words(allTokens)
        finder.apply_freq_filter(3)
        finder.apply_word_filter(word_filter)
        for tup in finder.nbest(scorer,10):
            print tup
        bigrams =[' '.join(tup) for tup in finder.nbest(scorer,25)]
        print bigrams
        context.gramassociation = bigrams    
        context.termList = bigrams
    
    def discoverBigrams(self,context):
           searchResult = context.searchResults
           word_filter = lambda w: (len(w) > 3) and w.isalpha() and (w.lower() not in nltk.corpus.stopwords.words('english'))
           allwords =[]    
           for r in searchResult:
               tokens = nltk.word_tokenize(r[1])
               c_tokens = filter(word_filter,tokens)
               allwords.extend(c_tokens)
           allwords = set(allwords)    
           bigramtuples = nltk.bigrams(allwords)
           bigramList =[]
           for tup in bigramtuples:
               bigramList.append(' '.join(tup))
           context.termList = bigramList