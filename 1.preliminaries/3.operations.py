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
print('comparing two tensors', X1 == X2) # we can also do X1 < X2, X1 > X2

# sum all elements of a tensor
print('sum all elements', X.sum())
