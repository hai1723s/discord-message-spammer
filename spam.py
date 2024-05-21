import requests
import time
import random  # Add this line to import the random module
import threading
import os
from function import *
from setting import *

os.system("color 4")
sleepo = "0"



time.sleep(0.1)
time.sleep(1)

def spam(token, channel_id, file_url):
    a = 0
    while True:
        a = a + 0.000000000000000001
        MESSAGE = RandomCWord() + "\n" + RandomChina(1000) + "\n" + RandomCWord()
        send_file_via_api(TOKEN, CHANNEL_ID, FILE_URL, MESSAGE)

for _ in range(5):
    threading.Thread(target=spam, args=(TOKEN, CHANNEL_ID, FILE_URL)).start()
