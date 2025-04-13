import sys

import util

from util import Util,pt

print(sys.path)

#util=Util()
#util.print_message("u1")
util.pt()

u= util.Util()
u.print_message("hey")

u2=Util()
u2.print_message("hey2")

pt()

print(util.__name__)
print(__name__)
