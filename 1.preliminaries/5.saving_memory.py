import torch

a = torch.arange(3).reshape((3, 1))
b = torch.arange(2).reshape((1, 2))

# Running operations can cause new memory to be allocated to host results. For example, if
# we write b = a + b, we dereference the tensor that b used to point to and instead point b at
# the newly allocated memory. We can demonstrate this issue with Python’s id() function,
# which gives us the exact address of the referenced object in memory. Note that after we
# run b = b + a, id(b) points to a different location. That is because Python first evaluates
# b + a, allocating new memory for the result and then points b to this new location in
# memory.
before = id(b)
b = b + a
print( id(b) == before)

# This might be undesirable for two reasons. First, we do not want to run around allocating memory unnecessarily all the time. In machine learning, we often have hundreds of
# megabytes of parameters and update all of them multiple times per second. Whenever
# possible, we want to perform these updates in place. Second, we might point at the same
# parameters from multiple variables. If we do not update in place, we must be careful to
# update all of these references, lest we spring a memory leak or inadvertently refer to stale
# parameters.

# updating in place
Z = torch.zeros_like(b) # zeros_like(b) will create a tensor with all zeros and shape as b
print('id(Z):', id(Z))
Z[:] = a + b
print('id(Z):', id(Z))