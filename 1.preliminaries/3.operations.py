import torch

X = torch.arange(12, dtype=torch.float32).reshape(-1,4)
print('tensor', X)

# apply unary scalar operator on every element. f: R -> R where R is real number. ex: e**x
# e is Euler's number / exponential constant equals to 2.718. https://www.mathcentre.ac.uk/resources/uploaded/mc-bus-expconstant-2009-1.pdf
print('performing exponential on every element of tensor', torch.exp(X))

X1 = torch.arange(12, dtype=torch.float32).reshape((3,4))
X2 = torch.tensor([[2.0, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])

# apply binary scalar operator on every element. f: R,R -> R where R is real number.
print('X1+X2', X1+X2)
print('X1-X2', X1-X2)
print('X1*X2', X1*X2)
print('X1/X2', X1/X2)
print('X1**X2', X1**X2)

# concatenating tensors
print('concatenating tensors along dimension 0', torch.cat((X1,X2), dim=0))
print('concatenating tensors along dimension 1', torch.cat((X1,X2), dim=1))

# constructing binary tensor via logical statement
print('comparing two tensors', X1 == X2)

# sum all elements of a tensor
print('sum all elements', X.sum())

# Broadcasting. When the two tensors are of different shape, we can still perform binary operations
a = torch.arange(3).reshape((3, 1))
b = torch.arange(2).reshape((1, 2))
print ('a',a)
print ('b',b)
# Since a and b are 3 × 1 and 1 × 2 matrices, respectively, their shapes do not match up.
# Broadcasting produces a larger 3 × 2 matrix by replicating matrix a along the columns and
# matrix b along the rows before adding them elementwise
# i.e
# a = [[0, 0],
#      [1, 1],
#      [2, 3]]
# b = [[0, 1],
#      [0, 1],
#      [0, 1]]
# a+b = [[0, 1],
#        [1, 2],
#        [2, 3]]
print('adding two tensors of different shape', a+b)