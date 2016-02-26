'''
Created on 2016/2/24

Author: by wang_yang1980@hotmail.com
'''
import logging
import sys
STDOUT = sys.stdout
logging.getLogger("scapy.loading").setLevel(logging.ERROR)
try:
    from scapy import all as scapylib
except ImportError, err:
    print '*WARN*  import scapy failed, please check whether scapy is installed'
    raise err
finally:
    sys.stdout = STDOUT
