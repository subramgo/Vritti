# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 00:46:22 2011

@author: gopi
"""
from lucene import SimpleFSDirectory,Document,File, IndexWriter,Field,SimpleAnalyzer,Version
from misc.gmail import *

class IndexEmail(object):
    """
    Creates lucene index of all the conversations
    in a given email address
    """
    def __init__(self,storDir):
        store =  SimpleFSDirectory(File(storDir))
        writer = IndexWriter(store,SimpleAnalyzer(Version.LUCENE_CURRENT),True,IndexWriter.MaxFieldLength.UNLIMITED)
        self.indexfeeds(writer)	
        writer.optimize()
        writer.close()
     
        
     
    def indexfeeds(self,writer):
         """
         """
         c = GmailClient()
         c.login('gopi@mzaya.in','cv2l7zxw')
         conversations = c.get_inbox_conversations()
         for contents in conversations:
                    try:
				doc = Document()
				doc.add(Field("name", contents,
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