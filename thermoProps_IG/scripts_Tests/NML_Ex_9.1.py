import math
from math import pi
import sys
sys.path.insert(1,'../functions')
from monatomic_Z_tr import monatomic_Z_tr

m_AMU = 4.0026 # [amu]
m = m_AMU * (1.6605*10**(-27))

T = 300 #[K]

V = 1 #[m3]

Z_tr = monatomic_Z_tr(m,T,V)

print( Z_tr)
