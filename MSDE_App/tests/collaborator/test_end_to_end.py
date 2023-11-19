from django.test import LiveServerTestCase
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select


class TestCreateCollaborator(LiveServerTestCase):

    def test_create_philanthropy_member(self):
        driver = webdriver.Chrome()
        driver.get('https://msde.azurewebsites.net/accounts/login/?next=/')
        time.sleep(3)
        # Inicia sesión en el sitio web
        username_input = driver.find_element(By.XPATH,
                                             '/html/body/section/div/div/div/div/div/div[1]/div/form/div[1]/label[2]/input')
        username_input.send_keys('colaborador')
        password_input = driver.find_element(By.XPATH,
                                             '/html/body/section/div/div/div/div/div/div[1]/div/form/div[2]/label[2]/input')
        password_input.send_keys('123')

        password_input.submit()

        time.sleep(2)

        # Realiza una serie de clics en enlaces y botones en el sitio web

        driver.find_element(By.XPATH, '/html/body/div[1]/div/ul/li[3]/a').click()

        driver.find_element(By.XPATH, '/html/body/div[2]/main/section[2]/article/div/a').click()

        collaboratorCode = driver.find_element(By.XPATH, '//*[@id="id_collaborator_code"]')
        collaboratorCode.send_keys("A003819673")

        collaboratorName = driver.find_element(By.XPATH, '//*[@id="id_collaborator_name"]')
        collaboratorName.send_keys("Victor Manuel Garzon")
        driver.find_element(By.XPATH, '//*[@id="id_collaborator_email"]')
        collaboratorEmail = driver.find_element(By.XPATH, '//*[@id="id_collaborator_email"]')
        collaboratorEmail.send_keys("panterro9212@gmail.com")

        time.sleep(4)

        driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/form/button').click()

        time.sleep(2)

        username = driver.find_element(By.XPATH, '/html/body/div[2]/form/p[1]/input')
        username.send_keys("Victor9043")
        password1 = driver.find_element(By.XPATH, '/html/body/div[2]/form/p[3]/input')
        password1.send_keys("Victor9043_")
        password2 = driver.find_element(By.XPATH, '/html/body/div[2]/form/p[5]/input')
        password2.send_keys("Victor9043_")

        driver.find_element(By.XPATH, '/html/body/div[2]/form/a/button').submit()

        time.sleep(2)






