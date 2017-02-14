#!/bin/python

from zipfile import _ZipDecrypter
import  sys
fp = open(sys.argv[1], 'rb')
zd = _ZipDecrypter(sys.argv[2])

fp.read(12)
print ''.join(zd(c) for c in fp.read())

fp.close()
