# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 18:05:42 2011

@author: gopi
"""
import web
import json
from search.Search import search
from misc.dpatterns.chainofcommands import Chain
from context.searchContext import searchContext
from ngrams.unigrams import unigrams
from ngrams.bigrams import bigrams
from ngrams.trigrams import trigrams
from association.wordAssociation import wordAssociation
from nlp.textMatrices import tfidf
from index.RAMIndex import RAMIndex
from ngrams.weight.OddsRatio import OddsRatio
from clustering.nmf import nmf


import lucene
lucene.initVM()
vm_env = lucene.getVMEnv()

urls = (
    '/search/(.*)', 'searchservice',
    '/unigrams/(.*)','unigramservice',
    '/bigrams/(.*)','bigramservice',
    '/trigrams/(.*)','trigramservice',
    '/unigramassociation/(.*)','unigramassociation',
    '/bigramassociation/(.*)','bigramassociation',
    '/trigramassociation/(.*)','trigramassociation',
    '/clustering/nmf/(.*)','clusteringservice'
    
)
app = web.application(urls, globals())


class unigramassociation:
    luceneDir = './data/nsf/index'
    def GET(self, searchString):
        #lucene.initVM()
        vm_env.attachCurrentThread()        
        if not searchString: 
            searchString = 'awards'

        context =searchContext()
        context.luceneDir = self.luceneDir
        context.searchString = searchString
        context.searchField = "contents"

        searchobj = search()
        ramindex = RAMIndex()
        unigramobj = unigrams()
        weightobj = OddsRatio()
        tfidfobj = tfidf()
        assoobj = wordAssociation()
        
        chainobj = Chain(searchobj,ramindex,unigramobj,weightobj,tfidfobj,assoobj)
        chainobj.execute(context)

        returnList = {}
        returnList = context.gramassociation
        
        return json.dumps(returnList)

class bigramassociation:
    luceneDir = './data/nsf/index'
    def GET(self, searchString):
        #lucene.initVM()
        vm_env.attachCurrentThread()        
        if not searchString: 
            searchString = 'awards'
            
        context =searchContext()
        context.luceneDir = self.luceneDir
        context.searchString = searchString
        context.searchField = "contents"

        searchobj = search()
        ramindex = RAMIndex()
        bigramobj = bigrams()
        weightobj = OddsRatio()
        tfidfobj = tfidf()
        assoobj = wordAssociation()
    
        
        chainobj = Chain(searchobj,ramindex,bigramobj,weightobj,tfidfobj,assoobj)
        chainobj.execute(context)
            
        returnList = {}
        returnList = context.gramassociation
        
        return json.dumps(returnList)

class trigramassociation:
    luceneDir = './data/nsf/index'
    def GET(self, searchString):
        #lucene.initVM()
        vm_env.attachCurrentThread()        
        if not searchString: 
            searchString = 'awards'
            
        context =searchContext()
        context.luceneDir = self.luceneDir
        context.searchString = searchString
        context.searchField = "contents"

        searchobj = search()
        ramindex = RAMIndex()
        trigramobj = trigrams()
        weightobj = OddsRatio()
        tfidfobj = tfidf()
        assoobj = wordAssociation()
    
        
        chainobj = Chain(searchobj,ramindex,trigramobj,weightobj,tfidfobj,assoobj)
        chainobj.execute(context)
            
        returnList = {}
        returnList = context.gramassociation
        
        return json.dumps(returnList)



class unigramservice:
    luceneDir = './data/nsf/index'
    def GET(self, searchString):
        #lucene.initVM()
        vm_env.attachCurrentThread()        
        if not searchString: 
            searchString = 'awards'
            
        context =searchContext()
        context.luceneDir = self.luceneDir
        context.searchString = searchString
        context.searchField = "contents"

        searchobj = search()
        ramindex = RAMIndex()
        unigramobj = unigrams()
        weightobj = OddsRatio()
    
        
        chainobj = Chain(searchobj,ramindex,unigramobj,weightobj)
        chainobj.execute(context)
            
        returnList = []
        returnList = context.termList
        
        return json.dumps(returnList)


class bigramservice:
    luceneDir = './data/nsf/index'
    def GET(self, searchString):
        #lucene.initVM()
        vm_env.attachCurrentThread()        
        if not searchString: 
            searchString = 'awards'
            
        context =searchContext()
        context.luceneDir = self.luceneDir
        context.searchString = searchString
        context.searchField = "contents"

        searchobj = search()
        ramindex = RAMIndex()
        bigramobj = bigrams()
        weightobj = OddsRatio()
    
        
        chainobj = Chain(searchobj,ramindex,bigramobj,weightobj)
        chainobj.execute(context)
            
        returnList = []
        returnList = context.termList
        
        return json.dumps(returnList)

class trigramservice:
    luceneDir = './data/nsf/index'
    def GET(self, searchString):
        #lucene.initVM()
        vm_env.attachCurrentThread()        
        if not searchString: 
            searchString = 'awards'
            
        context =searchContext()
        context.luceneDir = self.luceneDir
        context.searchString = searchString
        context.searchField = "contents"

        searchobj = search()
        ramindex = RAMIndex()
        trigramobj = trigrams()
        weightobj = OddsRatio()
    
        
        chainobj = Chain(searchobj,ramindex,trigramobj,weightobj)
        chainobj.execute(context)
            
        returnList = []
        returnList = context.termList
        
        return json.dumps(returnList)


    

class clusteringservice:
    luceneDir = './data/nsf/index'
    def GET(self, searchString):
        #lucene.initVM()
        vm_env.attachCurrentThread()        
        if not searchString: 
            searchString = 'awards'
            
        context =searchContext()
        context.luceneDir = self.luceneDir
        context.searchString = '"' + searchString + '"'
        context.searchField = "contents"

        searchobj = search()
        ramindex = RAMIndex()
        unigramobj = unigrams()
        weightobj = OddsRatio()
        tfidfobj = tfidf()
        nmfobj = nmf()
        assoobj = wordAssociation()
    
        
        chainobj = Chain(searchobj,ramindex,unigramobj,weightobj,tfidfobj,assoobj,nmfobj)
        chainobj.execute(context)
        clusters = context.clusters
        
        return json.dumps(clusters)

    

class searchservice:
    luceneDir = './data/nsf/index'
    def GET(self, searchString):
        #lucene.initVM()
        vm_env.attachCurrentThread()        
        if not searchString: 
            searchString = 'awards'
            
        context =searchContext()
        context.luceneDir = self.luceneDir
        #context.searchString = '"' + searchString + '"'
        context.searchString = searchString
            
        context.searchField = "contents"

        searchobj = search()
    
        
        chainobj = Chain(searchobj)
        chainobj.execute(context)
            
        returnList = []
        returnList = context.searchResults
        
        return json.dumps(returnList)
                                                

if __name__ == "__main__":
    app.run()