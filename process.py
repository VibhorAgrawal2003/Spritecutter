import cv2
import numpy as np
from PIL import Image
import os
from zipfile import ZipFile

# Split using specific dimension
def split_image(input_path, output_directory, width, height):
    # Load the image
    img = cv2.imread(input_path, cv2.IMREAD_UNCHANGED)

    # Get the height and width of the image
    image_height, image_width, _ = img.shape

    # Calculate the number of rows and columns for splitting
    rows = image_height // height
    columns = image_width // width

    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Split the image
    images = []
    for i in range(rows):
        for j in range(columns):
            # Calculate the starting and ending points for the current region
            start_row, end_row = i * height, (i + 1) * height
            start_col, end_col = j * width, (j + 1) * width

            # Extract the region
            pose = img[start_row:end_row, start_col:end_col]
            images.append(pose)

            # Saving individual images
            cv2.imwrite(os.path.join(output_directory, f"pose_{i + 1}_{j + 1}.png"), pose)
            

# Perform a smart splitting
def process_spritesheet(input_path, output_directory):

    # Load spritesheet and locate individual contours
    img = cv2.imread(input_path, cv2.IMREAD_UNCHANGED)
    alpha_channel = img[:, :, 3]
    contours, _ = cv2.findContours(alpha_channel, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Process each contour (pose) in the spritesheet   
    images = []
    for i, contour in enumerate(contours):

        # Extract the pose region from the spritesheet
        x, y, w, h = cv2.boundingRect(contour)
        pose = img[y:y+h, x:x+w]
        images.append(pose)

        # Saving individual images
        cv2.imwrite(os.path.join(output_directory, f"pose_{i + 1}.png"), pose)

# Zip the output images
def export_zipped(path, images):
    zip_file_path = os.path.join(path, "output_images.zip")
    with ZipFile(zip_file_path, 'w') as zip_file:
        for i, pose in enumerate(images):
            zip_file.write(os.path.join(path, f"pose_{i + 1}.png"), f"pose_{i + 1}.png")




