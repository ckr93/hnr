import pandas as pd
# df1 = pd.read_csv('E:/IIT/4th year/Project/Data Set/Cleaned Data/accountants.csv',index_col=[0], parse_dates=[0])
# df2 = pd.read_csv('E:/IIT/4th year/Project/Data Set/Cleaned Data/ceo.csv',index_col=[0], parse_dates=[0])
# df3 = pd.read_csv('E:/IIT/4th year/Project/Data Set/Cleaned Data/pm.csv',index_col=[0], parse_dates=[0])
# df4 = pd.read_csv('E:/IIT/4th year/Project/Data Set/Cleaned Data/SE_Virtusa.csv',index_col=[0], parse_dates=[0])
# df5 = pd.read_csv('E:/IIT/4th year/Project/Data Set/Cleaned Data/SE_Zone.csv',index_col=[0], parse_dates=[0])
# df6 = pd.read_csv('E:/IIT/4th year/Project/Data Set/Cleaned Data/TL.csv',index_col=[0], parse_dates=[0])
# df7 = pd.read_csv('E:/IIT/4th year/Project/Data Set/Cleaned Data/vitusa_final.csv',index_col=[0], parse_dates=[0])
#
# finaldf = pd.concat([df1, df2, df3,df4,df5,df6,df7], axis=1, join='inner').sort_index()
# finaldf.to_csv('E:/IIT/4th year/Project/Data Set/Cleaned Data/final.csv')
df1 = pd.read_csv('E:/IIT/4th year/Project/Data Set/Cleaned Data/final1.csv')
print(df1)