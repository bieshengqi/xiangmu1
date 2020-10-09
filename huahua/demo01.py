from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="chromedriver") 
driver.get("http://www.baidu.com")
time.sleep(3)
driver.maximize_window()
driver.find_element_by_id("kw").send_keys("四月是你的谎言")
time.sleep(3)
driver.find_element_by_id("su").click()
time.sleep(3)
text = driver.find_element_by_xpath("//*[@id=\"1\"]/h3/a").text
print(text)
time.sleep(3)
driver.find_element_by_xpath("//*[@id=\"1\"]/h3/a").click()
time.sleep(3)
driver.quit()

