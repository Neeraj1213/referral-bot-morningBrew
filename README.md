# MorningBrew-Referral-Bot

[Github](https://github.com/i0Z3R0/MorningBrew-Referral-Bot)

# Table of Contents
- [Table of Contents](#table-of-contents)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Setup for Idiots](#setup-for-idiots)
- [About](#about)
- [Overview of Features](#overview-of-features)
- [Detailed Overview](#detailed-overview)

# Prerequisites
- Latest version of Python3
- Latest version of Pip
- Text editor to change some settings
- Google account (Gmail)

# Installation
1. git clone https://github.com/i0Z3R0/MorningBrew-Referral-Bot.git
2. cd MorningBrew-Referral-Bot
3. pip3.9 install -r requirements.txt
4. Configure settings in settings.json (more info at very bottom of this file)
5. python3 main.py
6. python3 confirm.py
#### Note: ChromeDriver is NOT required, webdriver_manager will automatically download the matching version of ChromeDriver for your OS.

# Setup for Idiots

# About
This is a single-purpose bot to gain you a lot of referrals on Morning Brew. When you get enough referrals, it can be exchanged for free merchandise from Morning Brew, including notebooks, water bottles, shirts, and more.

The program uses ChromeDriver and Selenium to automate the action of gaining referrals. It exploits the "Gmail Dot Trick" to generate tons of email addresses that Morning Brew thinks are different, but are all sent to your single inbox.

# Overview of Features
- Generates email addresses using your main address
- Automatically subscribes using your referral URL and generated addresses
- Detects if the subscription was successful
- Automatically confirms subscriptions for the referrals to count (confirm.py)

# Detailed Overview

### **Overview**
This program was created for one and only one purpose: Farm tons of referrals on Morning Brew. Morning Brew is a daily newsletter that covers all sorts of the latest business-related news. Morning Brew has a referral program as well. For certain referral milestones (3, 5, 10, 15, 25, 50, 100, 1000), you will receive Morning Brew swag such as shirts, notebooks, mugs, and more. By adding a dot at random places in your Gmail address, Morning Brew is tricked into thinking those are different addresses, when in reality all of those emails will be sent to you.

### **Detailed Breakdown**
The program needs your referral URL, email address, and a few configured options to run. It can be run for theoretically forever, until you run out of generated email addresses. A total of 2^(x-1)^ emails can be generated for any address, X being the number of characters in your email address (excluding @gmail.com or the domain).

By automating certain mouse clicks and keyboard presses using Selenium and Chromedriver, tons of confirmation emails from Morning Brew are sent to your one inbox. If the box does not detect the message that shows up after you have entered your email, it assumes an error has occured and will log that in the output. After the specified number of emails are generated (see next section for configuration), the program will delete that number of lines from emails.txt so the same address is not used twice (which would cause an error).
The second program, confirm.py will then go through each email and confirm all the subscriptions so the referrals actually count.

Note: main.py uses Selenium and can / is encouraged to be run in headless mode, allowing you to use your computer to do other things. On the other hand, confirm.py will use pyautogui to simulate key presses and mouse clicks, so you can't do anything with your computer as you wait for the emails to all be confirmed. I have not tested running both programs simultaneously, as that may cause some problems with confirming the emails.

### **Settings**
- **Referral Link** - String (Line 2): Your referral URL found at the bottom of every Morning Brew newsletter you receive (e.g.: https://www.morningbrew.com/daily/r?kid=3395db04)
- **Base Email** - String (Line 3): The email you wish all the confirmation emails to be sent to, and the "fake" emails are generated using this.
- **Count** - Integer (Line 4): The number of emails / referrals you want to generate. The reason why this is here is because anything over 1000 is generally useless.
- **Headless Mode** - Boolean (Line 5): Headless mode is highly recommended and on by default. It allows for better performance and lets you do other things on your computer as the program will run in the background.
- **Generate** - Boolean (Line 6): Chooses whether or not to generate email addresses. Change this to true every time you enter a new base email and want to generate new addresses (Note: generated emails will overwrite the current list of emails).
