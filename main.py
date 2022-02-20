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

# Importing Settings
settingU = json.load(open('settings.json'))
jtopy = json.dumps(settingU)
setting = json.loads(jtopy)

# Starting Chromedriver
print('Starting...')
os.environ['WDM_LOG_LEVEL'] = '0'
caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "normal"
chrome_options = Options()
if setting["headlessMode"]:
	chrome_options.add_argument("--headless")
chrome_options.add_argument("--mute-audio")
os.system('clear')

# Generate Emails

if setting['generate']:
	f = open('emails.txt', 'w')
	emailSplit = setting["baseEmail"].split("@")
	username = emailSplit[0]
	suffix = '@' + emailSplit[1]
	emails = list()
	emailLength = len(username)
	combinations = pow(2, emailLength - 1)
	padding = "{0:0" + str(emailLength - 1) + "b}"
	for i in range(0, combinations):
		bin = padding.format(i)
		fullEmail = ""
		for j in range(0, emailLength - 1):
			fullEmail += username[j]
			if bin[j] == "1":
				fullEmail += "."
		fullEmail += username[j + 1]
		emails.append(fullEmail + suffix)

	for email in emails:
		f.write(email + '\n')
	f.close()

	print("Emails Generated and saved to emails.txt")

	settingFile = open("settings.json", "r")
	jsonSetting = json.load(settingFile)
	settingFile.close()
	jsonSetting["generate"] = False
	settingFile = open("settings.json", "w")
	json.dump(jsonSetting, settingFile, indent=2)
	settingFile.close()

	print("Settings Saved")


successful = 1
total = 1

def run():
	global total
	global successful
	# Open Ref Link
	driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options, desired_capabilities=caps)
	os.system('clear')
	print(f'{total - 1} Emails Entered')
	print(f'{total - successful} Emails Failed')
	driver.get(setting['refLink'])
	driver.implicitly_wait(1)
	emailInput = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div[2]/form/input')
	# confirmButton = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div[2]/form/button')
	emailToUse = linecache.getline('emails.txt', total)
	emailInput.send_keys(emailToUse)
	time.sleep(4)
	# OK somehow I don't even need to click confirm and it subscribes me lmao.
	# Realized that the line was not stripped so the new line character sends enter key lol.
	#confirmButton.click()
	#time.sleep(5)
	fails = 0
	total += 1
	while True:
		try:
			driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/div/h2')
			successful += 1
			print("Success")
			break
		except Exception as e:
			print('Error')
			fails += 1
			if fails > 5:
				print("Error")
				break

	# NOT WORKING
	# Confirm Subscription
	#driver.get("https://www.morningbrew.com/daily/welcome?email=" + emailToUse.strip('\n'))
	#time.sleep(3)

	driver.quit()

for i in range(int(setting['count'])):
	run()

# Delete Unused Lines
g = open('emails.txt', "r")
emailAddresses = g.readlines()
g.close()

keptAddresses = emailAddresses[setting['count']:]

g = open('emails.txt', "w")
keptAddresses = ''.join(keptAddresses)
g.write(keptAddresses)
g.close()


os.system('clear')
print("Finished")
print("Lines Removed")
print(f"Check Your Email to Confirm {successful - 1} Emails")
print(f"{total - successful} Emails Failed")
