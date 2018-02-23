#!/usr/bin/env python3

import os, sys
# os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
with open('process/test.zht', 'r') as f, open('process/test.zht-hpy.zht.sgm', 'w') as w:
	w.write('<srcset setid="zhwsrc" srclang="any">\n<doc docid="zhwsrc" genre="story" origlang="zht">\n<p>\n')
	for i, ln in enumerate(f, 1):
		w.write('<seg id="%d">%s</seg>\n' % (i,ln.strip()))
	w.write('</p>\n</doc>\n</srcset>\n')

with open('process/test.hpy', 'r') as f, open('process/test.zht-hpy.hpy.sgm', 'w') as w:
	w.write('<refset trglang="hpy" setid="zhwsrc" srclang="any">\n<doc sysid="ref" docid="zhwsrc" genre="story" origlang="zht">\n<p>\n')
	for i, ln in enumerate(f, 1):
		w.write('<seg id="%d">%s</seg>\n' % (i,ln.strip()))
	w.write('</p>\n</doc>\n</refset>\n')

with open('process/test.hpy', 'r') as f, open('process/test.hpy-zht.hpy.sgm', 'w') as w:
	w.write('<srcset setid="zhwsrc" srclang="any">\n<doc docid="zhwsrc" genre="story" origlang="hpy">\n<p>\n')
	for i, ln in enumerate(f, 1):
		w.write('<seg id="%d">%s</seg>\n' % (i,ln.strip()))
	w.write('</p>\n</doc>\n</srcset>\n')

with open('process/test.zht', 'r') as f, open('process/test.hpy-zht.zht.sgm', 'w') as w:
	w.write('<refset trglang="zht" setid="zhwsrc" srclang="any">\n<doc sysid="ref" docid="zhwsrc" genre="story" origlang="hpy">\n<p>\n')
	for i, ln in enumerate(f, 1):
		w.write('<seg id="%d">%s</seg>\n' % (i,ln.strip()))
	w.write('</p>\n</doc>\n</refset>\n')
