import torch

# creating a tensor
x = torch.arange(12, dtype=torch.float32)
print("created with torch.arange \n",x)

# number elements in a tensor
print("get number of elements in a tensor using x.numel() function \n",x.numel())

# shape of a tensor
print("get shape of the tensor using x.shape property \n", x.shape)

# reshaping a tensor
X = x.reshape(3,4) # given one argument other can be inferred ex: x.reshape(3,-1) or x.reshape(-1,4)
print("reshape a tensor using x.reshape(3,4) or x.reshape(-1,4) or x.reshape(3,-1) function. one argument can be passed as -1 in which case the function will calculate the value of it \n",X)

# creating a tensor and fill with zeros
X0s = torch.zeros((2,3,4))
print("create a tensor with all zeros using torch.zeros((2,3,4)) function \n",X0s)

# creating a tensor and fill with ones
X1s = torch.ones((2,3,4))
print("create a tensor with all ones using torch.ones((2,3,4)) function \n",X1s)

# creating a tensor and fill with random numbers with mean 0 and standard deviation 1
Xrandn = torch.randn((2,3,4))
print("create a tensor with random numbers where mean is 0 and standard deviation is 1 for the set using torch.randn((2,3,4)) function \n",Xrandn)

# creating a tensor by passing elements
Xpass = torch.tensor([[1,5,6], [2,4,9],[7,9,3]])
print("create a tensor with by passing all elements using torch.tensor([[1,5,6], [2,4,9],[7,9,3]]) function \n",Xpass)
