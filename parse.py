#!/usr/bin/env python
from __future__ import print_function

import sys
import os
import tempfile

from ingredient_phrase_tagger import kdutils

tmpfd, tmppath = tempfile.mkstemp()
with open(tmppath, 'w') as tmpFile:
  tmpFile.write(kdutils.export_data(sys.stdin.readlines()))

os.close(tmpfd)

modelFilename = os.path.join(os.path.dirname(__file__), "ingr-model2.crfmodel")
convertScript = os.path.join(os.path.dirname(__file__), "convert-to-json.py")
os.system("crf_test -v 1 -m %s %s | %s" % (modelFilename, tmppath, convertScript))
os.system("rm %s" % tmppath)
