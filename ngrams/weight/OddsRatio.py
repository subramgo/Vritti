# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 20:34:49 2011

@author: gopi
"""
from __future__ import division
from misc.dpatterns.chainofcommands import Command
from lucene import Version,IndexReader, IndexSearcher,SimpleFSDirectory,File,QueryParser,SimpleAnalyzer

class OddsRatio(Command):
    """
    Implements a keyword weighting schemes proposed by Roberston and Sparck jones.
    Assigns weightage to words based on both presence of the word in relevant
    document and absence of the word in irrelevant document.
    """
    def __init__(self):
        """
        """
        self.gramList =[]
        self.weightThreshold =10
        self.MAX = 50


    
    def process(self,context):
        self.calculateWeight(context)
        context.termList = self.gramList
        print 'Finished odds ratio weight calculation'
        self.context = context
    
    def calculateWeight(self,context):
        #try:
            self.termList = context.termList            
            ramreader = IndexReader.open(context.ramIndex,True)
            store = SimpleFSDirectory(File(context.luceneDir))
            storereader = IndexReader.open(store)
            searcher = IndexSearcher(store)
            ramsearcher = IndexSearcher(context.ramIndex)
            # Number of documents in the collection    
            N = storereader.numDocs()
            # Number of relevant documents            
            R = ramreader.numDocs()
            analyzer = SimpleAnalyzer(Version.LUCENE_CURRENT)

            
            for w in self.termList:       
                searchString= "'" + w + "'"
                query = QueryParser(Version.LUCENE_CURRENT,"contents",analyzer).parse(searchString)
                # Number of relevant document having the term
                #r = ramsearcher.docFreq(Term("contents",w))
                hits = ramsearcher.search(query,self.MAX)
                r = hits.totalHits    
                # Number of documents having the term
                #n = searcher.docFreq(Term("contents",w))
                query = QueryParser(Version.LUCENE_CURRENT,context.searchField,analyzer).parse(searchString)
                hits = searcher.search(query,self.MAX)
                n = hits.totalHits
                if (R-r) > 0 and (n-r) > 0 and (N-n-R+r) > 0:
                    weight = (r/(R-r))/(((n-r)/(N-n-R+r)))
                else:
                    weight =0
                if weight > self.weightThreshold:            
                    self.gramList.append([w,weight])
            searcher.close()
            ramsearcher.close()
            storereader.close()
            ramreader.close()
        #except Exception,e:
        #    print 'error',e
            