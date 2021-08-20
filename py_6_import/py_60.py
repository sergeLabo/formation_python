# # py_60.py

### Import intro

import time

print("time:", time, "\n")
print("dir(time):", dir(time), "\n")

# Le détail se trouve dans la doc
# https://docs.python.org/3/library/time.html

from time import time, sleep

print("il est", time())

sleep(1)

# #print(dir())
# #print("\n"*5)
# #import sys
# #for dossier in sys.path:
    # #print(dossier)
