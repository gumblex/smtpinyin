#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import random

file_in_ts_s = 'process/test-orig.hpy'
file_in_ts_t = 'process/test-orig.zht'
file_out_ts_s = 'process/test.hpy'
file_out_ts_t = 'process/test.zht'

with open(file_in_ts_s, 'r') as fins, open(file_in_ts_t, 'r') as fint:
    test_s = fins.readlines()
    test_t = fint.readlines()

samp = random.sample(range(len(test_s)), 3000)

with open(file_out_ts_s, 'w') as fouts, open(file_out_ts_t, 'w') as foutt:
    for k in samp:
        fouts.write(test_s[k])
        foutt.write(test_t[k])
