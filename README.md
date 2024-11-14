# image-format-changer

This repository provides Python scripts for converting image files to .bmp format, resizing, and organizing them into train, validation, and test datasets. 

#The code is particularly suited for preparing datasets in thermal and visible image formats.

# Features

**Image Conversion:** Converts .png and .tiff images to .bmp format, resizes them to a specified resolution, and converts to grayscale. 

**Dataset Organization:** Organizes images into train, validation, and test sets with customizable ratios and sorting options.

# Requirements 

#Python 3.x
#Pillow (PIL) : for image processing
#NumPy : for handling image data
#os and shutil :for file and folder management

# Overview 

1.**convert_images_to_bmp(input_folder, output_folder, new_resolution=(40, 28))**:
Converts images in the specified input_folder and subdirectories to .bmp format, resizing and converting them to grayscale as needed.

3.**organize_images(input_folder, organize_folder="organized_data", sort_by="name")**:
Organizes images into train, validation, and test subfold

#replace the input_folder = r'path' with your own path in the code
#replace the output_folder = r'path' with your own path in the code 

