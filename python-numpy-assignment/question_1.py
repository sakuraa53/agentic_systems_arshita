import numpy as np

data = np.array([10, 20, 30, 40])

mean = np.mean(data)
std = np.std(data)

normalized = (data - mean) / std

reshaped = normalized.reshape(2,2)

print('Original data: [10 20 30 40]')
print('Mean: ', mean)
print('Standard Deviation: ', std)
print('Normalized Data: ', normalized)
print('Reshaped data shape: ', reshaped.shape)
