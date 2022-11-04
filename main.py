from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import random
from selenium.webdriver.common.keys import Keys


def main():
    string_list = ["hej", "med", "dig", "du ", "er", "en", "bisse"]
    service = Service(executable_path=".\edgedriver_win32\msedgedriver.exe")
    driver = webdriver.Edge(service=service)
    driver.get("https://www.bing.com/")
    driver.implicitly_wait(0.5)
    for i in string_list:
        driver.find_element(by=By.ID, value="sb_form_q").send_keys(i, Keys.ENTER)
        driver.implicitly_wait(0.5)
    input()
    pass


if __name__ == '__main__':
    main()
