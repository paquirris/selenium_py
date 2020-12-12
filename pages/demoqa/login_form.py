"""Abstract logic to control practice form"""
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.demoqa.confirmation_form import ConfirmationForm

class LoginForm(BasePage):

    __URL = 'https://demoqa.com/login'

    __LOGIN_LOC = (By.ID, 'login')

    __USERNAME_LOC = (By.ID, 'userName')

    __PASSWORD_LOC = (By.ID, 'password')


    def __init__(self, driver: WebDriver, timeout: int = 10):
        super().__init__(driver, timeout, self.__URL)

    def wait_until_loaded(self):
        self._wait.until(EC.visibility_of_element_located(self.__LOGIN_LOC))

    def get_username(self):
        """Username"""
        return self.__get_input_value(self.__USERNAME_LOC)

    def set_username(self, value):
        """Add a username"""
        self.__set_input_value(self.__USERNAME_LOC, value)

    def get_password(self):
        return self.__get_input_value(self.__PASSWORD_LOC)

    def set_password(self, value):
        self.__set_input_value(self.__PASSWORD_LOC, value)

    def login(self):
        element = self._wait.until(EC.element_to_be_clickable(self.__LOGIN_LOC))
        element.click()

    def __get_input_value(self, locator):
        element = self._wait.until(EC.element_to_be_clickable(locator))
        return element.get_attribute('value')

    def __set_input_value(self, locator, value):
        element = self._wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(value)




