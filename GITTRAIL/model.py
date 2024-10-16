import torch

class Model(torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.fc = torch.nn.Linear(1, 1)
        self.fc.weight.data.fill_(1.0)
        self.fc.bias.data.fill_(0.0)
        
    def forward(self, x):
        return self.fc(x)
    

