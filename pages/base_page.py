"""Parent page for all page object."""
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    """Abstraction for base page."""

    __BODY_LOCATOR = (By.TAG_NAME, 'body')

    def __init__(self, driver: WebDriver, timeout: int = 10, url: str = None):
        """Create a new base page instance

        :param driver: Web driver instance
        :param timeout: Explicit wait's time out in seconds
        :param url: Page's url
        """
        self._driver = driver
        self._timeout = timeout
        self._url = url
        self._wait = WebDriverWait(driver, timeout)
        self._window_handler = None

    def open(self):
        """Open the web page

        :return: None
        """
        self._driver.get(self._url)
        self._window_handler = self._driver.current_window_handle

    def move_to_main_tab(self):
        """Move back to main page tab"""
        self._driver.switch_to.window(self._window_handler)

    def close(self):
        """Close the web page

        :return: None
        """
        self._driver.close()

    def get_default_timeout(self) -> int:
        """Get wait default timeout

        :return: Timeout in seconds
        """
        return self._timeout

    def set_default_timeout(self, timeout: int):
        """Set default timeout for explicit waits

        :param timeout: Timeout in seconds
        :return: None
        """
        if type(timeout) == int:
            self._timeout = timeout
            self._wait = WebDriverWait(self._driver, self._timeout)
        else:
            raise ValueError(f'Invalid value for timeout: {timeout}')

    def refresh(self):
        """Refresh web page

        :return: None
        """
        self._driver.refresh()

    def wait_until_loaded(self):
        """Wait until body is loaded

        :return: None
        """
        self._wait.until(EC.visibility_of_element_located(self.__BODY_LOCATOR))

    def set_value_attribute(self, element, value):
        """ Set attribute value

        :param element: Web element to modify
        :param value: Value to set
        :return: None
        """
        self._driver.execute_script(f"arguments[0].value = '{value}'", element)
