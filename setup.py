'''
Created on 2015/12/10

Author: by wang_yang1980@hotmail.com
'''

from setuptools import setup, find_packages

from os.path import abspath, dirname, join
execfile(join(dirname(abspath(__file__)), 'src', 'ScapyLibrary', 'version.py'))


DESCRIPTION = """
Scapy Robot Framework Library provide keywords for Robot Framework to send, sniff and dissect and forge network packets through scapy.
"""[1:-1]
CLASSIFIERS = """
Operating System :: OS Independent
Programming Language :: Python
Topic :: Software Development :: Testing
"""[1:-1]



setup(name         = 'robotframework-ScapyLibrary',
      version      = __version__,
      description  = 'Scapy library for Robot Framework',
      long_description = DESCRIPTION,
      author       = 'Wang Yang',
      author_email = 'wang_yang1980@hotmail.com',
      url          = 'https://github.com/rainmanwy/robotframework-ScapyLibrary',
      license      = 'Apache License 2.0',
      keywords     = 'robotframework testing testautomation scapy network protocol',
      platforms    = 'any',
      classifiers  = CLASSIFIERS.splitlines(),
      package_dir  = {'' : 'src'},
      packages     = find_packages('src'),
      install_requires = [
							'scapy>=2.3.2',
						 ],
      )
