import pandas as pd

colnames = ['data']
df = pd.read_csv("..\data\data.txt", header=None)
rows = df.shape[0]
lncount = 0

for i in range(1,rows):
    if i+2 <rows :
        sumA = df.iloc[i-1:i+1,0].sum()
        sumB = df.iloc[i:i+2,0].sum()
        print(sumA,sumB)
        if sumB>sumA:
            lncount+=1

print(lncount)