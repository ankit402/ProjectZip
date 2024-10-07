import  numpy as np
#
# a= np.array([1,2,3])
# print(type(a))
# #
# print(a.shape)
#
# b = np.arange(12).reshape(4,3)
# print(b)


#second library
# from scipy import constants
#
# print(constants.c)

import pandas as pd

df = pd.DataFrame(np.random.randn(5,4), index=list(range(5)), columns=list('ABCD'))
#df = pd.DataFrame(np.random.randn(5, 4), index=list(range(5)), columns=list('ABCD'))
print(df)

print(df.describe())