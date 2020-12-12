"""Represent calendar form from Expedia."""
from components.base_component import BaseComponent
from selenium import webdriver


class Move(BaseComponent):
    """Represent stay form from Expedia."""
    __ORIGIN_XPATH = "//*[@id='location-field-origin-input']"

    __DESTINATION_XPATH = "//*[@id='location-field-destination-input']"

    __OPT_XPATH = "//li/button"

    def __init__(self, driver: webdriver, root_locator: str, timeout: int = 10):
        super().__init__(driver, root_locator, timeout)

    def set_origin(self, value):
        """Set value of input"""
        self.__open()
        textbox = self.get_descendant_element(self.__ORIGIN_XPATH)
        textbox.send_keys(value)
        options = self.get_descendant_elements(self.__OPT_XPATH)
        if len(options) > 0:
            options[0].click()

    def set_destination(self, value):
        self.__open()
        textbox = self.get_descendant_element(self.__DESTINATION_XPATH)
        textbox.send_keys(value)
        options = self.get_descendant_elements(self.__OPT_XPATH)
        if len(options) > 0:
            options[0].click()

    def __open(self):
        self.get_root_element().click()