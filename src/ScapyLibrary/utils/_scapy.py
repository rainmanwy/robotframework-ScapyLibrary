'''
Created on 2016/2/24

Author: by wang_yang1980@hotmail.com
'''
import logging
import sys
import os
import glob
STDOUT = sys.stdout
logging.getLogger("scapy.loading").setLevel(logging.ERROR)

def _get_contrib():
    import scapy
    mods = []
    name="*.py"
    name = os.path.join(os.path.dirname(scapy.__file__), "contrib", name)
    for f in glob.glob(name):
        mod = os.path.basename(f)
        if mod.startswith("__"):
            continue
        if mod.endswith(".py"):
            mod = mod[:-3]
            mods.append(mod)
    return mods

try:
    from scapy import all as scapylib
    mods = _get_contrib()
    for mod in mods:
        scapylib.load_contrib(mod)

except ImportError, err:
    print '*WARN*  import scapy failed, please check whether scapy is installed'
    raise err
finally:
    sys.stdout = STDOUT
