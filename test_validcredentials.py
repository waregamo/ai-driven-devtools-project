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

class TestValidcredentials():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_validcredentials(self):
    self.driver.get("https://academy.powerlearnprojectafrica.org/login")
    self.driver.set_window_size(1536, 816)
    self.driver.find_element(By.ID, "email").click()
    element = self.driver.find_element(By.ID, "email")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys("danjeff254@gmail.com")
    self.driver.find_element(By.CSS_SELECTOR, ".flex:nth-child(2) > .peer").click()
    self.driver.find_element(By.CSS_SELECTOR, ".flex-col:nth-child(2)").click()
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("3DJ4me254")
    self.driver.find_element(By.CSS_SELECTOR, ".inline-flex").click()
    # Wait for the login button to be clickable
    login_button = WebDriverWait(self.driver, 10).until(
        expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".inline-flex"))
    )
    login_button.click()
    
    # Take a screenshot before waiting for dashboard
    self.driver.save_screenshot("before_dashboard_check.png")
    
    # Wait for the dashboard to load
    WebDriverWait(self.driver, 10).until(
        expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "[role='banner']"))
    )
    
    # Take a screenshot to verify successful login
    self.driver.save_screenshot("valid_login_test_result.png")
    self.driver.quit()
