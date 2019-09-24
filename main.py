from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import setting
import time
import sys

# Set up chrome and navigate to website
try:
    driver = webdriver.Chrome(setting.PATH_TO_CHROMEDRIVER)
except:
    raise Exception("Path to selenium chrome driver not found.")
    sys.exit()

driver.get("https://dictionary.com")

# Enter word in the search bar
word = "selenium"
search_box = driver.find_element_by_xpath("//input[@title='Search']")
search_box.send_keys(word)
search_box.send_keys(Keys.ENTER)

# Grab the audio and text element
word_box_xpath = "//h1[text()='#']//ancestor::div[@class='css-7ac8yh e16867sm0']".replace("#", word)
word_box = driver.find_element_by_xpath(word_box_xpath)

word_audio = word_box.find_element_by_xpath(".//span[@data-ci-target='audio']")
word_definition = word_box.find_element_by_xpath(".//span[@class='one-click-content css-1p89gle e1q3nk1v4']")

# Click audio
time.sleep(2)
word_audio.click()

# Extract text
print(word)
print(word_definition.text)
