from appium import webdriver
from appium.options.common import AppiumOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import Fore, Style
import cloudscraper
import json
import os
import colorama
import time
import random
import subprocess
import threading
import pytesseract
from PIL import Image
import sys
import cv2
import requests
from selenium import webdriver as selenium_webdriver
import undetected_chromedriver
import multiprocessing

colorama.init()
scraper = cloudscraper.create_scraper()
prices = 0

# make color for logs
def error_color(string: str):
    return colorama.Fore.RED + str(string) + colorama.Style.RESET_ALL
def success_color(string: str):
    return colorama.Fore.GREEN + str(string) + colorama.Style.RESET_ALL
def system_color(string: str):
    return colorama.Fore.YELLOW + str(string) + colorama.Style.RESET_ALL
def wait_color(string: str):
    return colorama.Fore.BLUE + str(string) + colorama.Style.RESET_ALL
def purple_color(string: str):
    return colorama.Fore.MAGENTA + str(string) + colorama.Style.RESET_ALL


capabilities = {
  "udid": "192.168.1.249:5555",
  "platformName": "Android",
  "noReset": True
}

def driver_init(adb_path, ask_udid=True, device_id=None, appium_port=None):
    for retry in range(5):
        try:
            requests.get("https://www.google.com/", timeout=2)
            break
        except:
            time.sleep(1)
            continue
    else:
        input("[!] Lỗi mạng >>> ")

    appium_server_url = f"http://localhost:{appium_port}/wd/hub"

    if ask_udid:
        os.system(adb_path + " devices")
        udid_inp = input(system_color("[?] Nhập vào udid máy của bạn\n-> "))
        capabilities['udid'] = udid_inp

    elif device_id is not None:
        capabilities['udid'] = device_id
    
    error = False
    while True:
        try:

            if len(capabilities['udid'].split(".")) >= 3 and error:
                os.system(adb_path + " connect " + capabilities['udid'])

            driver = webdriver.Remote(appium_server_url, options=AppiumOptions().load_capabilities(capabilities))            
            error = False
            break

        except Exception as e:
            # print(e)
            try:
                driver.quit()
            except:
                pass
            print(error_color(f"[Device: {device_id}] [!] Lỗi khi tạo driver, thử lại..."))
            error = True
    
    return driver


def facebook_init(driver: webdriver.Remote, device_id):
    try:
        driver.terminate_app("com.facebook.lite")
        driver.activate_app("com.facebook.lite")
    except:
        pass
    print(system_color(f"[> {device_id}] đang check phiên có bị văng hay không..."))
    try:
        check_login_btn = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//android.view.View[@text='Log in']"))
        )
        check_login_btn.click()
        print(error_color(f"[! {device_id}] phát hiện phiên đã bị văng, login lại..."))
    except:
        print(system_color(f"[> {device_id}] không phát hiện phiên bị văng, tiếp tục..."))

def golike_init(driver: webdriver.Remote):
    try:
        driver.terminate_app("com.golike")
        driver.activate_app("com.golike")
    except:
        pass


# make waiting animation theme
def waiting_ui(timeout=5, text="", device_id=None):
    for i in range(1, timeout+1):
        print(colorama.Fore.YELLOW + f"\r[Device: {device_id}] [{i}s] " + colorama.Style.RESET_ALL, end="")
        print(colorama.Fore.BLUE + text + colorama.Style.RESET_ALL, end="")
        time.sleep(1)
    print()
    return 0