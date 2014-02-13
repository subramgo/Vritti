# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 11:44:58 2011

@author: gopi
"""

class searchContext(object):
    """
    Data object passed to every command object
    in the invoked chain. Every command object
    retrieves its input from this object and
    puts its results back, for the next object
    in the sequence to consume
    """
    def __init__(self,luceneDir=None, inputDir=None, searchString=None,
                 searchField=None,searchResults=None,termList=None,
                 gramassociation =None,
                 termdocumentmatrix =None,wordsimilaritymatrix = None,
                 ramIndex = None,clusters=None):
        self.luceneDir = luceneDir
        self.ramIndex = ramIndex
        self.inputDir = inputDir
        self.searchString = searchString
        self.searchField = searchField
        self.searchResults = searchResults
        self.termList = termList
        self.termdocumentmatrix = termdocumentmatrix
        self.wordsimilaritymatrix = wordsimilaritymatrix
        self.gramassociation = gramassociation
        self.clusters = clusters
