from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://google.com")
print(driver.current_url)

google_search_box=driver.find_element(By.NAME,"q")
google_search_box.send_keys("apple"+Keys.ENTER)

expected_title_begin_with="apple"
actual_title=driver.title

if actual_title.startswith(expected_title_begin_with):
    print("SUCCESS")
else:
    print("FAILURE")
