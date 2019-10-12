
import cms50dplus as cms

port = '/dev/ttyUSB0'
cms_init = cms.cms_serial(port, False)

while True:
    a = cms.getNreadings(100,cms_init) # this function doesn't exist...
    print(a)
