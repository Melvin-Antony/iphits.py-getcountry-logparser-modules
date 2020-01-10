#!/usr/bin/python3

import logparser
import os
import sys
import getcountry

ipstkey='xxx ADD YOUR KEY xxx'

USAGE = "python3 ipcounter.py /path/to/access.log  minimum_count"
if len(sys.argv) != 3:
  print(USAGE)
else:
  log = sys.argv[1]
  mcount = sys.argv[2]

  if not os.path.isfile(log):
    print('Not a valid file {}.'.format(log))
    sys.exit(1)

  if not mcount.isdigit():
    print('Not a valid digit {}'.format(mcount))
    sys.exit(1)

  ipCounter = {}
  fh = open(log)
  for logLine in fh:
    logFields = logparser.parser(logLine)
    clientIp = logFields['host']

    if clientIp not in ipCounter:
      ipCounter[clientIp] = 1
    else:
      ipCounter[clientIp] = ipCounter[clientIp] + 1

  print('{:16}{:14}: {}'.format('   IP', 'Country','Hits'))
  print('#' * 40)
  
  for ip in ipCounter:
    hit = ipCounter[ip]
    if hit >= int(mcount):
      country = getcountry.country(ip,key=ipstkey)
      print('{:16}{:14}: {}'.format(ip,country,hit))
