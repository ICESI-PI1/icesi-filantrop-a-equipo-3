from django.test import LiveServerTestCase
from selenium.webdriver.common.by import By
from selenium import webdriver

class TestLogin(LiveServerTestCase):

    def test_login(self):
        driver = webdriver.Chrome()
        driver.get('https://msde.azurewebsites.net/accounts/login/?next=/')
        username_input = driver.find_element(By.XPATH, '/html/body/section/div/div/div/div/div/div[1]/div/form/div[1]/label[2]/input')
        username_input.send_keys('juan')

        password_input = driver.find_element(By.XPATH, '/html/body/section/div/div/div/div/div/div[1]/div/form/div[2]/label[2]/input')
        password_input.send_keys('123')

        driver.find_element(By.XPATH, '/html/body/section/div/div/div/div/div/div[1]/div/form/div[3]/button').click()

        assert "Base" in driver.title