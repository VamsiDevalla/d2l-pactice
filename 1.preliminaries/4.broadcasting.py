import torch

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
