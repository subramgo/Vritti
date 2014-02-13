# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 17:05:40 2011

@author: gopi
"""
import re

class ioprocess(object):
    """
    Support class to parse a given text based
    on regex. Used to index NMF abstracts
    """
    @staticmethod    
    def getTitleAbstract(content):

        strippedContent = re.sub('\n',' ',content)
        strippedContent = re.sub('\t',' ',strippedContent)
        strippedContent = re.sub('\s+',' ',strippedContent)
        titleString =re.findall('Title\s+:(.+)?Type\s+:',strippedContent)
        abstractString =re.findall('Abstract\s+:(.+)?',strippedContent)

        return ''.join(titleString),''.join(abstractString)
        
    @staticmethod    
    def getContent(content):
        returnString =''
        returnString =re.findall('Abstract\s+:(.+)?',content.strip())
        print returnString
        return returnString
   
    @staticmethod
    def getDate(content):
        returnString =''
        returnString =re.findall('Date\s+:(.+)?File\s+:',content.strip())
        return returnString
        