from django.test import LiveServerTestCase
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select


class TestCreateReport(LiveServerTestCase):

    def test_create_report(self):
        driver = webdriver.Chrome()
        driver.get('https://msde.azurewebsites.net/accounts/login/?next=/')
        time.sleep(3)
        # Inicia sesión en el sitio web
        username_input = driver.find_element(By.XPATH,'/html/body/section/div/div/div/div/div/div[1]/div/form/div[1]/label[2]/input')
        username_input.send_keys('filantropia')
        password_input = driver.find_element(By.XPATH,
                                             '/html/body/section/div/div/div/div/div/div[1]/div/form/div[2]/label[2]/input')
        password_input.send_keys('123')

        password_input.submit()

        time.sleep(2)

        driver.find_element(By.XPATH, '/html/body/div[1]/div/ul/li[3]/a').click()
        driver.find_element(By.XPATH, '/html/body/div[2]/main/section[1]/form/select').click()
        driver.find_element(By.XPATH, '/html/body/div[2]/main/section[1]/form/select/option[2]').click()
        driver.find_element(By.XPATH, '/html/body/div[2]/main/section[1]/form/select/option[2]').click()
        code = driver.find_element(By.XPATH, '/html/body/div[2]/main/section[1]/form/input')
        code.send_keys('A00381190')

        time.sleep(3)

        driver.find_element(By.XPATH, '/html/body/div[2]/main/section[1]/div/div/div/div[2]/form/div/button[2]')
