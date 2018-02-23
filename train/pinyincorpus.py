#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import sys
import collections

os.environ['PYPINYIN_NO_DICT_COPY'] = '1'

import pypinyin
import terra_pinyin

pypinyin.load_single_dict(terra_pinyin.pinyin_dict)
pypinyin.load_phrases_dict(terra_pinyin.phrases_dict)

RE_UCJK = re.compile(
    '([\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff'
    '\U00020000-\U0002A6DF\U0002A700-\U0002B73F'
    '\U0002B740-\U0002B81F\U0002B820-\U0002CEAF'
    '\U0002F800-\U0002FA1F]+)'
)

with open(sys.argv[1], 'w', encoding='utf-8') as w1, \
    open(sys.argv[2], 'w', encoding='utf-8') as w2, \
    open(sys.argv[3], 'w', encoding='utf-8') as w3:
    for ln in sys.stdin.buffer:
        for seg in RE_UCJK.findall(ln.decode('utf-8', 'ignore')):
            pinyins = pypinyin.pinyin(
                seg, style=pypinyin.Style.NORMAL, errors='ignore')
            length = len(seg)
            if length != len(pinyins):
                continue
            py = ' '.join(x[0] for x in pinyins)
            align = ' '.join('%d-%d' % (x, x) for x in range(length))
            w1.write(py + '\n')
            w2.write(' '.join(seg) + '\n')
            w3.write(align + '\n')
