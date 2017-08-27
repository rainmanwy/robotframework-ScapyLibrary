'''
Created on 2016/2/23

Author: by wang_yang1980@hotmail.com
'''

import types
from ScapyLibrary.utils._scapy import scapylib

class LayersWrapper(object):

    OTHER_KEYWORDS = ['log_packets', 'compose_packet']

    def __init__(self):
        self.layers = {}
        self._init_layers()

    def __getattr__(self, name):

        def _f(self, **kwargs):
            newKwargs = {}
            for key in kwargs:
                if isinstance(kwargs[key], basestring):
                    newKwargs[key] = str(kwargs[key])
                else:
                    newKwargs[key] = kwargs[key]
            p = self.layers[name](**newKwargs)
            return p
        try:
            if name in self.layers:
                _f.__name__ = name
                _f.__doc__ = self.layers[name].__doc__
                newMethod = types.MethodType( _f, self)
                return newMethod
            else:
                raise KeyError('Could not find %s' % name)
        except KeyError:
            return super(LayersWrapper, self).__getattr__(name)

    def compose_packet(self, *layers):
        '''Create packet with layers

        Example:
        |   ${eth}     |   Ether            |
        |   ${ip}      |   IP               |  dst=10.1.1.1  |
        |   ${packet}  |   Compose Packet   |  ${eth}        |  ${ip}  |
        '''
        newPacket = None
        index = 0
        for layer in layers:
            if index == 0:
                newPacket = layer
            else:
                newPacket = newPacket/layer
            index += 1
        return newPacket

    def log_packets(self, *packets):
        '''Show packets content with nice format

        It is a wrapper of scap packet "show" method
        Example:
        |   ${ip}            |   IP            |  dst=10.1.1.1  |
        |   Log Packets      |   ${ip}         |
        '''
        index = 0
        for packet in packets:
            index += 1
            print '****** Content of packet %s********' % str(index)
            packet.show()

    def get_keyword_names(self):
        return self.layers.keys() + LayersWrapper.OTHER_KEYWORDS

    def _init_layers(self):
        for protocol in scapylib.conf.layers:
            protocolName = protocol.__name__
            if protocol._name is None:
                doc = ''
            else:
                doc = protocol._name + '\n\n'
            for field in protocol.fields_desc:
                if hasattr(field, 'default'):
                    try:
                        doc += '@%s:    %s. Default value is %s\n\n' % (field.name,
                                                                    field.__class__.__name__,
                                                                    str(field.default))
                    except Exception, err:
                        print '*WARN* temp solution'
                else:
                    doc += '@%s:    %s\n\n' % (field.name, field.__class__.__name__)
            protocol.__doc__ = doc
            self.layers[protocolName] = protocol


if __name__ == '__main__':
    l = LayersWrapper()
    l.ARP().show()
