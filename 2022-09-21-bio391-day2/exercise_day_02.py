import pandas as pd

col=['biosample_id','reference_name','start','end','log2','variant_type','reference_bases','alternate_bases']
df=pd.DataFrame(columns=col)

with open('data.pgxseg', 'r') as fh:
    while True:
        line = fh.readline()
        # break while statement if line does not startwith #
        if not line.startswith('#'):
            break
    while line:
        line=fh.readline()
        x=line.split()
        df=df.append(pd.DataFrame([x],columns=col),ignore_index=True)

head(df)




