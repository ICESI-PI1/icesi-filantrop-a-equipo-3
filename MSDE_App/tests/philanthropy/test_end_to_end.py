from django.test import LiveServerTestCase
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select


class TestCreatePhilanthropy(LiveServerTestCase):

    def test_create_philanthropy_member(self):
        driver = webdriver.Chrome()
        driver.get('https://msde.azurewebsites.net/accounts/login/?next=/')
        time.sleep(3)
        # Inicia sesión en el sitio web
        username_input = driver.find_element(By.XPATH,
                                             '/html/body/section/div/div/div/div/div/div[1]/div/form/div[1]/label[2]/input')
        username_input.send_keys('juan')
        password_input = driver.find_element(By.XPATH,
                                             '/html/body/section/div/div/div/div/div/div[1]/div/form/div[2]/label[2]/input')
        password_input.send_keys('123')

        password_input.submit()

        time.sleep(2)

        # Realiza una serie de clics en enlaces y botones en el sitio web
        driver.find_element(By.XPATH, '//*[@id="menu"]/li[2]/a').click()

        driver.find_element(By.XPATH, '/html/body/div[2]/main/section/article/div/div[3]/div/a/button').click()

        driver.find_element(By.XPATH, '/html/body/div[2]/main/section[1]/article/div/div/a').click()

        memberCode = driver.find_element(By.XPATH, '//*[@id="id_philanthropy_member_code"]')
        memberCode.send_keys("A003819673")

        memberName = driver.find_element(By.XPATH, '//*[@id="id_philanthropy_member_name"]')
        memberName.send_keys("Victor Manuel Garzon")
        driver.find_element(By.XPATH, '//*[@id="id_philanthropy_member_email"]')
        memberEmail = driver.find_element(By.XPATH, '//*[@id="id_philanthropy_member_email"]')
        memberEmail.clear()
        memberEmail.send_keys("panterro9212@gmail.com")

        time.sleep(4)

        driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/form/button').click()

        time.sleep(2)

        username = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/form/p[1]/input')
        username.send_keys("Victor9043")
        password1 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/form/p[3]/input')
        password1.send_keys("Victor9043_")
        password2 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/form/p[5]/input')
        password2.send_keys("Victor9043_")

        driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/form/div/a/button').submit()

        time.sleep(2)

    def test_delete_philanhropy(self):
        driver = webdriver.Chrome()
        driver.get('https://msde.azurewebsites.net/fil/student/A00381190/student_detail')
        time.sleep(2)

        driver.find_element(By.XPATH, '/html/body/div[2]/section/div/div/div[1]/div[1]/div/div/a[2]/button').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[2]/form/a/button').click()




