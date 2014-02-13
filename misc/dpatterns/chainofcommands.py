# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 11:44:12 2011

@author: gopi
"""
import lucene

class Command(object):
    '''
    Command Base Class
    '''

    def __init__(self):
        '''
        Constructor
        '''
        
    def process(self, context):
        '''
        Method to be implemented by
        all the sub class derived from command
        '''
 
class LuceneCommand(Command):
	def __init__(self):
		super (LuceneCommand,self).__init__()
		lucene.initVM()
                   
class Chain(object):
    '''
    Chain Base Class
    '''
    
    def __init__(self,*args):
        self.commands = args
        
        
    def execute(self, context):
        for command in self.commands:
            command.process(context)
            context = command.context
            										
												


    
