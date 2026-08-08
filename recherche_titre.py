from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://duckduckgo.com")
time.sleep(2)

search_box = driver.find_element(By.ID, "searchbox_input")
search_box.send_keys("automatisation de tests QA")
search_box.send_keys(Keys.RETURN)

time.sleep(3)

# Vérification automatique du résultat
assert "automatisation de tests QA" in driver.title
print("✅ Le test a réussi : le titre contient bien la recherche")

driver.quit()