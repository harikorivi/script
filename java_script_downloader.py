from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import shutil
import base64


driver_path = r"C:\Users\HKORIVI\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')  # Optional: Run Chrome in headless mode
chrome_options.add_argument('--disable-gpu')
# Define the options to connect to the existing Chrome session
# chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
# chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:60776")

# Initialize the WebDriver
#driver = webdriver.Chrome(options=chrome_options)

# image_url = r"https://learning.oracle.com/secure_content_v2/ohr/media/1700054293/V2/D1107035GC10_sg/files/mobile/2.jpg?240625180142"
image_url = r"https://learning.oracle.com/secure_content_v2/ohr/media/657135545/V2/D1103181GC10_sg/files/mobile/1.jpg?220923160410"

#Student Guide
#base_url = r"https://learning.oracle.com/secure_content_v2/ohr/media/1700054293/V2/D1107035GC10_sg/files/mobile"
#Activity Guide
#base_url = r"https://learning.oracle.com/secure_content_v2/ohr/media/1700081792/V1/D1107035GC10_ag/files/mobile"
#Student _guide helidon
#base_url = r"https://learning.oracle.com/secure_content_v2/ohr/media/773537691/V1/S1104923GC10_sg/files/mobile"
# Activity Guide Helidon
base_url = r"https://learning.oracle.com/secure_content_v2/ohr/media/123490159/V2/S109871GC10_ag/files/mobile"

# Function to download image
def download_image(url, filename):
    try:
        driver.get(url)
        time.sleep(1)  # Adjust delay as needed to ensure new tab fully loads
        # Find the image element
        image_element = driver.find_element(By.CSS_SELECTOR, "body > img")
        src = image_element.get_attribute('src')
        
        # Check if the image source starts with 'data:image'
        if src.startswith('data:image'):
            print(f'Skipping {url} as it is a base64 encoded image')
            return
        
        # Execute JavaScript to fetch image data as base64
        base64_data = driver.execute_script(f'''
            var xhr = new XMLHttpRequest();
            xhr.open('GET', "{src}", true);
            xhr.responseType = 'blob';
            xhr.onload = function(e) {{
                if (this.status == 200) {{
                    var blob = this.response;
                    var reader = new FileReader();
                    reader.onload = function(event) {{
                        var base64data = event.target.result.split(',')[1];
                        window.localStorage.setItem('imageData', base64data);
                    }};
                    reader.readAsDataURL(blob);
                }}
            }};
            xhr.send();
        ''')
        
        # Get the image data from local storage
        base64_data = driver.execute_script('return window.localStorage.getItem("imageData");')
        
        # Decode base64 data to binary
        binary_data = base64.b64decode(base64_data)
        
        # Write binary data to file
        with open(filename, 'wb') as f:
            f.write(binary_data)
        
        print(f"Downloaded image from {url} to {os.path.abspath(filename)}")
    except Exception as e:
        print(f"Error downloading image from {url}: {str(e)}")


driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)

# Execute the script
# driver.execute_script(download_script)
# download_image(image_url, "hari_test.jpg")

# Output directory where images will be saved
# output_folder = 'downloaded_images'
output_folder = 'download_PL_SQL_19C_AG_Advanced'
os.makedirs(output_folder, exist_ok=True)
# Number of images you want to download
# num_images = 496
num_images = 134
# .jpg?240513235307
# .jpg?240625180142
for i in range(1, num_images + 1):
    image_url = f'{base_url}/{i}.jpg?210203150349'  # Adjust the URL pattern according to the actual URLs
    filename = f'{output_folder}/image{i}.jpg'

    # Download the image
    download_image(image_url, filename)
    print(f'Downloaded {filename}')
driver.quit()
print('Download complete.')