from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://127.0.0.1:8000/")
assert "http://127.0.0.1:8000/" in driver.title
