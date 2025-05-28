import cv2
import torch
import numpy as np
from model.dncnn import DnCNN
from torchvision import transforms
from PIL import Image
import os

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model = DnCNN(channels=1)
model.load_state_dict(torch.load("dncnn_jpeg.pth", map_location=device))
model.eval().to(device)

transform = transforms.Compose([
    transforms.Grayscale(),
    transforms.ToTensor()
])

def recover_image(image_path):
    original = Image.open(image_path)
    tensor = transform(original).unsqueeze(0).to(device)
    output = model(tensor).cpu().squeeze(0).squeeze(0).detach().numpy()
    output = np.clip(output * 255, 0, 255).astype(np.uint8)
    return output

for img_name in os.listdir('test_data/compressed'):
    output = recover_image(f'test_data/compressed/{img_name}')
    cv2.imwrite(f'test_data/recovered/{img_name}', output)
