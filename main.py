from selenium import webdriver
from selenium.webdriver.edge.service import Service


def main():
    service = Service(executable_path=".\edgedriver_win32\msedgedriver.exe")
    driver = webdriver.Edge(service=service)
    driver.get("https://www.bing.com/")
    input()
    pass


if __name__ == '__main__':
    main()
