import os
import sys

CWD = os.path.dirname(__file__)
# Change working directory so relative paths (and template lookup) work again
os.chdir(CWD)

sys.path.append(CWD)
sys.path.append(CWD + '/serverside')
sys.path.append(CWD + '/searchengine')
sys.path.append(CWD + '/lib/whoosh.par')

import bottle
bottle.debug(True)
# ... build or import your bottle application here ...
# Do NOT use bottle.run() with mod_wsgi

from urldispatch import *
application = bottle.default_app()
