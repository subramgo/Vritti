# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 18:36:08 2011

@author: gopi
"""

from lucene import SimpleFSDirectory,File,StandardAnalyzer, QueryParser, IndexSearcher,Version
from misc.dpatterns.chainofcommands import Command
     

class search(Command):
	def __init__(self):
		"""
		"""
		self.MAX = 50

	def process(self,context):
		context.searchResults = self.doSearch(context.searchString,context.searchField,context.luceneDir)
		self.context = context

	def doSearch(self,searchString,fieldToSearch,luceneDir):
		searchResult =[]
		store =	SimpleFSDirectory(File(luceneDir))
		analyzer = StandardAnalyzer(Version.LUCENE_CURRENT)
		searcher = IndexSearcher(store)
		query = QueryParser(Version.LUCENE_CURRENT,fieldToSearch,analyzer).parse(searchString)
		hits = searcher.search(query,self.MAX)
		
		print "Found %d documents that matched the query '%s'" %(hits.totalHits,searchString)
		for hit in hits.scoreDocs:
			doc = searcher.doc(hit.doc)
			#docdict['score'] = hit.score
			#docdict['docid'] = hit.doc
			#docdict['content'] = doc.get("contents").encode("utf-8")
			searchResult.append([doc.get("title").encode("utf-8"),doc.get("contents").encode("utf-8")])
		searcher.close()	
		return searchResult