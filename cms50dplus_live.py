
import cmsd50plus as cms

port = '/dev/tty.SLAB_USBtoUART'
cms_init = cms.cms_serial(port, False)

while True:
    a = cms.getNreadings(100,cms_init) # this function doesn't exist...
    print(a)
