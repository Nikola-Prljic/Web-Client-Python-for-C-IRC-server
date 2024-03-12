from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def basic_test():
    driver = webdriver.Firefox()
    driver.get("http://localhost:5000")
    input_field = driver.find_element("id", "messageInput")
    assert input_field is not None

    input_field.send_keys("hello")
    input_field.send_keys(Keys.RETURN)
    time.sleep(2)
    driver.quit()

if __name__ == "__main__":
    basic_test()
    assert True
