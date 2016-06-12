'''
Created on 2016/6/12

Author: by wang_yang1980@hotmail.com
'''

import types
from ScapyLibrary.utils._scapy import scapylib

class ScapyFunctionWrapper(object):

    def __init__(self):
        self.keywords = {}
        self._get_scapy_functions()

    def _get_scapy_functions(self):
        for attr in dir(scapylib):
            if type(getattr(scapylib, attr)) == types.FunctionType:
                if getattr(scapylib, attr).__doc__ != '' and getattr(scapylib, attr).__doc__ != None:
                    self.keywords[attr] = getattr(scapylib, attr)

    def __getattr__(self, item):
        if item in self.keywords.keys():
            return self.keywords[item]
        else:
            return super(ScapyFunctionWrapper, self).__getattr__(item)

    def get_keyword_names(self):
        return self.keywords.keys()

if __name__ == '__main__':
    s = ScapyFunctionWrapper()