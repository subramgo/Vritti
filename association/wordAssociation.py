# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 18:48:41 2011

@author: gopi
"""
from __future__ import division
from misc.dpatterns.chainofcommands import Command
import numpy as np
from collections import defaultdict

class wordAssociation(Command):
    """
    Finds association between two words. Words can be unigram or bigram or trigrams
    Usually called in a chain after creating term document matrix. Using the term document 
    matrix as input, produces word associations.
    Algorithm :
        input : Term document matrix ,A
    1.  A * transpose(A) = B, a term term, coweight matrix
    2.  Produce a similarity matrix using C, using coweight matrix B
            calculate jaccards coefficient, tij = tij/(tii+tjj-tij) 
    3.  Unit normalize matrix B
    4.  Calculate cosine matrix, C = B * transpose(B)
    
    Cosine matrix C, has every term in the rows, and columns indicate the associated
    terms. The entries are the weight
    
    Based on the weight, for a given term, a set of associated terms are found    
    
    This algorithm is based on the association and scala cluster generation algorithm
    by Dr Garcia.
    http://www.miislita.com/information-retrieval-tutorial/association-scalar-clusters-tutorial-1.pdf
    """
    def __init__(self):
        """
        """
        #: Number of documents in term document matrix 
        self.N = 0
        #: No of terms in input gram list
        self.m = 0
        #: term document matrix
        self.termdocumentmatrix = None
        #: List of unigrams/terms present in the term document matrix
        self.unigramList = None
        #: Cosine similarity matrix used for association discovery
        self.cosinematrix = None
        #: Dictionary of terms and associated terms
        self.associationDict = defaultdict(list)
        
    def process(self,context):
        self.gramList = context.termList
        self.termdocumentMatrix = context.termdocumentmatrix        
        self.m,self.N = context.termdocumentmatrix.shape
        self.createwordAssociationMatrix()
        for i,w in enumerate(self.gramList):
            a = self.cosinematrix[i,1:]
            matchinindex = []
            for j in range(1,5):
                ind = a.argmax()
                matchinindex.append(ind)
                a[0,ind] =-1
            self.associationDict[w[0]] = [self.gramList[indx][0] for indx in matchinindex]            
        
        context.wordsimilaritymatrix     =self.cosinematrix
        context.gramassociation = self.associationDict
        self.context = context

    def createwordAssociationMatrix(self):
        tdmatrix = np.matrix(self.termdocumentMatrix)
        coweightmatrix = tdmatrix * tdmatrix.transpose()
        m,n = coweightmatrix.shape
        similaritymatrix = np.matrix(np.zeros((m,n),dtype=float))
        for i in range(0,m):
            for j in range(0,n):
                similaritymatrix[i,j] = coweightmatrix[i,j]/(coweightmatrix[i,i] + coweightmatrix[j,j] - coweightmatrix[i,j])
        for i in range(0,m):
            similaritymatrix[i,:] = similaritymatrix[i,:] * 1/similaritymatrix[i,:].sum()
        self.cosinematrix = similaritymatrix * similaritymatrix.transpose()
        

           
       