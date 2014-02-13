# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 11:40:18 2011

@author: gopi
"""
from __future__ import division
from misc.dpatterns.chainofcommands import Command
from lucene import IndexReader
from nltk import *

class unigrams(Command):
    """
    Command object to generate unigram of the given search result. Usually preceeded
    by search command object and followed by weightage object (OddsRatio). Leverages
    apache lucene libraries to generate unigrams

    """
    def __init__(self):
         self.termdict ={}
         self.termList =[]
         self.unigramList =[]
         self.df = {}
        
    def process(self,context):
        self.loadtermFreq(context)
        context.termList = self.termList
        print 'finished unigrams'
        self.context = context
    
    
    def loadtermFreq(self,context)    :
        word_filter = lambda w: (len(w) > 3) and (w.isalpha()) and (w.lower() not in nltk.corpus.stopwords.words('english'))
        try:
            reader = IndexReader.open(context.ramIndex,True)
            wordList =[]
            termenum = reader.terms()
            while termenum.next():
                wordList.append(termenum.term().text())
            self.termList = filter(word_filter,wordList)
        except Exception,e:
            print 'Unable to read Ram Index',e
        
    
      
