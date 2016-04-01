'''
Created on 2016/3/14

Author: by wang_yang1980@hotmail.com
'''

from ScapyLibrary.utils.baseclass import _BaseClass
from ScapyLibrary.utils._scapy import scapylib

class SendRecv(_BaseClass):

    def send_and_receive_at_layer3(self, packet, return_answer=True,
                                    return_unanswer=False, return_send=False, *args, **kwargs):
        '''This keyword support send layer 3 packets and receive the answers, it use "sr" function in scapy

        @packet: Layer 3 packets created by scapy
        @return_answer: boolean, whether return answered packets
        @return_unanswer: boolean, whether return unanswered packets
        @return_send: boolean, whether return sended packets which are answered
        @args: please check doc of "sr" function in scapy to get detail
        @kwargs: please check doc of "sr" function in scapy to get detail
        @return: return sended packets/answered packets/unanswered packets,

        By default, only answered packets are return

        | ${answered} | Send And Receive At Layer3 | ${packets} | timeout=${10} |
        | Log Packets | ${answered[0]} |

        | ${answered} | Send And Receive At Layer3 | ${packets} | timeout=${10} | return_send=${True} |
        | Log Packets | ${answered[0][0]} |
        | Log Packets | ${answered[0][1]} |

        | ${answered} | ${unanswered} | Send And Receive At Layer3 | ${packets} | timeout=${10} | return_send=${True} | return_answer=${True} |
        | Log Packets | ${answered[0][0]} |
        | Log Packets | ${answered[0][1]} |
        | Log Packets | ${unanswered[0]} |

        '''
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

    def send_and_receive_at_layer2(self, packet, return_answer=True,
                                    return_unanswer=False, return_send=False, *args, **kwargs):
        '''This keyword support send layer 2 packets and receive the answers, it use "srp" function in scapy

        @packet: Layer 2 packets created by scapy
        @return_answer: boolean, whether return answered packets
        @return_unanswer: boolean, whether return unanswered packets
        @return_send: boolean, whether return sended packets which are answered
        @args: please check doc of "sr" function in scapy to get detail
        @kwargs: please check doc of "sr" function in scapy to get detail
        @return: return sended packets/answered packets/unanswered packets,

        By default, only answered packets are return

        | ${answered} | Send And Receive At Layer2 | ${packets} | timeout=${10} |
        | Log Packets | ${answered[0]} |

        | ${answered} | Send And Receive At Layer2 | ${packets} | timeout=${10} | return_send=${True} |
        | Log Packets | ${answered[0][0]} |
        | Log Packets | ${answered[0][1]} |

        | ${answered} | ${unanswered} | Send And Receive At Layer2 | ${packets} | timeout=${10} | return_send=${True} | return_answer=${True} |
        | Log Packets | ${answered[0][0]} |
        | Log Packets | ${answered[0][1]} |
        | Log Packets | ${unanswered[0]} |

        '''
        an, unan = scapylib.srp(packet, *args, **kwargs)
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


