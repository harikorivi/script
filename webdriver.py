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
import shutil

# Setup WebDriver
driver_path = r"C:\Users\HKORIVI\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
# Set up the ChromeDriver service
# service = Service(driver_path)

# # e.g., 'C:/path/to/chromedriver.exe'
# driver = webdriver.Chrome(service=service)

# # Open the portal and navigate to the book
# url = 'https://learning.oracle.com/player/play?in_sessionid=158241A54A804AJ9&classroom_id=1700055000'  # Replace with your URL
# driver.get(url)



# Define the options to connect to the existing Chrome session
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

# Initialize the WebDriver
#driver = webdriver.Chrome(options=chrome_options)

driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)
# Open the desired URL
# url = "https://learning.oracle.com/player/play?in_sessionid=158241A54A804AJ9&classroom_id=1700055000"
# driver.get(url)

# Initialize Chrome WebDriver with existing session
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Optional: Run in headless mode (no GUI)
options.add_argument('--no-sandbox')  # Optional: Add sandbox argument if necessary
#driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

# Create a directory to store downloaded images
os.makedirs('downloaded_images', exist_ok=True)

# Replace with the URL of the directory containing the JPG files
base_url = 'https://learning.oracle.com/secure_content_v2/ohr/media/1700054293/V2/D1107035GC10_sg/files/mobile/1.jpg?240625180142'
# base_url = 'https://learning.oracle.com/secure_content_v2/ohr/media/1700054293/V2/D1107035GC10_sg/files/mobile/'

# driver.get(base_url)



# Example URLs of JPG files to download
image_urls = [
    'https://example.com/images/image1.jpg',
    'https://example.com/images/image2.jpg',
    # Add more URLs as needed
]

# Output directory where images will be saved
# output_folder = 'downloaded_images'
# os.makedirs(output_folder, exist_ok=True)

# # Function to download image
# def download_image(url, filename):
#     driver.get(url)
#     image_element = driver.find_element_by_tag_name('img')
#     src = image_element.get_attribute('src')
#     if src.startswith('data:image'):
#         print(f'Skipping {url} as it is a base64 encoded image')
#         return
#     response = requests.get(src, stream=True)
#     with open(filename, 'wb') as out_file:
#         shutil.copyfileobj(response.raw, out_file)
#     del response

# download_image(base_url, "hari_test.jpg")

# # Download each image
# for url in image_urls:
#     filename = os.path.join(output_folder, url.split('/')[-1])  # Extract filename from URL
#     download_image(url, filename)
#     print(f'Downloaded {filename}')

# Close the WebDriver session

# Output directory where images will be saved
output_folder = 'downloaded_images'
os.makedirs(output_folder, exist_ok=True)

# Function to download JPG file using JavaScript executed through Selenium
def download_jpg_from_page(url, output_folder):
    driver.get(url)
    time.sleep(2)  # Adjust delay as needed to ensure page elements load
    driver.execute_script('window.open(arguments[0]);', driver.current_url)
    handles = driver.window_handles
    driver.switch_to.window(handles[-1])
    time.sleep(2)  # Adjust delay as needed to ensure new tab fully loads
    driver.execute_script('''\
        var link = document.createElement('a');
        link.href = arguments[0];
        link.download = 'downloaded_image.jpg';
        link.click();
        ''', driver.current_url)


# def save_page_as_pdf(url, output_folder):
#     driver.get(url)
#     time.sleep(2)  # Adjust delay as needed to ensure page loads

#     # Send Ctrl+S shortcut to save the page
#     #.send_keys('\ue009' + 's')  # '\ue009' is the Selenium key code for Control

#     # Wait for the save dialog to appear (adjust as needed)
#     time.sleep(2)

#     # Set the file name and save location in the save dialog
#     # Example: for Chrome in English, send 'file_name' + '\n'
#     driver.switch_to.active_element.send_keys(os.path.join(output_folder, 'downloaded_file.jpg') + '\n')



# JavaScript code to download the image
javascript_code = '''
// JavaScript code to download image
let imageUrl = 'https://learning.oracle.com/secure_content_v2/ohr/media/1700054293/V2/D1107035GC10_sg/files/mobile/1.jpg?240625180142';

let downloadLink = document.createElement('a');
downloadLink.href = imageUrl;
downloadLink.download = 'image.jpg';
document.body.appendChild(downloadLink);
downloadLink.click();
document.body.removeChild(downloadLink);
'''
# Download image directly using requests after navigating with Selenium
driver.get(base_url)
# save_page_as_pdf(base_url, output_folder)
# Execute JavaScript code to download the image
driver.execute_script(javascript_code)
driver.quit()

# # Number of images you want to download
# num_images = 496

# for i in range(1, num_images + 1):
#     image_url = f'{base_url}/{i}.jpg?240625180142'  # Adjust the URL pattern according to the actual URLs
#     filename = f'downloaded_images/image{i}.jpg'

#     # Download the image
#     response = requests.get(image_url)
#     with open(filename, 'wb') as f:
#         f.write(response.content)
#         print(f'Downloaded {filename}')

print('Download complete.')
# Login if necessary
# login_button = driver.find_element(By.ID, 'loginButton')
# login_button.click()
# username_field = driver.find_element(By.ID, 'username')
# password_field = driver.find_element(By.ID, 'password')
# username_field.send_keys('your_username')
# password_field.send_keys('your_password')
# login_submit = driver.find_element(By.ID, 'loginSubmit')
# login_submit.click()

# Wait for the page to load
time.sleep(20)

# # Create a directory to save screenshots
# if not os.path.exists('screenshots'):
#     os.makedirs('screenshots')

# # Function to take a screenshot
# def take_screenshot(page_num):
#     driver.save_screenshot(f'screenshots/page_{page_num}.png')

# # Capture all pages
# page_num = 1
# while True:
#     try:
#         # Take a screenshot of the current page
#         take_screenshot(page_num)
        
#         # Click the arrow to go to the next page
#         next_button = driver.find_element(By.XPATH, 'your_next_button_xpath')  # Replace with the correct XPath
#         next_button.click()
        
#         # Wait for the page to load
#         time.sleep(3)
        
#         page_num += 1
#     except Exception as e:
#         print(f'End of book or an error occurred: {e}')
#         break

# driver.quit()

# # Combine screenshots into a PDF
# images = []
# for file_name in sorted(os.listdir('screenshots'), key=lambda x: int(x.split('_')[1].split('.')[0])):
#     if file_name.endswith('.png'):
#         images.append(Image.open(os.path.join('screenshots', file_name)))

# if images:
#     images[0].save('book.pdf', save_all=True, append_images=images[1:], resolution=100.0)

print('PDF created successfully.')