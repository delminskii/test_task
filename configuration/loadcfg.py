#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys
from os import path

config_filename = './config.json'

if not path.exists(config_filename):
    print 'Check %s for existance.' % config_filename
    sys.exit(1)

CFG = None
with open(config_filename, 'r') as fp:
    CFG = json.loads(fp.read())
if CFG is None:
    print 'It seems like config is empty.'
    sys.exit(1)
