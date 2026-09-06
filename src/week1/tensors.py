import torch
# x = torch.tensor([1,2,3,4])
# print(x)
# print(x.shape)
# print(x.ndim)
# print(x.dtype)

# y = torch.tensor([
#     [1,2,3],
#     [4,5,6]
# ])
# print(y)
# print("shape of y: ",y.shape)
# print("dimesnion of y: ",y.ndim)
# print("dtype: ", y.dtype);

x = torch.zeros(3)
print(x, x.shape, x.ndim)
x=torch.ones(3)
print(x, x.shape, x.ndim)
x=torch.arange(5)
print(x, x.shape, x.ndim)
x = torch.randn(2,3)
print(x, x.shape, x.ndim)