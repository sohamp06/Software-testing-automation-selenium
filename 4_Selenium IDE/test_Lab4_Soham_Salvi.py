# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestLab4():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_lab4(self):
        self.driver.get("https://www.calculator.net/body-fat-calculator.html")
        self.driver.set_window_size(1295, 767)
        element = self.driver.find_element(By.NAME, "cage")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.NAME, "cage")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.NAME, "cage")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.NAME, "cage").click()
        self.driver.find_element(By.CSS_SELECTOR, ".cbcontainer:nth-child(2)").click()
        self.driver.find_element(By.NAME, "cage").click()
        self.driver.find_element(By.NAME, "cage").send_keys("40")
        self.driver.find_element(By.NAME, "cweightkgs").send_keys("100")
        self.driver.find_element(By.ID, "cheightmeter").send_keys("189")
        self.driver.find_element(By.ID, "cneckmeter").send_keys("57")
        self.driver.find_element(By.ID, "cwaistmeter").send_keys("98")
        self.driver.find_element(By.ID, "chipmeter").send_keys("100")
        self.driver.find_element(By.CSS_SELECTOR, "table:nth-child(4) input").click()
        self.driver.find_element(By.CSS_SELECTOR, ".cbcontainer:nth-child(1) > .rbmark").click()
        self.driver.find_element(By.NAME, "cage").click()
        self.driver.find_element(By.NAME, "cage").click()
        self.driver.find_element(By.NAME, "cage").send_keys("15")
        self.driver.find_element(By.NAME, "cweightkgs").send_keys("220")
        self.driver.find_element(By.ID, "cheightmeter").send_keys("90")
        self.driver.find_element(By.ID, "cneckmeter").send_keys("18")
        self.driver.find_element(By.ID, "cwaistmeter").send_keys("100")
        self.driver.find_element(By.CSS_SELECTOR, "table:nth-child(4) input").click()
        self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(7)").click()

