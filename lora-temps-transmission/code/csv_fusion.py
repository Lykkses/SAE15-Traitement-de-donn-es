# importing libraries
import pandas as pd
import glob
import os



joined_files = os.path.join('U:\Documents\exel_python', "sending*.csv")

joined_list = glob.glob(joined_files)

df = pd.concat(map(pd.read_csv, joined_list), ignore_index=True)
print(df)
export_csv = df.to_csv ('Donnee.csv', index=None, header=True, encoding='utf-8', sep='\n')