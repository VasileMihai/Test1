from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from assertpy import soft_assertions, assert_that

driver= webdriver.Chrome()

driver.get("https://emag.ro")

searchBox = driver.find_element(By.ID,"searchboxTrigger")
searchBox.send_keys("mouse")
searchBox.send_keys(Keys.ENTER)

firstResult = driver.find_element(By.CLASS_NAME,"card-v2-thumb-inner")
firstResult.click()

with soft_assertions():
    assert_that(driver.title).contains("Mouse")

