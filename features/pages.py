from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class PageAccueilDuckDuckGo:
    def __init__(self, driver):
        self.driver = driver

    def rechercher(self, texte):
        search_box = self.driver.find_element(By.ID, "searchbox_input")
        search_box.send_keys(texte)
        search_box.send_keys(Keys.RETURN)