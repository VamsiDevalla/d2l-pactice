import torch


X = torch.arange(12)

# converting to numpy ndarray
A = X.numpy()

# converting to torch tensor
B = torch.from_numpy(A)
print(type(A), type(B))

# The torch tensor and NumPy array will share their underlying memory,
# and changing one through an in-place operation will also change the other
B[3] = 14
print('A', A)
print('B', B)

# To convert a size-1 tensor to a Python scalar, we can invoke the item function
# or Python’s built-in functions.
a = torch.tensor([3.5])
print(a, a.item(), float(a), int(a))
