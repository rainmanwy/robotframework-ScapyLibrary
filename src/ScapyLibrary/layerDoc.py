'''
Created on 2016/3/14

Author: by wang_yang1980@hotmail.com
'''

SCAPY_PROTOCOL_TEMPLATE = """
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<html>
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <style type="text/css">
html {
  font-family: Arial,Arial,sans-serif;
  background-color: white;
  color: black;
  font-size: 10pt
  font-style: italic
}
table {
  border-collapse: collapse;
  empty-cells: show;
  margin: 1em 0em;
  border: 0.1em solid black;
}
th, td {
  border-style: solid;
  border-width: 0.1em 0.15em;
  border-color: black;
  padding: 0.1em 0.2em;
  height: 1.5em;
  font-size: 11pt
}
th {
  background-color: rgb(192, 192, 192);
  color: black;
  border-width: 0.15em;
  font-weight: bold;
  text-align: center;
  letter-spacing: 0.1em;
  font-style: italic
}
td.protocol {
  background-color: rgb(1, 254, 147);
  font-weight: bold;
}
td.doc {
  background-color: rgb(1, 254, 147);
}
td.field {
    font-style: italic;
}
td.name, th.name {
    text-align: center;
    font-style: italic;
}
    </style>
    <title>scapy protocol help</title>
    </head>
    <body>
        <h1>Scapy Protocol Help</h1>
        <table id="protocol table" border="1">
            <tr>
                <th class="name">Protocol</th>
                <th class="name">Fields</th>
            </tr>

            ${protocol_doc}

    </body>
</html>
"""

PROTOCOL_TEMPLATE = """
            <tr>
                <td class="protocol">%s</td>
                <td class="doc">%s</td>
            </tr>
"""

FIELD_TEMPLATE = """
            <tr>
                <td>%s</td>
                <td class="field">%s</td>
            </tr>
"""

import os
import re
from ScapyLibrary.utils._scapy import scapylib

def generate_scapy_layer_doc(docFile):
    protocolDoc = ''
    for protocol in scapylib.conf.layers:
        protocolDoc += PROTOCOL_TEMPLATE % (protocol.__name__, protocol.name)
        for f in protocol.fields_desc:
            if hasattr(f, 'default'):
                protocolDoc += FIELD_TEMPLATE % ('', '<b>%s</b>:&nbsp;&nbsp;&nbsp;&nbsp;Default value is %s' % (f.name, str(f.default)))
            else:
                protocolDoc += FIELD_TEMPLATE % ('', f.name)

    protocolDoc = re.sub('\$\{(.*?)\}', lambda x: "%s" % protocolDoc, SCAPY_PROTOCOL_TEMPLATE)

    with open(docFile, 'w+') as f:
        f.write(protocolDoc)
    print "Generate layer doc to %s" % os.path.abspath(docFile)

if __name__ == '__main__':
    import sys
    helpDoc = '''usage: python -m ScapyLibrary.layerDoc <scapy_layer_doc >

    Example: python -m ScapyLibrary.layerDoc scapy.html
    '''
    if len(sys.argv)==1 or len(sys.argv)>1 and (sys.argv[1].lower() in ['help', '-h', '--help']):
        print helpDoc
    else:
        generate_scapy_layer_doc(sys.argv[1])


