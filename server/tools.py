#!/usr/libexec/platform-python

import os

print ("Current euid = %d" % os.geteuid())

os.seteuid(48)

print ("iupdated  euid = %d" % os.geteuid())

os.system('klist')
os.system('kinit  custom/sampleapp.apps.demo.redhatfsi.com@REDHATFSI.COM')

