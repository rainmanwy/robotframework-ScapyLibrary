'''
Created on 2016/2/23

Author: by wang_yang1980@hotmail.com
'''

from ScapyLibrary.keywords.layers import LayersWrapper
from ScapyLibrary.keywords.scapyfunctions import ScapyFunctionWrapper
from ScapyLibrary.keywords.sendrecv import SendRecv
from ScapyLibrary.keywords.pcap import PcapFile
from .version import __version__

class ScapyLibrary(SendRecv, ScapyFunctionWrapper, LayersWrapper, PcapFile):

    ROBOT_LIBRARY_VERSION = __version__
    ROBOT_LIBRARY_SCOPE = 'global'

    def __init__(self):
        for _base in ScapyLibrary.__bases__:
            _base.__init__(self)

    # def __getattr__(self, item):
    #     return super(ScapyLibrary, self).__getattr__(item)

    def get_keyword_names(self):
        keywords = []
        for _base in ScapyLibrary.__bases__:
            keywords.extend(_base.get_keyword_names(self))
        return keywords


if __name__ == '__main__':
    s = ScapyLibrary()
    print s.get_keyword_names()
