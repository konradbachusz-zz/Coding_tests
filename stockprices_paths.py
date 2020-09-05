import numpy as np
import pandas as pd
import datetime as dt


def solution(files):
    # files - any of available files, i.e:
    # files = ["./data/framp.csv", "./data/gnyned.csv", "./data/gwoomed.csv",
    #            "./data/hoilled.csv", "./data/plent.csv", "./data/throwsh.csv",
    #            "./data/twerche.csv", "./data/veeme.csv"]

    # write your solution here
    list_of_lists=[]
    for path in files:
        df=pd.read_csv(path,engine='python')
        df.date=df.date.apply(pd.to_datetime)
        df['year']=df.date.dt.year
        subset1=df.groupby(df['date'].dt.year)['vol'].agg(['max']).reset_index()
        subset1=subset1.rename(columns={"date": "year",'max':'vol'})
        df1=pd.merge(subset1,df,on=['year','vol'],how='left')[['date','vol']]
    

        subset2=df.groupby(df['date'].dt.year)['close'].agg(['max']).reset_index()
        subset2=subset2.rename(columns={"date": "year",'max':'close'})
        df2=pd.merge(subset2,df,on=['year','close'],how='left')[['date','close']]

        pair=[df1,df2]
        list_of_lists.append(pair)
    return list_of_lists

solution(["./data/aapl.csv","./data/avis.csv",'./data/GE.csv',"./data/tsla.csv"])