import cv2
import numpy as np
from PIL import Image
import os
from zipfile import ZipFile

def process_spritesheet(input_path, output_directory):
    img = cv2.imread(input_path, cv2.IMREAD_UNCHANGED)
    alpha_channel = img[:, :, 3]

    contours, _ = cv2.findContours(alpha_channel, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    images = []
    for i, contour in enumerate(contours):
        x, y, w, h = cv2.boundingRect(contour)
        pose = img[y:y+h, x:x+w]
        images.append(pose)
        cv2.imwrite(os.path.join(output_directory, f"pose_{i + 1}.png"), pose)

    # Save images in a zip file
    zip_file_path = os.path.join(output_directory, "output_images.zip")
    with ZipFile(zip_file_path, 'w') as zip_file:
        for i, pose in enumerate(images):
            zip_file.write(os.path.join(output_directory, f"pose_{i + 1}.png"), f"pose_{i + 1}.png")

if __name__ == "__main__":
    process_spritesheet("spritesheet.png", "output_directory")
