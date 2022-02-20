import time
import string
import os
import pyautogui

# J switches to the next email in the list, going older
# (700, 580) is my position for confirm button

try:
	totalEmails = int(input('How many emails do you have to confirm? '))
except Exception as e:
	if "invalid literal for int() with base 10" in str(e):
		print("Invalid Number!")
	else:
		print("Error: " + str(e))
	os._exit(1)

os.system('clear')
# Note: Say you have 20 unread emails that are from Morning Brew to confirm your subscription.
# Click on the first email at the very top.
# Enter the number 20 here, not 19. Even though your inbox shows 19 unread now, enter 20 please.

# IMPORTANT: TURN OFF CONVERSATION VIEW IN THE SETTINGS

input("Press enter after you have navigated to the first email\nAutomation will start 5 seconds after you press enter")
time.sleep(5)
pyautogui.moveTo(700, 580, duration=0.25)
time.sleep(1)
for i in range(totalEmails):
	time.sleep(0.2)
	print("CLICKING ON LINK")
	pyautogui.click()
	time.sleep(1.25)
	print("CLOSING TAB")
	pyautogui.hotkey('command', 'w')
	time.sleep(0.8)
	print("PRESSING KEY J")
	pyautogui.press('j')
