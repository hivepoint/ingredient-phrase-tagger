#!/usr/bin/env python
from __future__ import print_function

import sys
import json

from ingredient_phrase_tagger import kdutils

# if len(sys.argv) < 2:
#     sys.stderr.write("Usage: make-data.py FILENAME")
#     sys.exit(1)

# print(json.dumps(utils.import_data(open(sys.argv[1])), indent=4))
print(json.dumps(kdutils.import_data(sys.stdin.readlines()), indent=4))