from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver

class TestCreateStudent(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        self.selenium.get('http://127.0.0.1:8000/accounts/login/?next=/')
        username_input = self.selenium.find_element(By.XPATH, '/html/body/section/div/div/div/div/div/div[1]/div/form/div[1]/label[2]/input')
        username_input.send_keys('juan')

        password_input = self.selenium.find_element(By.XPATH, '/html/body/section/div/div/div/div/div/div[1]/div/form/div[2]/label[2]/input')
        password_input.send_keys('123')

        self.selenium.find_element(By.XPATH, '/html/body/section/div/div/div/div/div/div[1]/div/form/div[3]/button').click()



