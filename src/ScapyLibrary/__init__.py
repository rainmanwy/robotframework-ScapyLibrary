'''
Created on 2016/2/23

Author: by wang_yang1980@hotmail.com
'''

from ScapyLibrary.keywords.layers import LayersWrapper
from .version import __version__

class ScapyLibrary(LayersWrapper):

    ROBOT_LIBRARY_VERSION = __version__
    ROBOT_LIBRARY_SCOPE = 'global'

    def get_keyword_names(self):
        return super(ScapyLibrary, self).get_keyword_names()


if __name__ == '__main__':
    s = ScapyLibrary()
    print s.get_keyword_names()
