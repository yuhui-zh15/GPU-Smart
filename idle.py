import torch

linear = torch.nn.Linear(1, 1).cuda()
while True:
    data = torch.autograd.Variable(torch.ones(1, 1)).cuda()
    output = linear(data)
