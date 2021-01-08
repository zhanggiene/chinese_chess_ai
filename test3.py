import pickle
a=pickle.dumps([(1,2),(3,2)])
b=pickle.loads(a)
print(b)