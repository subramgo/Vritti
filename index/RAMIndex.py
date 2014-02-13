# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 20:30:26 2011

@author: gopi
"""
from lucene import Version, RAMDirectory,SimpleAnalyzer,IndexWriter, Document,Field,IndexReader, Term, IndexSearcher,SimpleFSDirectory,File
from misc.dpatterns.chainofcommands import Command

class RAMIndex(Command):
    def __init__(self):
        """
        Command object. Creates a RAM Index of the given contents.
        Usually follows the search object in the chain and creates lucene
        RAM index of the search results.
        
        RAM index is used by several other command objects, for
            1. Searching
            2. Document Frequency calculation
            3. Term Frequency calculation
        """
        self.ramIndex = None
    
    def process(self,context):
        self.createRamIndex()
        self.addContents(context.searchResults)
        context.ramIndex = self.ramIndex
        print 'Created RAM index'
        self.context = context
        
    def createRamIndex(self):
        """
        create lucene ram index of the resultsets
        """
        try:
            self.ramIndex = RAMDirectory()
            print 'Created a ram directory'
        except Exception,e:
            print 'Unable to create RAM index',e

    def addContents(self,contents):
         try:
              #iwconfig = IndexWriterConfig(SimpleAnalyzer(),IndexWriter.MaxFieldLength.LIMITED)
              writer = IndexWriter(self.ramIndex,SimpleAnalyzer(Version.LUCENE_CURRENT),True,IndexWriter.MaxFieldLength.LIMITED)
              for content in contents:
                  doc = Document()
                  doc.add(Field("contents",content[1],Field.Store.NO,Field.Index.ANALYZED,Field.TermVector.YES))
                  writer.addDocument(doc)
              writer.close()
         except Exception,e:
              print 'Unable to add content to RAM index'        