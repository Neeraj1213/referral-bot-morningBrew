import time
import string
import os
import json
import linecache
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# Path to the chromedriver executable
# driver_path = 'path/to/chromedriver'

# Path to the email.txt file
# email_path = 'path/to/email.txt'

# Load the email from the file
# with open(email_path, 'r') as f:
#     email = f.read().strip()

total = 1

# Importing Settings
settingU = json.load(open('settings.json'))
jtopy = json.dumps(settingU)
setting = json.loads(jtopy)


# Initialize the webdriver
driver = webdriver.Chrome()

# Navigate to the Morning Brew sign-up page
driver.get('https://www.morningbrew.com/daily/r?kid=36e1023c')

for emailToUse in emails:
        # Find the email input field and enter the email
    emailToUse = linecache.getline('emails.txt', total)

    emailInput = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div[2]/div/form/input')
    emailInput.send_keys(emailToUse)

    # Find the "Continue" button and click it
    continue_button = driver.find_element(By.XPATH, '')
    continue_button.click()

# Wait for the page to load
time.sleep(5)

# Close the webdriver
driver.quit()
