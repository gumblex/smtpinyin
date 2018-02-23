#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

for ln in sys.stdin.buffer:
    sys.stdout.write(ln.decode('utf-8', errors='ignore'))
