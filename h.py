








import os
import sys


def h(o,b):
    d = os.path.join(o['location'], 'bin', 'libpng12-config')
    if os.path.exists(d) and ('cygwin' in sys.platform):
        content = open(d).read()
        if not '-lpng12-0' in content :
            print "patching libpng12-config"
            content = content.replace('-lpng12', '-lpng12-0')
            content += '\n#minitagepatched\n'
            open(d, 'w').write(content)
        else:
		    print "libpng12-config already patched!"


