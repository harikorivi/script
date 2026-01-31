from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
import time
import os
import requests

# Setup WebDriver
path = r"C:\Users\HKORIVI\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
# Define the options to connect to the existing Chrome session
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

driver = webdriver.Chrome(service=Service(path), options=chrome_options)


# Create a directory to store downloaded images
os.makedirs('downloaded_images', exist_ok=True)

# Replace with the URL of the directory containing the JPG files
base_url = 'https://learning.oracle.com/secure_content_v2/ohr/media/1700054293/V2/D1107035GC10_sg/files/mobile/1.jpg?240625180142'
# base_url = 'https://learning.oracle.com/secure_content_v2/ohr/media/1700054293/V2/D1107035GC10_sg/files/mobile/'

driver.get(base_url)

# Output directory where images will be saved
output_folder = 'downloaded_images'
os.makedirs(output_folder, exist_ok=True)

# Download the image
def download_image(url, save_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Image downloaded: {save_path}")
    else:
        print(f"Failed to download image. Status code: {response.status_code}")

# Define the save path for the image
save_path = os.path.join(os.getcwd(), 'downloaded_image.jpg')
download_image(base_url, "1.jpg")

print('PDF created successfully.')