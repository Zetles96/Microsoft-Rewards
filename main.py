from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import random
from nltk.corpus import words
import time


def main():
    word_list = words.words()
    print(len(word_list))
    service = Service(executable_path=".\edgedriver_win32\msedgedriver.exe")
    driver = webdriver.Edge(service=service)
    driver.get("https://www.bing.com/")
    for i in range(random.randint(30, 40)):
        search_box = driver.find_element(by=By.ID, value="sb_form_q")
        search_box.clear()
        search_box.send_keys(random.choice(word_list), Keys.ENTER)
        time.sleep(random.randint(5, 15))
    input()


if __name__ == '__main__':
    main()
