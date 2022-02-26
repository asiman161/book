#%%

import pandas as pd
import os

HOUSING_PATH = os.path.join("datasets", "housing")

def load_housing_data(housing_path=HOUSING_PATH) -> pd.DataFrame:
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)

#%%

housing = load_housing_data()
housing.head()


#%%

housing.info()

#%%

housing['ocean_proximity'].value_counts()

#%%

housing.describe()

#%%

housing.hist()

