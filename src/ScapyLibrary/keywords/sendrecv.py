'''
Created on 2016/3/14

Author: by wang_yang1980@hotmail.com
'''

from ScapyLibrary.utils.baseclass import _BaseClass
from ScapyLibrary.utils._scapy import scapylib

class L3SendRecv(_BaseClass):

    def send_and_receive_at_layer3(self, packet, return_answer=True,
                                    return_unanswer=False, return_send=False, *args, **kwargs):
        an, unan = scapylib.sr(packet, *args, **kwargs)
        answered = scapylib.plist.PacketList(name='Answered')
        returnAnswer = True
        if return_answer and return_send:
            answered = an
        elif (not return_answer) and return_send:
            for _an in an:
                answered.append(_an[0])
        elif return_answer and (not return_send):
            for _an in an:
                answered.append(_an[1])
        else:
            returnAnswer = False

        if returnAnswer and return_unanswer:
            return answered, unan
        elif returnAnswer and (not return_unanswer):
            return answered
        elif (not returnAnswer) and return_unanswer:
            return unan



