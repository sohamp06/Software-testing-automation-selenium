# Group No.: 11
# Members: Salvi Patel, Soham Patel, Dawa Sherpa
# Date: July 26, 2023
# Description: Selecting a product from a website with selenium
# File name: Lab5_salvi_soham_dawa.py
import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class ChromeDriverManager:
    def install(self):
        pass


class MagentoTestCase(unittest.TestCase):
    browser = None

    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome(ChromeDriverManager().install())
        cls.browser.maximize_window()

    def open_Website(self):
        self.browser.get('https://magento.softwaretestingboard.com/')

    def test_select_Product(self):
        self.open_Website()
        time.sleep(1)
        women = self.browser.find_element(By.ID, "ui-id-4")
        action = ActionChains(self.browser)
        action.move_to_element(women).perform()
        time.sleep(1)

        tops = self.browser.find_element(By.ID, "ui-id-9")
        action.move_to_element(tops).perform()
        time.sleep(1)

        hoodies = self.browser.find_element(By.ID, "ui-id-12")
        hoodies.click()
        time.sleep(1)

        self.browser.find_element(By.XPATH, "/html/body/div[1]/main/div[3]/div[2]/div/div[2]/div/div[1]/div[1]").click()
        time.sleep(2)
        self.browser.find_element(By.XPATH, "/html/body/div[1]/main/div[3]/div[2]/div/div[2]/div/div[1]/div[2]/ol/li[3]/a").click()
        time.sleep(2)
        self.browser.find_element(By.XPATH, "/html/body/div[1]/main/div[3]/div[2]/div/div[2]/div/div[2]/div[1]").click()
        time.sleep(1)
        self.browser.get("https://magento.softwaretestingboard.com/eos-v-neck-hoodie.html")
        time.sleep(1)
        self.browser.find_element(By.ID, "option-label-size-143-item-166").click()
        time.sleep(2)
        self.browser.find_element(By.ID, "option-label-color-93-item-50").click()
        time.sleep(2)
        self.browser.find_element(By.ID, "product-addtocart-button").click()
        time.sleep(2)
        self.browser.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div[1]/a").click()
        time.sleep(1)
        self.browser.find_element(By.XPATH, "//*[@id='top-cart-btn-checkout']").click()
        time.sleep(2)
        self.browser.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div[2]/aside/div[2]/div/div/div[1]/div/div[1]").click()
        time.sleep(1)
        self.browser.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div[2]/aside/div[2]/div/div/div[1]/div/div[2]/div/ol/li/div/div/div[2]").click()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()


if __name__ == "__main__":
    unittest.main()
