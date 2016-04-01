'''
Created on 2016/4/1

Author: by wang_yang1980@hotmail.com
'''
import os
from ScapyLibrary.utils.baseclass import _BaseClass
from ScapyLibrary.utils._scapy import scapylib

class PcapFile(_BaseClass):

    def read_pcap_file(self, pcapFile, count=-1):
        '''This keyword is used to read pcap file through "rdpcap"

        @pcapFile: path of pcap file
        @count: read only <count> packets
        @return: packet list, instance of PacketList
        '''
        count = int(count)
        packetList = scapylib.rdpcap(pcapFile, count)
        print '*DEBUG* Read %s' % packetList.__repr__()
        return packetList

    def save_to_pcap_file(self, pcapFile, packetList, *args, **kargs):
        '''This keyword is used to save packets to pcap file through "wrpcap"

        @pcapFile: path of pcap file
        @count: read only <count> packets
        @return: packet list, instance of PacketList
        '''
        pcapFile = os.path.abspath(pcapFile)
        scapylib.wrpcap(pcapFile, packetList, *args, **kargs)
        print '*DEBUG* Save to %s' % pcapFile