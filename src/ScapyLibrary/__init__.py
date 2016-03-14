'''
Created on 2016/2/23

Author: by wang_yang1980@hotmail.com
'''

from ScapyLibrary.keywords.layers import LayersWrapper
from ScapyLibrary.keywords.sendrecv import L3SendRecv
from .version import __version__

class ScapyLibrary(L3SendRecv, LayersWrapper):

    ROBOT_LIBRARY_VERSION = __version__
    ROBOT_LIBRARY_SCOPE = 'global'

    def get_keyword_names(self):
        keywords = []
        for _base in ScapyLibrary.__bases__:
            keywords.extend(_base.get_keyword_names(self))
        return keywords


if __name__ == '__main__':
    s = ScapyLibrary()
    print s.get_keyword_names()
