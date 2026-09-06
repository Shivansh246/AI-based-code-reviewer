import torch
import torch.nn as nn

# layer = nn.Linear(3,2)
# x=torch.tensor(
#     [1.0,2.0,3.0]
# )
# output=layer(x)

# print("input:")
# print(x)

# print("output: ")
# print(output)

# print("input shape: ",x.shape)
# print("output shape: ",output.shape)

# print("weights: ")
# print(layer.weight)

# print("bias: ")
# print(layer.bias)
model = nn.Sequential(
    nn.Linear(4, 8),
    nn.ReLU(),
    nn.Linear(8, 2)
)

x = torch.tensor([
    [1.0, 2.0, 3.0, 4.0]
])

output=model(x)
print(x)
print(output)
print(output.shape)