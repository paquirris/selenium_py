import os
import pytest
from common.webdriver_factory import create_driver_instance, ROOT_DIR
from pages.expedia.home_page import HomePage
from components.expedia.calendar import Calendar
from components.expedia.input import Input
from components.expedia.move import Move


driver = create_driver_instance('chrome')
page = HomePage(driver, 5)
page.open()
page.wait_until_loaded()
page.select_tab('packages')
page.wait_until_loaded()

locations = Move(driver, 3)
locations.set_origin('Guadalajara')
locations.set_destination('Mexico')

dates = Calendar(driver, 2)
dates.select_dates(13,19)

