# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 19:25:58 2011

@author: gopi
"""

from __future__ import division
from misc.dpatterns.chainofcommands import Command
from lucene import IndexReader,Version,IndexSearcher,QueryParser,SimpleAnalyzer
import numpy as np


class tfidf(Command):
    """
    """
    def __init__(self):
        """
        """
        # Number of documents
        self.N = 0 
        # Number of terms
        self.m = 0
        # Individual terms
        self.unigramList = None
        
    def process(self,context):
        self.unigramList = context.termList
        self.ramreader = IndexReader.open(context.ramIndex,True)
        self.ramsearcher = IndexSearcher(context.ramIndex)
        self.N = self.ramreader.numDocs()
        self.m = len(self.unigramList)
        self.createTermDocumentMatrix()
        self.ramsearcher.close()
        self.ramreader.close()
        context.termdocumentmatrix = self.termdocumentMatrix
        print 'finished creating term document matrix'
        self.context = context
        
        
    def createTermDocumentMatrix(self):
       self.termdocumentMatrix = np.zeros((self.m,self.N),dtype=int)
       analyzer = SimpleAnalyzer(Version.LUCENE_CURRENT)
       for index,word in enumerate(self.unigramList):
                searchString= "'" + word[0] + "'"
                query = QueryParser(Version.LUCENE_CURRENT,"contents",analyzer).parse(searchString)
                hits = self.ramsearcher.search(query,self.N)
                for hit in hits.scoreDocs:
                    self.termdocumentMatrix[index,hit.doc] = hits.totalHits    

               
  