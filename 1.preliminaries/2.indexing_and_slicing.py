import torch
X = torch.arange(12).reshape(3,-1)
print(X)

# we can access tensor elements by index starting 0. This access relative to beginning of the tensor
print('accessing relative to start', X[1])

# we can use negative numbers to access elements relative to end of the tensor
print('accessing relative to end', X[-1])

# slicing the tensor using range include start but excludes end
print('accessing a range of tensor', X[1:2])
print('accessing a range of tensor without stop index will return all elements from the start(including)', X[1:])
print('accessing a range of tensor without start index will return all elements until the end(excluding)', X[:2])
print('accessing a range of sub-tensor', X[1,1:])

# writing to tensor
X[1,2] = 17
print('writing 17 to 2nd row 3rd element', X)

# setting same value to multiple elements
X[:2, :] = 12
X[2, :3] = 20
print('writing same value to multiple element', X)
