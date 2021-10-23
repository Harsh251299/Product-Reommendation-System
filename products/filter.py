import pandas as pd
import numpy as np
df=pd.read_csv("C:\\Users\\Harsh Patel\\Desktop\\SEM 5\\PDS\\Project\\productFilter\\products\\laptops.csv")
option={}

def option_set():
    global df,option
    for x in list(df.columns):

        if(x=="Product") or (x=="Inches") or (x=="Gpu") or (x=="DisplayType") or (x=="ScreenResolution") or (x=="Weight"):
            continue
        
        elif(x=="Cpu"):  
            option["Cpu"]=[]
            for i in range(len(df)):
                str0=str(df.loc[i,"Cpu"]).split(" ")
                if len(str0)>3:
                    str0=" ".join(str0[0:-1])
                    option["Cpu"].append(str0)
                else:
                    str0=" ".join(str0)
                    option["Cpu"].append(str0)
            option["Cpu"]=sorted(list(set(option["Cpu"])))

        elif(x=="Memory"):
            option["MemorySize"]=[]
            option["MemoryType"]=[]
            for i in range(len(df)):
                str0=str(df.loc[i,"Memory"]).split("+")
                if len(str0)>1:
                    str1= (str0[0].strip(" ")).split(" ")
                    option["MemorySize"].append(str1[0])
                    option["MemoryType"].append(" ".join(str1[1:]))
                    str1= (str0[1].strip(" ")).split(" ")
                    option["MemorySize"].append(str1[0])
                    option["MemoryType"].append(" ".join(str1[1:]))
                if len(str0)==1:
                    str1= (str0[0].strip(" ")).split(" ")
                    option["MemorySize"].append(str1[0])
                    option["MemoryType"].append(" ".join(str1[1:]))
            option["MemorySize"]=sorted(list(set(option["MemorySize"])))
            option["MemoryType"]=sorted(list(set(option["MemoryType"])))
                

        elif(x=="Price"):
            prizelist0=list(map(float,list(df[x].unique())))
            option[x]=[min(prizelist0),max(prizelist0)]
            
        else:
            option[x]=sorted(list(df[x].unique()))
    return option

def filter(Company=None,OpSys=None,TypeName=None,Cpu=None,Ram=None,Price=None,Speed=None,MemSize=None,MemType=None):
    df=pd.read_csv("C:\\Users\\Harsh Patel\\Desktop\\SEM 5\\PDS\\Project\\productFilter\\products\\laptops.csv")
    fltdf=df
    filteredResult=[]

    if Company:
        fltdf=fltdf[fltdf["Company"].isin(Company)]
        fltdf.reset_index(inplace=True)
        fltdf=fltdf.drop("index",axis=1)

    if OpSys:
        fltdf=fltdf[fltdf["OpSys"].isin(OpSys)]
        fltdf.reset_index(inplace=True)
        fltdf=fltdf.drop("index",axis=1)

    if TypeName:
        fltdf=fltdf[fltdf["TypeName"].isin(TypeName)]
        fltdf.reset_index(inplace=True)
        fltdf=fltdf.drop("index",axis=1)

    if Ram:
        fltdf=fltdf[fltdf["Ram"].isin(Ram)]
        fltdf.reset_index(inplace=True)
        fltdf=fltdf.drop("index",axis=1)

    if Price:
        price_min=float(Price[0])
        price_max=float(Price[1])
        fltdf=fltdf[(fltdf["Price"]>=price_min) & (fltdf["Price"]<=price_max)]
        fltdf.reset_index(inplace=True)
        fltdf=fltdf.drop("index",axis=1)
    
    if MemSize:
        drops=0
        for i in range(0,len(fltdf)):
            containing=0
            for j in MemSize:
                if j in (str(fltdf.loc[i,"Memory"])):
                    containing=1
                    break
            if containing==0:
                fltdf.drop(fltdf.index[i-drops],inplace=True)
                drops+=1
        fltdf.reset_index(inplace=True)
        fltdf=fltdf.drop("index",axis=1)
    
    if MemType:
        drops=0
        for i in range(0,len(fltdf)):
            containing=0
            for j in MemType:
                if j in (str(fltdf.loc[i,"Memory"])):
                    containing=1
                    break
            if containing==0:
                fltdf.drop(fltdf.index[i-drops],inplace=True)
                drops+=1
        fltdf.reset_index(inplace=True)
        fltdf=fltdf.drop("index",axis=1)

    if Cpu:
        drops=0
        for i in range(0,len(fltdf)):
            containing=0
            for j in Cpu:
                if j in (str(fltdf.loc[i,"Cpu"])):
                    containing=1
                    break
            if containing==0:
                fltdf.drop(fltdf.index[i-drops],inplace=True)
                drops+=1
        fltdf.reset_index(inplace=True)
        fltdf=fltdf.drop("index",axis=1)

    for i in range(0,len(fltdf)):
        filteredResult.append(list(fltdf.iloc[i,:]))
    return filteredResult


