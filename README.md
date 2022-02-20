# MorningBrew-Referral-Bot

This is a single-purpose bot to gain you a lot of referrals on Morning Brew. When you get enough referrals, it can be exchanged for free merchandise from Morning Brew, including notebooks, water bottles, shorts, and more.

This program uses ChromeDriver and Selenium to automate the action of gaining referrals. It exploits the "Gmail Dot Trick" to generate tons of email addresses that Morning Brew thinks are different, but are all sent to your single inbox.

Currently, the program needs your referral URL, email address, and a few configured options to run. It can be run for theoretically forever, until you run out of generated email addresses.

There is another file, confirm.py which will confirm all the subscriptions so the referrals actually count. 

Configuration
refLink: The referral URL found at the bottom of every Morning Brew newsletter you receive.
baseEmail: The email you wish for all confirmation emails to be sent to (Note: I highly highly HIGHLY recommend creating a separate Gmail account for this automation only, as you will receive too many emails to keep track and will continuously receive tons and tons of emails.
count: The number of emails to sign up. This option is here because running the program infinitely would not be very productive, as it would clog up the inbox and take forever to confirm all the emails. I personally set this to around 15-30, then manually confirm all the emails before running again.
headlessMode: Whether or not the program runs in headless mode. Headless mode means the browser is hidden and you cannot interact with it, but the program will run faster. If headless mode is off, your computer will constantly switch to the new Chrome window. I highly highly recommend keeping headless mode on, there's no reason to turn it off unless you are constantly experiencing errors.
generate: Change this to true on the first run, it will generate a text file "emails.txt" with all variations of the base email specified earlier. Setting will automatically change to false after you run it.
