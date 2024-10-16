import torch

class Model(torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.fc = torch.nn.Linear(1, 1)
        
    def forward(self, x):
        return self.fc(x)
    

