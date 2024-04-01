import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_rows",None)
pd.set_option('display.max_columns',None)
pd.set_option('display.width',500)

def load_data(file_path):
    return pd.read_csv(file_path)


def check_df(dataframe, head=5):
    print("__SHAPE__")
    print(dataframe.shape)
    print("__TYPES__")
    print(dataframe.dtypes)
    print("__HEAD__")
    print(dataframe.head())
    print("__TAIL__")
    print(dataframe.tail())
    print("__NaN__")
    print(dataframe.isnull().sum())
    print("__QUANTILES__")
    print(dataframe.describe().T)
    
    
    
    
if __name__ == "__main__":
   file_path = "projects/datasets/persona.csv"
        
       
data = load_data(file_path)

check_df(data)  

def calculate_column_unique_frequencies(df, column_name):
  
    if column_name in df.columns:
        unique_values = df[column_name].nunique()
        frequencies = df[column_name].value_counts()
        return {"unique": unique_values, "frequencies": frequencies}
   
for col in data.columns:
    result = calculate_column_unique_frequencies(data,col)
    print(result)
    
column_name = "PRICE"
column_name = "SOURCE"


    
result = calculate_column_unique_frequencies(data, column_name)


sales_by_country = data.groupby("COUNTRY").agg({"PRICE": ["sum", "count"]})

avg_prices_by_country_source = data.groupby(['COUNTRY', 'SOURCE']).agg({"PRICE": "mean"})

avg_prices_by_segment = data.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"}).reset_index() 
avg_prices_by_segment_sorted = avg_prices_by_segment.sort_values("PRICE", ascending=False) 

avg_prices_by_segment_sorted.rename(columns={"PRICE": "AVG_PRICE"}, inplace=True)

def categorize_age(age):
    if age <= 18:
        return "0_18"
    elif age <= 23:
        return "19_23"
    elif age <= 30:
        return "24_30"
    elif age <= 40:
        return "31_40"
    else:
        return "41+"

avg_prices_by_segment_sorted["AGE_CATEGORY"] = avg_prices_by_segment_sorted["AGE"].apply(categorize_age) 
data.head()

avg_prices_by_segment_sorted["customers_level_based"] = avg_prices_by_segment_sorted[["COUNTRY", "SOURCE", "SEX", "AGE_CATEGORY"]].apply(
    lambda x: '_'.join(x).upper(), axis=1)

agg_df = avg_prices_by_segment_sorted.groupby("customers_level_based").agg({"AVG_PRICE": "mean"}).reset_index()
agg_df["SEGMENT"] = pd.qcut(agg_df["AVG_PRICE"], 4, labels=["D", "C", "B", "A"])

def get_segment_price(segment_name, df):
    return df[df["customers_level_based"] == segment_name]

new_user1_segment = get_segment_price("TUR_ANDROID_FEMALE_31_40", agg_df)
new_user2_segment = get_segment_price("FRA_IOS_FEMALE_31_40", agg_df)






