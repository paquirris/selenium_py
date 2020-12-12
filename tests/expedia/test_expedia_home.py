import os
import pytest
from common.webdriver_factory import create_driver_instance, ROOT_DIR
from pages.expedia.home_page import HomePage

driver = create_driver_instance('chrome')
page = HomePage(driver, 5)
page.open()
page.wait_until_loaded()
page.list_property()
page.move_to_main_tab()

page.support()
page.move_to_main_tab()

page.trips()
page.move_to_main_tab()

page.select_tab('flights')
page.select_tab('stays')
page.stay.wait_until_loaded()
page.stay.destination.set_value('Guadalajara')

driver.quit()