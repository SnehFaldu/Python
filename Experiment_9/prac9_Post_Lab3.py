import pandas as pd
import numpy as np

list_data = [10, 20, 30, 40]
s_list = pd.Series(list_data)
print("Series from List:\n", s_list)

array_data = np.array([100, 200, 300, 400])
s_array = pd.Series(array_data)
print("\nSeries from NumPy Array:\n", s_array)

dict_data = {"x": 1, "y": 2, "z": 3}
s_dict = pd.Series(dict_data)
print("\nSeries from Dictionary:\n", s_dict)