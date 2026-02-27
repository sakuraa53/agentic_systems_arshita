import numpy as np
np.random.seed(42)
data= np.random.randint(0,100,(100,2))
#mean&standard deviation 
mean=data.mean(axis=0)
std= data.std(axis=0)
#normalize
normalized=(data-mean)/std
#split(80% tarin, 20%test data)
split_index=int(0.8*len(normalized))
train = normalized[:split_index]
test = normalized [split_index:]
print("before:", normalized[0,0])
train[0,0]=999
print("after:", normalized[0,0])
#print shapes
print("\nOriginal shape:", data.shape)
print("mean shape:", mean.shape)
print("std shape:", std.shape)
print("train shape:", train.shape)
print("test shape:", test.shape)
print("\nNote: Changing train also changed normalized(slicing give views):")
