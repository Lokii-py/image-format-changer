from PIL import Image
import os
import shutil
import random
import numpy as np

def convert_images_to_bmp(input_folder, output_folder, new_resolution=(40, 28)):
    """
    Convert all .png and .tiff images in a given folder and subfolders to .bmp format.
    The images are resized to new_resolution and converted to grayscale if not already.
    """
    for root, _, files in os.walk(input_folder):
        for filename in files:
            if filename.endswith('.png') or filename.endswith('.tiff'):
                
                # Set up paths for input and output
                img_path = os.path.join(root, filename)
                relative_path = os.path.relpath(root, input_folder)  # Preserve subdirectory structure
                output_subfolder = os.path.join(output_folder, relative_path)
                os.makedirs(output_subfolder, exist_ok=True)
                
                # Process the image
                img = Image.open(img_path)
                if img.mode == 'I;16':  # Convert 16-bit to 8-bit
                    img = Image.fromarray((np.array(img) / 256).astype('uint8'))
                if img.mode != 'L':  # Convert to grayscale if not already
                    img = img.convert('L')
                
                # Resize and save as .bmp
                img_resized = img.resize(new_resolution, Image.BICUBIC)
                new_filename = os.path.splitext(filename)[0] + '.bmp'
                output_path = os.path.join(output_subfolder, new_filename)
                img_resized.save(output_path, format='BMP')
                
                print(f'Converted {filename} to {new_filename} in {output_subfolder} with resolution {new_resolution}')

def organize_images(input_folder, organize_folder="organized_data", sort_by="name"):
    """
    Organize images into train, validation, and test folders after conversion.
    Images are randomly shuffled, sorted if needed, and distributed based on specified split ratios.
    """
    # Paths for train, validation, and test folders
    train_folder = os.path.join(organize_folder, "train")
    validation_folder = os.path.join(organize_folder, "val")
    test_folder = os.path.join(organize_folder, "test")
    os.makedirs(train_folder, exist_ok=True)
    os.makedirs(validation_folder, exist_ok=True)
    os.makedirs(test_folder, exist_ok=True)

    # Collect all .bmp images from the input folder and subdirectories
    images = []
    for root, _, files in os.walk(input_folder):
        for filename in files:
            if filename.endswith('.bmp'):
                images.append(os.path.join(root, filename))

    # Sort and shuffle images
    if sort_by == "name":
        images.sort()
    random.shuffle(images)  # Randomly distribute images

    # Define split ratios
    train_split = int(0.7 * len(images))
    validation_split = int(0.85 * len(images))

    # Distribute images across train, val, and test folders
    for idx, image_path in enumerate(images):
        filename = os.path.basename(image_path)
        if idx < train_split:
            shutil.copy(image_path, os.path.join(train_folder, filename))
            print(f"Copied to train: {filename}")
        elif idx < validation_split:
            shutil.copy(image_path, os.path.join(validation_folder, filename))
            print(f"Copied to validation: {filename}")
        else:
            shutil.copy(image_path, os.path.join(test_folder, filename))
            print(f"Copied to test: {filename}")

    print(f"Images have been organized into '{organize_folder}' with 'train', 'val', and 'test' subfolders.")

base_input_folder = r'path'  # Main dataset folder 
output_folder = r'path'  # Output folder for .bmp images

if __name__ == "__main__":
    convert_images_to_bmp(os.path.join(base_input_folder, 'thermal'), os.path.join(output_folder, 'thermal'))
    convert_images_to_bmp(os.path.join(base_input_folder, 'visible'), os.path.join(output_folder, 'visible'))
    
    # Organize images into train, val and test
    organize_images(output_folder, sort_by="name")
