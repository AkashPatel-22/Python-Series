# Creating DataFrame using Numpy array.
import numpy as np
np_arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
df = pd.DataFrame(np_arr, columns = ["col1","col2","col3"])
print(df)