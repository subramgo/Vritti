# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 23:52:44 2011

@author: gopi
"""
from search.Search import search
from misc.dpatterns.chainofcommands import Chain
from context.searchContext import searchContext
from ngrams.bigrams import bigrams
from ngrams.unigrams import unigrams
from ngrams.trigrams import trigrams
from association.wordAssociation import wordAssociation
from nlp.textMatrices import tfidf
from clustering.singularvalue import singularvalue
from clustering.nmf import nmf
from index.RAMIndex import RAMIndex
from ngrams.weight.OddsRatio import OddsRatio
from index.IndexFeed import IndexFeed
from index.IndexEmail import IndexEmail
from index.Index import IndexFiles
import lucene


def testtrigrams():
    lucene.initVM()
    context =searchContext()
    context.luceneDir = './data/index'
    context.searchString = "activated carbon"
    context.searchField = "contents"

    searchobj = search()
    ramindex = RAMIndex()
    trigramobj = trigrams()
    weightobj = OddsRatio()
    
        
    chainobj = Chain(searchobj,ramindex,trigramobj,weightobj)
    chainobj.execute(context)
            
    print context.termList
    print context.gramassociation


def testbigrams():
    lucene.initVM()
    context =searchContext()
    context.luceneDir = './data/index'
    context.searchString = "activated carbon"
    context.searchField = "contents"

    searchobj = search()
    ramindex = RAMIndex()
    bigramobj = bigrams()
    weightobj = OddsRatio()
    
        
    chainobj = Chain(searchobj,ramindex,bigramobj,weightobj)
    chainobj.execute(context)
            
    print context.termList
    print context.gramassociation


def testunigrams():
    lucene.initVM()
    context =searchContext()
    context.luceneDir = './data/newsgroup/index'
    context.searchString = "mac"
    context.searchField = "contents"

    searchobj = search()
    ramindex = RAMIndex()
    unigramobj = unigrams()
    weightobj = OddsRatio()
        
    chainobj = Chain(searchobj,ramindex,unigramobj,weightobj)
    chainobj.execute(context)
            
    print context.termList



def testunigramassociation():
    lucene.initVM()
    context =searchContext()
    context.luceneDir = './data/newsgroup/index'
    context.searchString = 'god'
    context.searchField = "contents"
    context.associationType ='bigram'
    searchobj = search()
    ramindex = RAMIndex()
    unigramobj = unigrams()
    weightobj = OddsRatio()
    tfidfobj = tfidf()
    assoobj = wordAssociation()
    
        
    chainobj = Chain(searchobj,ramindex,unigramobj,weightobj,tfidfobj,assoobj)
    chainobj.execute(context)
    
    for k,v in context.gramassociation.items():
        print k,v
    
def testbigramassociation():
    lucene.initVM()
    context =searchContext()
    context.luceneDir = './data/index'
    context.searchString = "glycine betaine"
    context.searchField = "contents"
    context.associationType ='bigram'
    searchobj = search()
    ramindex = RAMIndex()
    bigramobj = bigrams()
    weightobj = OddsRatio()
    tfidfobj = tfidf()
    assoobj = wordAssociation()
    
        
    chainobj = Chain(searchobj,ramindex,bigramobj,weightobj,tfidfobj,assoobj)
    chainobj.execute(context)
    
    for k,v in context.gramassociation.items():
        print k,v

def testtrigramassociation():
    lucene.initVM()
    context =searchContext()
    context.luceneDir = './data/feeds/index'
    context.searchString = "news"
    context.searchField = "contents"
    context.associationType ='bigram'
    searchobj = search()
    ramindex = RAMIndex()
    trigramobj = trigrams()
    weightobj = OddsRatio()
    tfidfobj = tfidf()
    assoobj = wordAssociation()
    
        
    chainobj = Chain(searchobj,ramindex,trigramobj,weightobj,tfidfobj,assoobj)
    chainobj.execute(context)
    
    for k,v in context.gramassociation.items():
        print k,v

def createfileindexnsf():
    lucene.initVM()
    print 'about to index'
    indexobj = IndexFiles('C:/gopi/ms/Project/Vritti/data/input/awards_2000/' ,'./data/nsf/index')

def createfileindexnewsgroup():
    lucene.initVM()
    indexobj = IndexFiles('C:/gopi/ms/Project/Vritti/data/input/mini_newsgroups/mini_newsgroups','./data/newsgroup/index')

def createemailindex():
    lucene.initVM()
    emailobj = IndexEmail('./data/email/index')

def createfeedindex():
    lucene.initVM()
    indxfeedobj = IndexFeed('./data/feeds/index')

def testclustering():
    lucene.initVM()
    context =searchContext()
    context.luceneDir = './data/index'
    context.searchString = "activated carbon"
    context.searchField = "contents"

    searchobj = search()
    ramindex = RAMIndex()
    unigramobj = unigrams()
    weightobj = OddsRatio()
    tfidfobj = tfidf()
    nmfobj = singularvalue()
    assoobj = wordAssociation()
    
        
    chainobj = Chain(searchobj,ramindex,unigramobj,weightobj,tfidfobj,assoobj,nmfobj)
    chainobj.execute(context)
    
    clusters = context.clusters
    
    for cl in clusters:
        print cl[0]
    
def main():
        
    createfileindexnsf()    
    #createemailindex()    
    #testunigrams()
    #createfeedindex()
    #testbigrams()
    #testtrigrams()
    #testbigramassociation()
    #testtrigramassociation()
    #testclustering()
    #testunigramassociation()
    


if __name__ == "__main__":
    main()
    