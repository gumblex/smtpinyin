#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import sys
import collections

TONES = {
'a1': 'ā',
'a2': 'á',
'a3': 'ǎ',
'a4': 'à',
'e1': 'ē',
'e2': 'é',
'e3': 'ě',
'e4': 'è',
'o1': 'ō',
'o2': 'ó',
'o3': 'ǒ',
'o4': 'ò',
'i1': 'ī',
'i2': 'í',
'i3': 'ǐ',
'i4': 'ì',
'u1': 'ū',
'u2': 'ú',
'u3': 'ǔ',
'u4': 'ù',
'v1': 'ǖ',
'v2': 'ǘ',
'v3': 'ǚ',
'v4': 'ǜ'
}

re_style_conv1 = re.compile('([aeiou])(ng?|r)([1234])')
re_style_conv2 = re.compile('([aeo])([iuo])([1234])')
re_style_conv3 = re.compile('([nljqxy])v')
re_style_conv4 = re.compile('eh[0-5]?')
re_style_conv5 = re.compile('([a-z]+)[0-5]')

#- xform ([aeiou])(ng?|r)([1234]) $1$3$2
#- xform ([aeo])([iuo])([1234]) $1$3$2

#- xform/([nljqxy])v/$1ü/
#- xform/eh[0-5]?/ê/
#- xform/([a-z]+)[0-5]/$1/

def style_convert(pinyin):
    s = re_style_conv1.sub(r'\1\3\2', pinyin)
    s = re_style_conv2.sub(r'\1\3\2', s)
    for k, v in TONES.items():
        s = s.replace(k, v)
    s = re_style_conv3.sub(r'\1ü', s)
    s = re_style_conv4.sub('ê', s)
    s = re_style_conv5.sub(r'\1', s)
    return s

def load_pinyin_dict(fp):
    started = False
    single_dict = collections.defaultdict(list)
    phrase_dict = {}
    for ln in fp:
        ln = ln.strip()
        if started and ln and ln[0] != '#':
            l = ln.split(maxsplit=1)
            w, c = l[0], l[1].split('\t')[0].split(' ')
            if len(w) == 1:
                single_dict[ord(w)].append(style_convert(c[0]))
            else:
                phrase_dict[w] = tuple(map(style_convert, c))
        elif ln == '...':
            started = True
    single_dict2 = {}
    for k, v in single_dict.items():
        single_dict2[k] = ','.join(v)
    del single_dict
    return single_dict2, phrase_dict

def write_pinyin_dict(single_dict, phrase_dict, fp):
    fp.write('# -*- coding: utf-8 -*-\n\npinyin_dict = {\n')
    for k in sorted(single_dict.keys()):
        fp.write("0x%04x: '%s',\n" % (k, single_dict[k]))
    fp.write('}\n\nphrases_dict = {\n')
    for k in sorted(phrase_dict.keys()):
        fp.write("'%s': [%s],\n" %
            (k, ', '.join("['%s']" % s for s in phrase_dict[k])))
    fp.write('}\n')

if __name__ == '__main__':
    single_dict, phrase_dict = load_pinyin_dict(sys.stdin)
    write_pinyin_dict(single_dict, phrase_dict, sys.stdout)
