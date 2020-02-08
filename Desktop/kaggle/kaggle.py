import pandas as pd
import datetime

# Path of the file to read
iowa_file_path = 'train.csv'

# Fill in the line below to read the file into a variable home_data
home_data = pd.read_csv(iowa_file_path)


avg_lot_size = home_data['LotArea'].mean()

newest_home_age = datetime.datetime.now().year - home_data['YearBuilt'].max()

print(newest_home_age)

print(avg_lot_size)