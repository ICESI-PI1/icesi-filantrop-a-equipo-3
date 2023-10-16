from django.test import LiveServerTestCase
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select


class TestCreateStudent(LiveServerTestCase):

    def test_create_student(self):
        driver = webdriver.Chrome()
        driver.get('https://msde.azurewebsites.net/accounts/login/?next=/')
        time.sleep(2)
        username_input = driver.find_element(By.XPATH,
                                             '/html/body/section/div/div/div/div/div/div[1]/div/form/div[1]/label[2]/input')
        username_input.send_keys('juan')
        password_input = driver.find_element(By.XPATH,
                                             '/html/body/section/div/div/div/div/div/div[1]/div/form/div[2]/label[2]/input')
        password_input.send_keys('123')
        driver.find_element(By.XPATH, '/html/body/section/div/div/div/div/div/div[1]/div/form/div[3]/button').click()

        time.sleep(1)

        driver.find_element(By.XPATH, '//*[@id="menu"]/li[2]/a').click()

        driver.find_element(By.XPATH, '/html/body/div[2]/main/section/article/div/div[1]/div/a/button').click()

        driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div[2]/a').click()

        student_code = driver.find_element(By.XPATH, '//*[@id="id_student_code"]')
        student_code.send_keys('A00381190')

        student_name = driver.find_element(By.XPATH, '//*[@id="id_student_name"]')
        student_name.send_keys('Esto es una prueba')

        student_surname = driver.find_element(By.XPATH, '//*[@id="id_student_surname"]')
        student_surname.send_keys('end-to-end')

        student_birth_date = driver.find_element(By.XPATH, '//*[@id="id_student_birth_date"]')
        student_birth_date.send_keys('2020-04-07')

        student_id = driver.find_element(By.XPATH, '//*[@id="id_student_id"]')
        student_id.send_keys('123456')

        student_mail = driver.find_element(By.XPATH, '//*[@id="id_student_email"]')
        student_mail.send_keys('selenium@hotla.com')

        student_phone = driver.find_element(By.XPATH, '//*[@id="id_student_phone_number"]')
        student_phone.send_keys('3233994830')

        icfes = driver.find_element(By.XPATH, '//*[@id="id_student_ICFES_score"]')
        icfes.send_keys(456)

        donor = driver.find_element(By.XPATH, '//*[@id="id_donor_student_code"]')
        select = Select(donor)
        select.select_by_value('1')

        driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[1]/form/div/button').submit()
        text = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div[1]/h1')
        assert 'Estudiantes' in text.text

    def test_delete_student(self):
        driver = webdriver.Chrome()
        driver.get('https://msde.azurewebsites.net/student/A00381190/student_detail')
        time.sleep(2)

        driver.find_element(By.XPATH, '/html/body/div[2]/section/div/div/div[1]/div[1]/div/div/a[2]/button').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[2]/form/a/button').click()
        text = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div[1]/h1')

        assert 'Estudiantes' in text.text
