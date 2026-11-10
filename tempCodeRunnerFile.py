mergedf = pd.merge(leftdf , rightdf , how='inner' , on='id')
print(mergedf)