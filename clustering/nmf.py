# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 19:24:43 2011
Implements non-negative matrix factorization
@author: gopi
"""

from __future__ import division
from misc.dpatterns.chainofcommands import Command
import numpy as np

class nmf(Command):
    def __init__(self):
        """
        """
        self.themes = []
        
    def process(self,context):
        weightmatrix,featurematrix = self.factorize(context.termdocumentmatrix)
        
        frows,fcols =  featurematrix.shape
        wrows,wcols = weightmatrix.shape 
        print weightmatrix.shape
        print frows,fcols
        
        # Loop over all the features
        for i in range(frows):
            slist=[]
            # list of words and their weights
            for j in range(fcols):
                slist.append((featurematrix[i,j],context.termList[j]))
            # Reverse the sort order list
            slist.sort()
            slist.reverse()
            
            # Print say five words for heading
            themeheading = [s[1][0] for s in slist[0:3]]
            
            # Get the list of documents for this heading
            doclist =[]
            for j in range(len(context.searchResults)):
                doclist.append((weightmatrix[j,i],context.searchResults[j]))
            
            doclist.sort()
            doclist.reverse()
            
            themedocs = [s[1] for s in doclist[0:5]]
            
            self.themes.append([' '.join(themeheading),themedocs])            
            
                       
                
        context.clusters = self.themes    
        self.context = context
        
       
    def factorize(self,vt,pc=5,iter=50):
        # transpose to create a document term matrix
        v = vt.transpose()
        ic,fc = v.shape
        
        #Initialize weight and feature matrix
        w = np.matrix([[np.random.random() for j in range(pc)] for i in range(ic)])        
        h = np.matrix([[np.random.random() for j in range(fc)] for i in range(pc)]) 
        
        for i in range(iter):
            wh = w*h
            cost = self.difcost(v,wh)
            if cost == 0: break
            
            if i%10 == 0 : print cost
            hn = w.transpose()*v
            hd = w.transpose()*w*h
            
            h = np.matrix(np.array(h)*np.array(hn)/np.array(hd))
            
            wn = v*np.transpose(h)
            wd = w*h*h.transpose()
        
            w = np.matrix(np.array(w)*np.array(wn)/np.array(wd))
            
        return w,h   
        
    def difcost(self,a,b):
        dif=0
        for i in range(np.shape(a)[0]):
            for j in range(np.shape(a)[1]):
                dif+=pow(a[i,j]-b[i,j],2)
        return dif       
                