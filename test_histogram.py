import pandas as pd
from teslaseries.visualization.histogram import histogram

# Test with a list
data_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
histogram(data_list)

# Test with a DataFrame
df = pd.DataFrame({"values": data_list})
histogram(df, column="values")
###########################################

import pandas as pd
from teslaseries.visualization.histogram import histogram

# Test with a list
data_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
histogram(data_list, bins=5)  # Label will show it as "List Data"

# Test with a DataFrame
df = pd.DataFrame({"values": data_list})
histogram(df, column="values", bins=5)  # Label will show it as "DataFrame Data"
