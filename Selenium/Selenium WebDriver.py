from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome WebDriver automatically
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open a webpage
driver.get("https://google.com")

# Find elements and interact (Example: click a link)
link = driver.find_element(By.LINK_TEXT, "More information...")
link.click()

# Wait for a few seconds
time.sleep(5)

# Close the browser
driver.quit()
