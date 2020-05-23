import torch
import torch.nn as nn
import torch.nn.functional as F


class Shallow(nn.Module):

    def __init__(self, img_size=28, hidden_size=800, num_classes=10):
        super(Shallow, self).__init__()

        self.hidden_size = hidden_size
        self.num_classes = num_classes
        self.img_size = img_size

        self.fc1 = nn.Linear(self.img_size**2, self.hidden_size)
        self.fc2 = nn.Linear(self.hidden_size, self.hidden_size)
        self.fc3 = nn.Linear(self.hidden_size, self.num_classes)

    def forward(self, x):
        x = torch.flatten(x, 1)
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(x)
        x = F.relu(x)
        out = self.fc3(x)

        return out
