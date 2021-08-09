# -*- coding: utf-8 -*-
"""
# // @Marcello
"""

#data duplication

import pandas as pd

print()
df = pd.DataFrame({'A': [0, 0, 0, 0, 0, 1, 0],
                   'B': [0, 2, 3, 5, 0, 2, 0],
                   'C': [0, 3, 4, 1, 0, 2, 0]})

print()
print(df, '====> Original DF')

print()


df = df.drop_duplicates()
print(df, '====> No data duplication DF')

print('_'*92)