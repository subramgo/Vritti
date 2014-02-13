# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 19:50:27 2011

@author: gopi
"""

from __future__ import division
from misc.dpatterns.chainofcommands import Command
from numpy.linalg import svd

class singularvalue(Command):
    def __init__(self):
        """
        """
        self.wordsimilaritymatrix = None
        self.U = None
        self.Ur = None
        self.sigma = None
        self.sigmar = None
        self.V = None
        self.Vt = None
        self.Vtr = None
        self.rankApprox = 5
        self.terms = None
        
    def process(self,context):
        self.wordsimilaritymatrix = context.wordsimilaritymatrix
        self.terms = context.termList
        self.U,self.sigma,self.V = svd(self.wordsimilaritymatrix)
        self.Vt = self.V.transpose()
        
        print self.U.shape
        print self.sigma.shape
        print self.V.shape        
        
        # Reduced matrices doing a rank n approximation
#        self.Ur = self.U[:,0:self.rankApprox]        
#        self.Vtr = self.Vt[0:self.rankApprox,:]
#        
#        feature1 = self.Ur[:,0]
#        feature2 = self.Ur[:,1]
#        feature3 = self.Ur[:,2]        
#
#        print feature1.shape
#        print 'feature1 terms'
#        for i in xrange(3):
#            ind = feature1.argmax()
#            
#            print self.terms[ind],':',str(ind)
#            feature1[ind] = -1
#                
#        print feature2.shape
#        print 'feature2 terms'
#        for i in xrange(3):
#            ind = feature2.argmax()
#            
#            print self.terms[ind],':',str(ind)
#            feature2[ind] = -1
#        print feature3.shape
#        print 'feature3 terms'
#        for i in xrange(3):
#            ind = feature3.argmax()
#            
#            print self.terms[ind],':',str(ind)
#            feature3[ind] = -1
        
        
        self.context = context
        
        
    