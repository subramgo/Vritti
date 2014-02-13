# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 20:15:02 2011

@author: gopi
"""

class searchResult(object):
	def __init__(self,docScore,docId,docContent):
		self.docScore = docScore
		self.docId = docId
		self.docContent = docContent
		