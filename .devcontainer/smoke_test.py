"""Check that ModelFlow imports and can build a tiny model inside the Codespace."""
import shutil
import sys

import modelclass
from modelclass import model

print('python     ', sys.version.split()[0])
print('modelclass ', modelclass.__file__)
print('graphviz   ', shutil.which('dot') or 'NOT FOUND')

m = model('FRML <> Y = C + I $ FRML <> C = 0.8*Y $')
print('model built, endogenous:', sorted(m.endogene))
