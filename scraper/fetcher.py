import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

HEADERS = {"User-Agent": "Mozilla/5.0"}

def fetch_static(url):
    try:
        res = requests.get(url, headers=HEADERS, timeout=10)
        res.raise_for_status()
        return res.text
    except Exception as e:
        print("Static fetch error:", e)
        return None

def fetch_static_screenshot(url):
    """Capture screenshot of static page using Selenium"""
    try:
        options = Options()
        options.add_argument("--headless")
        
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        time.sleep(3)
        
        # Set window size to match content
        total_width = driver.execute_script("return document.body.offsetWidth")
        total_height = driver.execute_script("return document.body.parentNode.scrollHeight")
        driver.set_window_size(total_width, total_height)
        time.sleep(2)
        
        import os
        os.makedirs("output", exist_ok=True)
        driver.save_screenshot("output/page.png")
        driver.quit()
        print("✓ Screenshot saved: output/page.png")
    except Exception as e:
        print("Screenshot capture error:", e)

def fetch_dynamic(url, username=None, password=None):
    options = Options()
    options.add_argument("--headless")

    try:
        driver = webdriver.Chrome(options=options)
        
        driver.get(url)
        
        # Simple login if credentials provided (basic form detection)
        if username and password:
            try:
                # Try to find login form
                username_field = driver.find_element("name", "username") or driver.find_element("name", "email") or driver.find_element("name", "user")
                password_field = driver.find_element("name", "password")
                login_button = driver.find_element("xpath", "//input[@type='submit']") or driver.find_element("xpath", "//button[@type='submit']")
                
                username_field.send_keys(username)
                password_field.send_keys(password)
                login_button.click()
                time.sleep(3)  # Wait for login
            except:
                print("Login form not found or login failed")
        
        # Wait for page to be fully loaded and animations to settle
        time.sleep(5)
        
        # Set window size to match content for better screenshot
        total_width = driver.execute_script("return document.body.offsetWidth")
        total_height = driver.execute_script("return document.body.parentNode.scrollHeight")
        driver.set_window_size(total_width, total_height)
        time.sleep(2)

        html = driver.page_source
        import os
        os.makedirs("output", exist_ok=True)
        driver.save_screenshot("output/page.png")
        print("✓ Screenshot saved: output/page.png")
        driver.quit()

        return html
    except Exception as e:
        print("Dynamic fetch error:", e)
        try:
            driver.quit()
        except:
            pass
        return None