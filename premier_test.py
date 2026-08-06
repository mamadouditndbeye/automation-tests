from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Ouvre un navigateur Chrome automatiquement
driver = webdriver.Chrome()

# Va sur Google
driver.get("https://duckduckgo.com")

# Attend 2 secondes pour voir la page se charger
time.sleep(2)

# Trouve la barre de recherche et tape du texte
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("automatisation de tests QA")

# Attend 3 secondes pour voir le résultat
time.sleep(3)

# Ferme le navigateur
driver.quit()

print("Test terminé avec succès !")