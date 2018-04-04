import pandas as pd
df = pd.DataFrame([[1,2,3],[2,3,4],[2,4,3],[1,3,7]],index = ['one','two','three','four'],columns = ['A','B','C'])
print(df )

df.sort_values(by=['A','B'],ascending=[0,1],inplace=True)
print(df)