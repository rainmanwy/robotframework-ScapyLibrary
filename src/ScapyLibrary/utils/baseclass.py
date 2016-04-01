'''
Created on 2016/3/14

Author: by wang_yang1980@hotmail.com
'''
import types

class _BaseClass(object):

    def get_keyword_names(self):
        keywords = []
        for attr in dir(self):
            if not attr.startswith('_') and attr != 'get_keyword_names' and \
                    type(getattr(self, attr)) == types.MethodType:
                keywords.append(attr)
        return keywords

