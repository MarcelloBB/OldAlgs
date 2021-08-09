# -*- coding: utf-8 -*-
"""
# // @ Marcello
"""

import pandas as pd
from numpy import NAN

df1 = pd.DataFrame({'A': [0, 0, 1, None],
                    'B': [1, 2, 3, 4],
                    'C': [NAN, 3, 4, 1]}, dtype=int)

print(df1)

print()


values = pd.Series(df1.mean(), dtype=int)
print(values)

print()

df1 = df1.fillna(values)
print(df1)

print('_'*92)
