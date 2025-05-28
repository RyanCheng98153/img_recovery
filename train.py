import torch
from torch import nn, optim
from torch.utils.data import DataLoader
from torchvision.datasets import ImageFolder
from torchvision import transforms
from model.dncnn import DnCNN

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

transform = transforms.Compose([
    transforms.Grayscale(),
    transforms.ToTensor()
])

dataset = ImageFolder('data/', transform=transform)
loader = DataLoader(dataset, batch_size=16, shuffle=True)

model = DnCNN(channels=1).to(device)
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=1e-3)

for epoch in range(10):
    for inputs, _ in loader:
        noisy = inputs + 0.1 * torch.randn_like(inputs)
        noisy, inputs = noisy.to(device), inputs.to(device)
        output = model(noisy)
        loss = criterion(output, inputs)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    print(f"Epoch {epoch}, Loss: {loss.item():.4f}")

torch.save(model.state_dict(), 'dncnn_jpeg.pth')
