from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:/Users/Naman/chromedriver.exe')
driver.get("https://www.ajio.com/s/fresh-arrivals-women-clothing")
headlines = driver.find_element(By.className("item rilrtl-products-list__item item"))
for headline in headlines:
    print(headline.text.strip())
driver.close()
