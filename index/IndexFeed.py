# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 00:46:22 2011

@author: gopi
"""
from lucene import SimpleFSDirectory,Document,File, IndexWriter,Field,SimpleAnalyzer,Version
import feedparser

class IndexFeed(object):
    """
    Creates a lucene index of the following RSS feeds
    
    'http://today.reuters.com/rss/topNews',
    'http://today.reuters.com/rss/domesticNews',
    'http://today.reuters.com/rss/wordNews',
    'http://rss.cnn.com/rss/edition.rss',
    'http://rss.cnn.com/rss/edition_word.rss',
    'http://rss.cnn.com/rss/edition_us.rss']     
    
    """
    def __init__(self,storDir):
        store =  SimpleFSDirectory(File(storDir))
        writer = IndexWriter(store,SimpleAnalyzer(Version.LUCENE_CURRENT),True,IndexWriter.MaxFieldLength.UNLIMITED)
        self.indexfeeds(writer)	
        writer.optimize()
        writer.close()
     
    def strphtml(self,h):
        p=''
        s=0
        for c in h:
            if c == '<':
                s=1
            elif c == '>':
                s=0
                p+= ' '
            elif s == 0: p+=c
         
        return p   
        
     
    def indexfeeds(self,writer):
         """
         """
         feedlist=['http://today.reuters.com/rss/topNews',
                      'http://today.reuters.com/rss/domesticNews',
                      'http://today.reuters.com/rss/wordNews',
                      'http://rss.cnn.com/rss/edition.rss',
                      'http://rss.cnn.com/rss/edition_word.rss',
                      'http://rss.cnn.com/rss/edition_us.rss']     
         articletitles=[]
         for feed in feedlist:
                f=feedparser.parse(feed)
                for e in f.entries:
                    if e.title in articletitles: continue
                    contents = e.title.encode('utf8') + self.strphtml(e.description.encode('utf8'))
                    try:
				doc = Document()
				doc.add(Field("name", e.title,
	                                         Field.Store.YES,
	                                         Field.Index.NOT_ANALYZED))
				if len(contents) > 0:					
					doc.add(Field("contents", contents,
	                                            Field.Store.YES,
	                                            Field.Index.ANALYZED,
								    Field.TermVector.YES))
				writer.addDocument(doc)        
                    except Exception, e:
                        print 'Unable to index'