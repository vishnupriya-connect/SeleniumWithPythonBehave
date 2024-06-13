import logging
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def open_browser():
    serv_obj = Service(r'C:\Users\rihaa\Documents\Drivers\chromedriver.exe')
    driver = webdriver.Chrome(service=serv_obj)
    logging.info("Browser opened")
    return driver


def maximize_browser(driver):
    driver.maximize_window()
    logging.info("Browser maximized")

def take_screen_shot():
    pass

def open_url(driver, url):
    driver.get(url)
    logging.info("Opened %s" % url)


def sleep(seconds):
    time.sleep(seconds)
    logging.info("Sleep for %s Seconds" % seconds)


def close_browser(driver):
    driver.quit()
    logging.info("Browser closed")


def find_element_by_id(driver, id):
    element = driver.find_element(By.ID,id)
    return element


def send_keys(element,text):
    element.send_keys(text)


def click(element):
    element.click()


def clear(element):
    element.clear()

