#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import random

ratio = 3000 / 36821348
file_in_s = 'process/tok.hpy.txt'
file_in_t = 'process/tok.zht.txt'
file_out_tr_s = 'process/train.hpy'
file_out_tr_t = 'process/train.zht'
file_out_tr_a = 'process/aligned.txt.grow-diag-final-and'
file_out_ts_s = 'process/test-orig.hpy'
file_out_ts_t = 'process/test-orig.zht'

with open(file_in_s, 'r') as fins, open(file_in_t, 'r') as fint, \
     open(file_out_tr_a, 'w') as fouttra, \
     open(file_out_tr_s, 'w') as fouttrs, open(file_out_tr_t, 'w') as fouttrt,\
     open(file_out_ts_s, 'w') as fouttss, open(file_out_ts_t, 'w') as fouttst:
    for lns, lnt in zip(fins, fint):
        wc = len(lnt.replace(' ', '')) - 1
        if (1 < wc <= 20 and random.random() < ratio):
            fouttss.write(lns)
            fouttst.write(lnt)
        elif wc <= 50:
            fouttrs.write(lns)
            fouttrt.write(lnt)
            fouttra.write(' '.join('%d-%d' % (i, i) for i in range(wc)) + '\n')
