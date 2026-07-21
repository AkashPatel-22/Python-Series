#  Pandas with csv Files.

import pandas as pd

data = pd.read_csv("Global_air_quality.csv")
print(data)


#  Pandas with json Files.

import pandas as pd

j_data = pd.read_csv("data.json")
print(j_data)