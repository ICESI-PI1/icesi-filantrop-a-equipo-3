from django.test import LiveServerTestCase
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select


class TestEndToEnd(LiveServerTestCase):

    def test_create_alert(self):
        # Login
        driver = webdriver.Chrome()
        driver.get('https://msde.azurewebsites.net/accounts/login/?next=/')
        time.sleep(3)
        # Username Input
        username_input = driver.find_element(By.XPATH,
                                             '/html/body/section/div/div/div/div/div/div[1]/div/form/div[1]/label[2]/input')
        username_input.send_keys('juan')

        # Password input
        password_input = driver.find_element(By.XPATH,
                                             '/html/body/section/div/div/div/div/div/div[1]/div/form/div[2]/label[2]/input')
        password_input.send_keys('123')

        password_input.submit()

        time.sleep(2)

        # Drive through app

        driver.find_element(By.XPATH, '//*[@id="menu"]/li[2]/a').click()

        # Click en el botón de info estudiantes
        driver.find_element(By.XPATH, '/html/body/div[2]/main/section/article/div/div[1]/div/a/button').click()

        # Scroll down
        driver.execute_script("window.scrollTo(900,document.body.scrollHeight)")

        time.sleep(1)

        # click en el estudiante para crear la alerta
        driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div[6]/div/a[1]').click()

        # Click botón de alerta

        driver.find_element(By.XPATH, '/html/body/div[2]/section/div/div/div[1]/div[2]/div/div/a/button').click()

        # Descripcón de alerta

        text_area=driver.find_element(By.XPATH, '//*[@id="id_alert_description"]')

        text_area.send_keys('Sus calificaciones están bajando y le pegó a un profesor')

        # Alert Sender

        alert_sender = driver.find_element(By.XPATH,'//*[@id="id_alert_sender"]')

        alert_sender.send_keys('Diana Romero')

        # Scroll down
        driver.execute_script("window.scrollTo(500,document.body.scrollHeight)")
        time.sleep(3)

        # Type Alert

        type = driver.find_element(By.XPATH, '//*[@id="id_type_alert"]')
        select = Select(type)
        select.select_by_index(2)

        # Botón de save

        driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[1]/div[2]/div/form/button').click()




