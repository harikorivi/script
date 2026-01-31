import requests
import os

# Replace with the URL of the directory containing the JPG files
base_url = 'https://learning.oracle.com/secure_content_v2/ohr/media/1700054293/V2/D1107035GC10_sg/files/mobile/'

# Create a directory to store downloaded images
os.makedirs('downloaded_images', exist_ok=True)

# Number of images you want to download
num_images = 496

for i in range(1, num_images + 1):
    image_url = f'{base_url}/{i}.jpg?240625180142'  # Adjust the URL pattern according to the actual URLs
    filename = f'downloaded_images/image{i}.jpg'

    # Download the image
    response = requests.get(image_url)
    with open(filename, 'wb') as f:
        f.write(response.content)
        print(f'Downloaded {filename}')

print('Download complete.')
