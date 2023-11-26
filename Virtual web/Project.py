import os

os.system("pip install selenium==3.141.0")
from webbot import Browser
import time

driver = Browser()

driver.go_to(
    'https://chrome.google.com/webstore/detail/virtual-keyboard/pflmllfnnabikmfkkaddkoolinlfninn?hl=en'
)
time.sleep(5)
driver.go_to('google.com')

for i in range(5):
    time.sleep(0.5)
    driver.new_tab(url='https://google.com')

input("Service is running")
