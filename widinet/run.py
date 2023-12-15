import subprocess
import os
import cv2
import numpy as np


########################### INITIAL MIN-POOLING #######################################
# Directory containing the images
image_dir = "/database/jhkim/widinet/Realwild2/cockPNG"

# Get a list of image files with names containing numbers
image_files = [f for f in os.listdir(image_dir) if f.split(".")[0].isdigit() and f.endswith((".jpg", ".png"))]

# Initialize an empty list to store image data
image_data_list = []

# Load images and store their data in the list
for image_file in image_files:
    image_path = os.path.join(image_dir, image_file)
    image_data = cv2.imread(image_path)
    image_data_list.append(image_data)

# Convert the list of image data to a NumPy array
image_data_array = np.array(image_data_list)


# Create a new image by finding the darkest value for each pixel (min-pooling)
darkest_image = np.min(image_data_array, axis=0)

# Subtract the darkest image pixel values from all selected images
darkened_images = image_data_array - darkest_image

# Save the darkened images (optional)
output_dir = "/database/jhkim/widinet/initial_minpooling/cock"
os.makedirs(output_dir, exist_ok=True)

for i, darkened_image in enumerate(darkened_images):
    output_path = os.path.join(output_dir, f"{i}.png")
    cv2.imwrite(output_path, darkened_image)
########################### RELIGHTING #######################################
# Define the full paths to the test.py script and the configuration file
test_script_path = "/database/jhkim/widinet/IAN/test.py"
config_file_path = "/database/jhkim/widinet/IAN/options/cock.yml"

# Build the command to run train.py with the specified configuration file
command = f"python {test_script_path} -opt {config_file_path}"

# Execute the command using subprocess
subprocess.run(command, shell=True)

########################### REFINED MIN-POOLING #######################################
# Directory containing the images
image_dir = "/database/jhkim/widinet/Realwild2/cockPNG"

# Get a list of image files with names containing numbers
image_files = [f for f in os.listdir(image_dir) if f.split(".")[0].isdigit() and f.endswith((".jpg", ".png"))]

# Initialize an empty list to store image data
image_data_list = []

# Load images and store their data in the list
for image_file in image_files:
    image_path = os.path.join(image_dir, image_file)
    image_data = cv2.imread(image_path)
    
    image_data_list.append(image_data)


# Get a list of relighted image files
relighted_image_files = ["/database/jhkim/widinet/initial_minpooling/cock/16.png", "/database/jhkim/widinet/initial_minpooling/cock/17.png"]
# Load images and store their data in the list
# Load images and store their data in the list
for image_file in relighted_image_files:
    image_path = os.path.join(image_dir, image_file)
    image_data = cv2.imread(image_path)
    
    image_data_list.append(image_data)



# Convert the list of image data to a NumPy array
image_data_array = np.array(image_data_list)

# Create a new image by finding the darkest value for each pixel (min-pooling)
darkest_image = np.min(image_data_array, axis=0)

# Subtract the darkest image pixel values from all selected images
darkened_images = image_data_array - darkest_image

# Save the darkened images (optional)
output_dir = "/database/jhkim/widinet/refined_minpooling/cock"
os.makedirs(output_dir, exist_ok=True)

for i, darkened_image in enumerate(darkened_images):
    output_path = os.path.join(output_dir, f"{i}.png")
    cv2.imwrite(output_path, darkened_image)

# ######################### NORMAL ESTIMATION ###################################
# Define the full paths to the train.py script and the configuration file
train_script_path = "/database/jhkim/widinet/SCPS-NIR/train.py"
config_file_path = "/database/jhkim/widinet/SCPS-NIR/configs/diligent/cock.yml"

# Build the command to run train.py with the specified configuration file
command = f"python {train_script_path} --config {config_file_path} --testing True --quick_testing True"

# Execute the command using subprocess
subprocess.run(command, shell=True)


