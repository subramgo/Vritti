# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 17:41:21 2011

@author: gopi
"""

from lucene import SimpleFSDirectory,Document,File, IndexWriter,Field,SimpleAnalyzer,Version
import os
from ioprocess import *

class IndexFiles(object):
    """
    Given a directory, loops through all files
    and subdirectory inside and creates a lucene
    index of all the text files.
    """
    def __init__(self,root,storDir):
        store =  SimpleFSDirectory(File(storDir))
        writer = IndexWriter(store,SimpleAnalyzer(Version.LUCENE_CURRENT),True,IndexWriter.MaxFieldLength.UNLIMITED)
        self.indexDocs(root,writer)	
        writer.optimize()
        writer.close()
        
    def indexDocs(self,root,writer):
        print 'adding'
        for root,dirnames,filenames in os.walk(root):
            for filename in filenames:
                print 'adding',filename
                try:
                    path = os.path.join(root,filename)
                    file = open(path)
                    contents = unicode(file.read(),'iso-8859-1')
                    file.close()
                    doc = Document()
                    if len(contents) > 0:
                        title,abstract = ioprocess.getTitleAbstract(contents)
                        doc.add(Field("title", title,Field.Store.YES,
	                                         Field.Index.ANALYZED,Field.TermVector.YES))
                        doc.add(Field("contents",abstract,Field.Store.YES,
                                      Field.Index.ANALYZED,Field.TermVector.YES))
                        writer.addDocument(doc)
                except Exception, e:
				print 'failed in indexDocs',e
     
         
				
           
