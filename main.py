#Lets have some fun!

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import random

chrome_options = Options()
chrome_options.add_argument('--log-level=3')
chrome_options.add_argument(r"--user-data-dir=C:\Users\etfri\AppData\Local\Temp\scoped_dir22500_1595245904")
site = webdriver.Chrome(executable_path=r"chromedriver.exe", options=chrome_options)

class Fun:
    def __init__(self):
        self.streamer = str(input("What streamer chat would you like to type in?\n> "))
        site.get('https://www.twitch.tv/' + self.streamer)
        if input("Is the streamer offline? (y/n)\n> ").lower() == "y":
            site.find_element_by_link_text("Chat").click()  
        self.chat = site.find_elements_by_tag_name('textarea')[0]


    def pyramid(self):
        if input("Doing this will spam the chat, are you sure you would like to proceed? (y/n)\n> ") == 'y':
            delay = input("Are you VIP/Mod/Broadcaster? (y/n)\n> ")
            length = int(input("How tall would you like your pyramid? (Put Integer)\n> "))
            text = str(input("What would you like to pyramid? (emote preferred)\n> "))
            if delay == 'y':
                for i in range(1,length+1):
                    self.chat.send_keys(i*(" "+ text))
                    self.chat.send_keys(Keys.RETURN)
                for i in range(length-1,0,-1):
                    self.chat.send_keys(i*(" "+ text))
                    self.chat.send_keys(Keys.RETURN)
            if delay == 'n':
                for i in range(1,length+1):
                    self.chat.send_keys(i*(" "+ text))
                    self.chat.send_keys(Keys.RETURN)
                    time.sleep(round(random.uniform(1,1.3),2)) 
                for i in range(length-1,0,-1):
                    self.chat.send_keys(i*(" "+ text))
                    self.chat.send_keys(Keys.RETURN)
                    time.sleep(round(random.uniform(1,1.3),2)) 
            

        else:
            print("No longer auto-pyramiding...")

    def test(self):
        test_text = input("Input text to send\n> ")
        self.chat.send_keys(test_text)
        self.chat.send_keys(Keys.RETURN)
        print("Sent the test!")

funchat = Fun()
while True:
    do = input("What would you like to do? [p (pyramid),test,quit]\n> ").lower()
    if do == 'p':
        funchat.pyramid()
    elif do == 'test':
        funchat.test()
    elif do == 'quit':
        site.quit()
        break
    else: print("Please input a valid option...")
        






